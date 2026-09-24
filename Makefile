PY := uv run --quiet --with pyyaml==6.0.2 python scripts/catalog.py

.PHONY: validate render check public properties
validate: ; $(PY) validate
render:   ; $(PY) render
check:    ; $(PY) validate --offline && $(PY) render --check
# Leak-check a local checkout of the public Algorythmos-AI/.github repo: make public PUBLIC=../.github
public:   ; $(PY) check-public $(PUBLIC)
# Org custom properties from the catalog: dry-run first, then `make properties APPLY=--apply`
properties: ; $(PY) properties $(APPLY)
