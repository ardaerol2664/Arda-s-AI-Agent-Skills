"""Dependency-free checks for this package's simple scalar skill frontmatter and local files.

This is not a general YAML validator or a substitute claim for quick_validate.py.
"""
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
skill = ROOT / "codex-security"
text = (skill / "SKILL.md").read_text(encoding="utf-8")
match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
assert match, "frontmatter delimiters missing"
fields = {}
for line in match.group(1).splitlines():
    key, value = line.split(":", 1)
    assert key not in fields, "duplicate frontmatter key"
    fields[key] = value.strip()
assert set(fields) == {"name", "description"}
assert fields["name"] == "codex-security" and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fields["name"])
assert len(fields["name"]) <= 64 and 0 < len(fields["description"]) <= 1024
assert not any(mark in fields["description"] for mark in ("<", ">", "[TODO:"))
links = []
for document in ROOT.rglob("*.md"):
    content = document.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
        if re.match(r"[a-z]+://", target):
            continue
        destination = (document.parent / target.split("#", 1)[0]).resolve()
        assert destination.is_file(), (document, target)
        assert ROOT == destination or ROOT in destination.parents, "link escapes package"
        links.append(str(destination.relative_to(ROOT)))
sources = list(ROOT.rglob("*.py"))
for source in sources:
    ast.parse(source.read_text(encoding="utf-8"), filename=str(source), feature_version=8)
required = ["LICENSE", "PROJE_BAGLAMI.md", "DEGISIKLIK_RAPORU.md",
            "codex-security/README.md", "codex-security/references/contracts.md",
            "codex-security/references/workflow.md", "codex-security/scripts/panel.py",
            "tests/evidence/ab-baseline.json", "tests/evidence/ab-revised.json",
            "tests/evidence/panel-tests.json", "tests/evidence/review.md"]
assert all((ROOT / name).is_file() for name in required), "required record missing"
for record in (ROOT / "tests/evidence").glob("*.json"):
    json.loads(record.read_text(encoding="utf-8"))
print(json.dumps({"passed": True, "scalar_frontmatter": True, "local_links": len(links),
                  "python38_syntax_files": len(sources), "required_records": len(required)}, indent=2))
