# AI Engineer Journey

Learning AI engineering in public: one build and one post every day.
Roadmap: LLM basics, prompt and context engineering, RAG, MCP, agents, LLM observability.

## Day 1: First LLM API call
- Python virtual environment, API key stored in `.env` (never committed)
- `hello_llm.py` sends one prompt to a model through the Groq API and prints the reply

### Run it
1. `python -m venv venv` and activate it
2. `pip install -r requirements.txt`
3. Create a `.env` file with `GROQ_API_KEY=your_key`
4. `python hello_llm.py`

### What I learned
- Training builds the model. Inference is using it.
- Keep secrets in environment variables.
- Fixed a 404 `model_not_found` (retired model name) and a Windows `UnicodeEncodeError`.

## Progress
| Day | Topic           | Status |
|-----|-----------------|--------|
| 1   | First API call  | Done   |
| 2   | Tokens and cost | Next   |
