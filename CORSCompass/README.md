# CORSCompass

CORSCompass reviews exported cross-origin resource sharing policies for wildcard origins, unsafe credential combinations, broad headers, and anonymously exposed mutation methods.

```bash
python agent.py example_input.json
python -m unittest discover -s tests
```

It runs locally without credentials and never changes a live service. Confirm findings against the deployed gateway before remediation.
