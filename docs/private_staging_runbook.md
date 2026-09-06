# Private staging runbook

## Required environment

- Python 3.11+
- Dependencies from pyproject.toml
- OPENAI_API_KEY configured as a private environment secret
- No secrets committed to GitHub

## Smoke test

1. Install dependencies.
2. Run the API with `python main.py`.
3. Check `GET /health`.
4. Send a test request to `POST /intake`.
5. Send the returned intake to `POST /boss`.
6. Confirm the report includes status, workers, next move, risks, and approval needs.
7. Confirm money and external actions remain blocked.
8. Stop the service if any test would contact a real person or spend money.

## Go-live gate

The owner must approve the hosting provider, domain, external connectors,
data-retention policy, and worker autonomy level before private deployment.
