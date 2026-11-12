#!/usr/bin/env python3
"""Basic all-explicit-atom model QA; not a chemistry or stereo validator."""
import argparse
from collections import Counter
import json
import math
from pathlib import Path

ELEMENTS = set('H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og'.split())


def validate(data, planar_ids=None, tolerance=0.03):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return {'errors': ['Root must be an object'], 'warnings': []}
    atoms, bonds = data.get('atoms'), data.get('bonds')
    if not isinstance(atoms, list) or not atoms:
        return {'errors': ['atoms must be a nonempty list'], 'warnings': []}
    if not isinstance(bonds, list):
        return {'errors': ['bonds must be a list'], 'warnings': []}
    by_id, counts, valences = {}, Counter(), Counter()
    for a in atoms:
        if not isinstance(a, dict):
            errors.append('Atom must be an object')
            continue
        aid = a.get('id')
        if type(aid) is not int or aid in by_id:
            errors.append('Atom IDs must be unique integers')
            continue
        element = a.get('element')
        if not isinstance(element, str) or element not in ELEMENTS:
            errors.append(f'Atom {aid}: unknown element')
            continue
        if type(a.get('charge')) is not int:
            errors.append(f'Atom {aid}: charge must be an integer')
            continue
        xyz = [a.get(k) for k in ('x', 'y', 'z')]
        if not all(type(v) in (int, float) and math.isfinite(v) for v in xyz):
            errors.append(f'Atom {aid}: coordinates must be finite numbers')
            continue
        by_id[aid] = a
        counts[element] += 1
    if errors:
        return {'errors': errors, 'warnings': warnings}
    keys = sorted(counts)
    if 'C' in counts:
        keys = ['C'] + (['H'] if 'H' in counts else []) + sorted(set(counts) - {'C', 'H'})
    formula = ''.join(k + (str(counts[k]) if counts[k] != 1 else '') for k in keys)
    if data.get('formula') != formula:
        errors.append(f'Formula mismatch: counted {formula}; use Hill notation and explicit H')
    charge = sum(a['charge'] for a in atoms)
    if type(data.get('charge')) is not int or data['charge'] != charge:
        errors.append(f'Charge mismatch: counted {charge}')
    if not data.get('coordinate_method'):
        errors.append('coordinate_method is required')
    seen = set()
    for b in bonds:
        if not isinstance(b, dict):
            errors.append('Bond must be an object')
            continue
        a, c, order = b.get('a'), b.get('b'), b.get('order')
        if type(a) is not int or type(c) is not int or a not in by_id or c not in by_id or a == c:
            errors.append('Bond endpoints must be distinct existing integer IDs')
            continue
        pair = tuple(sorted((a, c)))
        if pair in seen:
            errors.append(f'Duplicate bond {pair}')
        seen.add(pair)
        if type(order) not in (int, float) or order not in (1, 1.5, 2, 3):
            errors.append(f'Unsupported bond order for {pair}')
            continue
        valences[a] += order
        valences[c] += order
        distance = math.dist([by_id[a][k] for k in ('x','y','z')], [by_id[c][k] for k in ('x','y','z')])
        if distance > 3:
            warnings.append(f'Bond {pair}: {distance:.3f} Å; verify chemistry and units')
    for i, a in enumerate(atoms):
        for b in atoms[i+1:]:
            distance = math.dist([a[k] for k in ('x','y','z')], [b[k] for k in ('x','y','z')])
            if distance < 0.35:
                errors.append(f'Near-coincident atoms {a["id"]}, {b["id"]}')
        v = valences[a['id']]
        if a['element'] == 'H' and v > 1:
            warnings.append(f'H {a["id"]}: valence {v}; verify nonstandard bonding')
        if a['element'] == 'C' and a['charge'] == 0 and v != 4:
            warnings.append(f'C {a["id"]}: bond-order sum {v}; verify H, radical or unusual state')
        if v == 0 and len(atoms) > 1:
            warnings.append(f'Atom {a["id"]} has no bonds; verify disconnected species')
    result = {'formula': formula, 'charge': charge, 'atom_count': len(atoms), 'bond_count': len(bonds), 'errors': errors, 'warnings': warnings}
    if planar_ids is not None:
        if len(planar_ids) < 3 or len(set(planar_ids)) != len(planar_ids) or any(i not in by_id for i in planar_ids):
            errors.append('Plane check requires >=3 distinct existing atom IDs')
        else:
            import numpy as np
            coords = np.array([[by_id[i][k] for k in ('x','y','z')] for i in planar_ids])
            centered = coords - coords.mean(axis=0)
            _, singular, vh = np.linalg.svd(centered, full_matrices=False)
            if singular[1] < 1e-8:
                errors.append('Plane check is undefined for collinear atoms')
            else:
                deviation = float(np.max(np.abs(centered @ vh[-1])))
                result['max_plane_deviation_A'] = deviation
                if deviation > tolerance:
                    errors.append(f'Plane deviation {deviation:.6f} Å exceeds {tolerance} Å')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model', type=Path)
    parser.add_argument('--planar-ids', help='Comma-separated atom IDs')
    parser.add_argument('--planarity-tol', type=float, default=0.03)
    args = parser.parse_args()
    try:
        if not math.isfinite(args.planarity_tol) or args.planarity_tol < 0:
            raise ValueError('planarity tolerance must be finite and nonnegative')
        ids = [int(x) for x in args.planar_ids.split(',')] if args.planar_ids else None
        result = validate(json.loads(args.model.read_text()), ids, args.planarity_tol)
    except (ValueError, OSError, ImportError) as exc:
        result = {'errors': [str(exc)], 'warnings': []}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if result['errors'] else 0)


if __name__ == '__main__':
    main()
