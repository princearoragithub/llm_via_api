# LLM Connector

A simple Python utility to connect with multiple LLM providers (OpenAI, Anthropic, and Google's Gemini) through a single interface.

## Setup

1. Install `uv` if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create and activate a new virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Unix/macOS
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. Sync the project dependencies:
   ```bash
   uv sync
   ```

4. Create a `.env` file by copying the template:
   ```bash
   cp .env.template .env
   ```

5. Add your API keys to the `.env` file:
   - Get OpenAI API key from: https://platform.openai.com/api-keys
   - Get Anthropic API key from: https://console.anthropic.com/
   - Get Google API key from: https://makersuite.google.com/app/apikey

## Usage

```python
from llm_connector import get_llm_response

# Example with OpenAI
response = get_llm_response(
    provider="openai",  # Choose from: "openai", "anthropic", "gemini"
    prompt="What is the capital of France?",
    model="gpt-3.5-turbo",  # Optional: defaults to provider-specific models
    temperature=0.7  # Optional: controls response randomness
)
print(response)
```

## Supported Providers and Default Models

- OpenAI: `gpt-3.5-turbo`
- Anthropic: `claude-3-sonnet-20240229`
- Google: `gemini-pro`

You can specify different models for each provider using the `model` parameter.

## Development

To update dependencies or add new ones, modify the `pyproject.toml` file and run:
```bash
uv pip install .
```

## Why uv?

We use `uv` as our Python package installer because:
- It's significantly faster than pip (up to 10-100x)
- Has built-in virtual environment management
- Provides reliable and reproducible installations
- Supports modern Python packaging standards 