# SBOMScout

SBOMScout audits CycloneDX-like software bills of materials for missing versions, package URLs, licences, and integrity hashes.

```bash
python agent.py example_input.json
python -m unittest discover -s tests
```

The check is deterministic and offline; vulnerability status still requires a current advisory source.
