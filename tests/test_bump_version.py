"""Tests for the shared EMMO domain bump_version tool.

This file is IDENTICAL across the EMMO domain repos: it discovers the tooling
package under src/*/bump_version.py and exercises it against a synthetic
mini-repository, so it is independent of the host domain's real files.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

# ── module discovery (repo-agnostic) ─────────────────────────────────────────

_CANDIDATES = sorted((Path(__file__).parents[1] / "src").glob("*/bump_version.py"))
assert _CANDIDATES, "no src/*/bump_version.py found"
_spec = importlib.util.spec_from_file_location("bump_version", _CANDIDATES[0])
bv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(bv)


# ── synthetic mini-repo ──────────────────────────────────────────────────────

MAIN_TTL = """\
<https://w3id.org/emmo/domain/testdom> rdf:type owl:Ontology ;
    owl:versionIRI <https://w3id.org/emmo/domain/testdom/0.5.0/testdom> ;
    owl:imports <https://w3id.org/emmo/domain/testdom/0.5.0/dependencies> ;
    dcterms:issued "2020-01-01"^^xsd:date ;
    dcterms:modified "2020-01-01"^^xsd:date ;
    owl:backwardCompatibleWith "0.4.0" ;
    owl:priorVersion "0.4.0" ;
    owl:versionInfo "0.5.0" .
"""

MODULE_TTL = """\
<https://w3id.org/emmo/domain/testdom/modules/mod> rdf:type owl:Ontology ;
    owl:versionIRI <https://w3id.org/emmo/domain/testdom/0.5.0/modules/mod> ;
    owl:priorVersion <https://w3id.org/emmo/domain/testdom/0.4.0/modules/mod> ;
    owl:versionInfo "0.5.0" .
"""

CATALOG = """\
<?xml version="1.0"?>
<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">
    <uri name="https://w3id.org/emmo/domain/testdom/0.5.0/testdom" uri="./main.ttl"/>
</catalog>
"""

CONFIG = """\
ontology_name: "testdom"
version_tooling:
  main_ttl: "main.ttl"
  ttl_files:
    - "main.ttl"
    - "modules/mod.ttl"
  catalog_files:
    - "catalog-v001.xml"
  uri_segments:
    - "emmo/domain/testdom/"
"""


@pytest.fixture()
def mini_repo(tmp_path: Path, monkeypatch) -> Path:
    (tmp_path / "modules").mkdir()
    (tmp_path / "main.ttl").write_text(MAIN_TTL, encoding="utf-8")
    (tmp_path / "modules" / "mod.ttl").write_text(MODULE_TTL, encoding="utf-8")
    (tmp_path / "catalog-v001.xml").write_text(CATALOG, encoding="utf-8")
    (tmp_path / "config.yml").write_text(CONFIG, encoding="utf-8")
    monkeypatch.chdir(tmp_path)
    return tmp_path


# ── unit tests ───────────────────────────────────────────────────────────────

def test_calc_new_version():
    assert bv.calc_new_version("0.5.0", "patch") == "0.5.1"
    assert bv.calc_new_version("0.5.1", "minor") == "0.6.0"
    assert bv.calc_new_version("0.5.1", "major") == "1.0.0"


def test_get_current_version(mini_repo):
    assert bv.get_current_version(mini_repo, "main.ttl") == "0.5.0"


def test_bump_rewrites_everything(mini_repo):
    bv.main(["--version", "0.5.1"])
    main = (mini_repo / "main.ttl").read_text(encoding="utf-8")
    assert "testdom/0.5.1/testdom" in main
    assert "testdom/0.5.1/dependencies" in main
    assert 'owl:versionInfo "0.5.1"' in main
    assert "0.5.0/" not in main  # no stale segments outside prior-version lines
    catalog = (mini_repo / "catalog-v001.xml").read_text(encoding="utf-8")
    assert "testdom/0.5.1/testdom" in catalog


def test_prior_version_string_form_advanced(mini_repo):
    bv.main(["--version", "0.5.1"])
    main = (mini_repo / "main.ttl").read_text(encoding="utf-8")
    assert 'owl:priorVersion "0.5.0"' in main
    assert 'owl:backwardCompatibleWith "0.5.0"' in main


def test_prior_version_iri_form_advanced(mini_repo):
    bv.main(["--version", "0.5.1"])
    mod = (mini_repo / "modules" / "mod.ttl").read_text(encoding="utf-8")
    assert "owl:priorVersion <https://w3id.org/emmo/domain/testdom/0.5.0/modules/mod>" in mod
    assert "testdom/0.5.1/modules/mod" in mod  # versionIRI moved forward


def test_dates_updated_by_default(mini_repo):
    import datetime
    bv.main(["--version", "0.5.1"])
    main = (mini_repo / "main.ttl").read_text(encoding="utf-8")
    today = datetime.date.today().isoformat()
    assert f'dcterms:issued "{today}"' in main
    assert f'dcterms:modified "{today}"' in main


def test_no_dates_flag(mini_repo):
    bv.main(["--version", "0.5.1", "--no-dates"])
    main = (mini_repo / "main.ttl").read_text(encoding="utf-8")
    assert 'dcterms:issued "2020-01-01"' in main


def test_dry_run_writes_nothing(mini_repo):
    before = (mini_repo / "main.ttl").read_text(encoding="utf-8")
    bv.main(["--version", "0.5.1", "--dry-run"])
    assert (mini_repo / "main.ttl").read_text(encoding="utf-8") == before


def test_check_ok_after_bump(mini_repo):
    bv.main(["--version", "0.5.1"])
    with pytest.raises(SystemExit) as e:
        bv.main(["--check"])
    assert e.value.code == 0


def test_check_detects_drift(mini_repo):
    # Corrupt the catalog with a stale version
    cat = mini_repo / "catalog-v001.xml"
    cat.write_text(cat.read_text(encoding="utf-8").replace("0.5.0", "0.4.9"), encoding="utf-8")
    with pytest.raises(SystemExit) as e:
        bv.main(["--check"])
    assert e.value.code == 1


def test_same_version_is_noop(mini_repo, capsys):
    bv.main(["--version", "0.5.0"])
    assert "nothing to do" in capsys.readouterr().out
