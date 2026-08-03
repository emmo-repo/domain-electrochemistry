"""Catalog-vs-imports consistency check (P0.1 / future P3.2 CI job).

For a repo: collect every owl:imports IRI from tracked .ttl files, collect every
<uri name=...> entry from catalog-v001.xml files, and report:
  1. imports with NO catalog entry (offline resolution will fail)
  2. catalog entries pointing at moving targets (refs/heads/, /master/, /main/)
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def check(repo: Path) -> int:
    ttls = [p for p in repo.rglob("*.ttl")
            if ".venv" not in p.parts and "build" not in p.parts
            and not p.name.endswith("-inferred.ttl")]
    catalogs = [p for p in repo.rglob("catalog-v001.xml") if ".venv" not in p.parts]

    imports = {}  # iri -> [files]
    for t in ttls:
        txt = t.read_text(encoding="utf-8", errors="replace")
        # owl:imports may list multiple IRIs separated by commas
        for m in re.finditer(r"owl:imports\s+((?:<[^>]+>\s*,\s*)*<[^>]+>)", txt):
            for iri in re.findall(r"<([^>]+)>", m.group(1)):
                imports.setdefault(iri, []).append(str(t.relative_to(repo)))

    catalog_names = set()
    moving = []
    for c in catalogs:
        root = ET.parse(c).getroot()
        for uri in root.iter("{urn:oasis:names:tc:entity:xmlns:xml:catalog}uri"):
            name, target = uri.get("name"), uri.get("uri")
            catalog_names.add(name)
            if target and re.search(r"refs/heads/|/(master|main)/", target):
                moving.append((str(c.relative_to(repo)), name, target))

    missing = {i: fs for i, fs in imports.items()
               if i not in catalog_names and not i.startswith("http://www.w3.org")}

    print(f"### {repo.name}: {len(ttls)} ttl, {len(catalogs)} catalogs, "
          f"{len(imports)} distinct imports, {len(catalog_names)} catalog entries")
    if missing:
        print(f"  MISSING catalog entries ({len(missing)}):")
        for iri, fs in sorted(missing.items()):
            print(f"    {iri}\n      imported by: {', '.join(sorted(set(fs)))}")
    if moving:
        print(f"  MOVING-TARGET catalog entries ({len(moving)}):")
        for c, n, t in sorted(set(moving)):
            print(f"    [{c}] {n}\n      -> {t}")
    if not missing and not moving:
        print("  OK: all imports catalog-resolvable at pinned versions; no moving targets")
    return 1 if (missing or moving) else 0

if __name__ == "__main__":
    rc = 0
    for arg in sys.argv[1:]:
        rc |= check(Path(arg))
        print()
    sys.exit(rc)
