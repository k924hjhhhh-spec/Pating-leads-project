# Painting Leads

South Florida painting-job lead marketplace prototype for Broward and Palm Beach.

## Current status

The first runnable slice includes a FastAPI service, a /health readiness endpoint, an /intake endpoint, and ALEX 1 customer-intake agent. The remaining official agents are documented in docs/architecture.md.

## Run locally

Install with uv, then set OPENAI_API_KEY only in your local environment:

    uv sync
    OPENAI_API_KEY=your_key_here uv run python main.py

Never commit API keys, customer credentials, or provider tokens.
