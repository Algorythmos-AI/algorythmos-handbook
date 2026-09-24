PY := uv run --quiet --with pyyaml==6.0.2 python scripts/catalog.py

.PHONY: validate render check public
validate: ; $(PY) validate
render:   ; $(PY) render
check:    ; $(PY) validate --offline && $(PY) render --check
# Leak-check a local checkout of the public Algorythmos-AI/.github repo: make public PUBLIC=../.github
public:   ; $(PY) check-public $(PUBLIC)
