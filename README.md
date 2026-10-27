# AI Learning

Hands-on AI and Python practice, organized by week and day. Each day is an
independent Python project with its own dependencies and virtual environment.


## Project structure

```text
week1/
  day1/   # Python 3.14, Groq API example
  day2/   # Python 3.11, Groq API practice
  day3/   # Groq token usage
  day4/   # Structured JSON output with Pydantic
  day5/
    resume_evaluator/  # Resume parsing and AI-based job matching

week2/
  day6/   # Prompt engineering and role-based task design
  day7/   # ReAct reasoning and tool-calling workflow
  day8/   # Prompt chaining for resume-to-job matching
  day9/   # Streaming model responses in real time
  hiremeAi/  # AI resume parsing and recruiter Q&A

week3/
  day1/   # Keyword-based retrieval with an LLM response
  day2/   # Text embeddings and cosine similarity
  day3/   # Retrieval-augmented generation (RAG)
```


## Prerequisites

- Windows with PowerShell
- Git
- Python (each project's required version is listed in its `.python-version`)
- [uv](https://docs.astral.sh/uv/) for Python and project management

Install uv on Windows with:

```powershell
winget install --id=astral-sh.uv -e
```

Restart PowerShell, then check that uv is available:

```powershell
uv --version
```


## Set up a project

Run these commands from the repository's `Jaykant_AI_Learning` folder. Choose
the project folder you want to work on:

```powershell
Set-Location .\week1\day1
# Other examples: .\week1\day2, .\week2\day6, or .\week3\day2.
```

Install the Python version configured for that project and sync its locked
dependencies:

```powershell
uv python install
uv sync
```

`uv sync` creates the project's `.venv` and installs dependencies from
`uv.lock`. You can run commands through uv without activating the environment:

```powershell
uv run python --version
```

To activate the environment in PowerShell instead:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation scripts, you can keep using `uv run` above, or
allow scripts for just the current PowerShell session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

When finished, leave the environment with:

```powershell
deactivate
```

Day 5 is in a nested project and currently uses a `venv` with pip. From the
`Jaykant_AI_Learning` folder, set it up with:

```powershell
Set-Location .\week1\day5\resume_evaluator
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install groq pypdf python-docx python-dotenv pydantic
```

Create a `.env` file in that folder with your `GROQ_API_KEY`, then add PDF or
DOCX resumes directly to its `resumes` folder. See the
[Day 5 project README](./week1/day5/resume_evaluator/README.md) for details.


## Run the examples

From the selected day's folder:

```powershell
# Day 1
uv run python .\hello.llm.py

# Day 2
uv run python .\sys_temp.py

# Day 3
uv run python .\tokens.py

# Day 4
uv run python .\json_pydantic.py

# Day 5 (from week1\day5\resume_evaluator)
.\.venv\Scripts\python.exe .\resume_parser.py

# Day 6
uv run python .\prompt_engg.py

# Day 7
uv run python .\reAct.py

# Day 8
uv run python .\prompt_chaining.py

# Day 9
uv run python .\streaming.py

# Week 2 HireMeAI (from week2\hiremeAi\backend)
uv run uvicorn main:app --reload

# Week 3, Day 2
uv run python .\embed_rag.py

# Week 3, Day 3
uv run python .\full_rag.py

# Week 3, Day 1
uv run python .\rag_intro.py
```

The Groq examples in Week 1 Day 1, Week 2 HireMeAI, and Week 3 Days 1 and 3
need an API key. For HireMeAI, put the `.env` file in
`week2\hiremeAi\backend`; for the other examples, put it in the day's project
folder (the same folder as `pyproject.toml`). Use:

```dotenv
GROQ_API_KEY=your_groq_api_key
```

Keep real API keys private. `.env` files are ignored by Git; never paste a
secret into source code or commit it.

## What I'm learning

- **Day 3 — Token usage:** Send multiple prompts to the Groq chat completions
  API and inspect prompt, completion, and total token counts, along with the
  response finish reason. See [day3/tokens.py](./week1/day3/tokens.py).
- **Day 4 — Structured output:** Describe ticket fields with a Pydantic model,
  request JSON from the Groq API, parse and validate the response, and access
  the extracted fields. See [day4/json_pydantic.py](./week1/day4/json_pydantic.py).
- **Day 5 — Resume evaluation:** Extract text from PDF and DOCX resumes, use
  the Groq API to organize candidate details and compare them with a job
  description, then review the generated scores and evaluations. See the
  [resume evaluator](./week1/day5/resume_evaluator/README.md) and
  [Day 5 topics and interview questions](./week1/day5/README.md).
- See the [Day 1](./week1/day1/README.md), [Day 2](./week1/day2/README.md),
  [Day 3](./week1/day3/README.md), and
  [Day 4](./week1/day4/README.md) guides for topics and interview Q&A.

## Week 2 analysis

Week 2 focused on moving from basic LLM usage to better prompt design and
practical AI workflows. The main lesson was that model quality improves not
just from larger models, but from clearer instructions, structured outputs, and
well-defined reasoning steps.

- **Day 6 — Prompt engineering:** Learned how to define a role, constraints,
  output format, examples, and fallback behavior in a single prompt. This makes
  the AI more reliable for classification tasks and reduces ambiguous responses.
- **Day 7 — ReAct pattern:** Built a simple tool-using agent that thinks,
  chooses an action, receives an observation, and then decides the next step.
  This introduced the core idea behind agentic workflows: break work into
  reasoning + tool execution + feedback loops.
- **Day 8 — Prompt chaining:** Split a workflow into multiple stages: extract
  skills from a resume, extract skills from a job description, then compare both
  and score the match. This is a practical pattern for multi-step AI tasks.
- **Day 9 — Streaming responses:** Implemented incremental output generation so
  the model's answer appears in real time instead of waiting for the full
  response. This is useful for chat UX, long-form generation, and progressive
  feedback.
- **HireMeAI — Resume Q&A application:** Built a FastAPI backend that extracts
  text from a candidate's PDF resume, uses a Groq model to structure the
  candidate profile, and answers recruiter questions using that profile.
  Run it from `week2\hiremeAi\backend` with `uv run uvicorn main:app --reload`;
  Swagger docs are available at `http://127.0.0.1:8000/docs`. See the
  [HireMeAI project README](./week2/hiremeAi/README.md) for setup details.
- See the [Day 6](./week2/day6/README.md), [Day 7](./week2/day7/README.md),
  [Day 8](./week2/day8/README.md), and [Day 9](./week2/day9/README.md) guides
  for topics and interview Q&A.

Overall, Week 2 showed how to build more dependable AI systems by combining
prompt structure, tool use, and workflow orchestration instead of relying on a
single raw prompt.

## Week 3 analysis

Week 3 introduces the foundations of retrieval-augmented generation (RAG):
turning text into vector embeddings, finding relevant information by semantic
similarity, and using retrieved context to ground an LLM response.

- **Day 1 — Introductory retrieval:** Created a small in-memory knowledge base,
  selected context with simple keyword checks, and supplied it to the Groq chat
  completions API so the response is grounded in the retrieved information.
  See [day1/rag_intro.py](./week3/day1/rag_intro.py).
- **Day 2 — Text embeddings and cosine similarity:** Used the
  `all-MiniLM-L6-v2` Sentence Transformer model to encode text as vectors, then
  compared sentence embeddings with cosine similarity. This demonstrates how
  sentences with similar meanings can be matched even when their wording differs.
  See [day2/embed_rag.py](./week3/day2/embed_rag.py).
- **Day 3 — Basic RAG workflow:** Encoded a small collection of employee-policy
  documents, retrieved the document most similar to a question, and passed that
  context to the Groq chat completions API to generate a grounded answer. The
  example requires `GROQ_API_KEY` in the day's `.env` file.
  See [day3/full_rag.py](./week3/day3/full_rag.py).
- See the [Day 1](./week3/day1/README.md), [Day 2](./week3/day2/README.md),
  and [Day 3](./week3/day3/README.md) guides for topics and interview Q&A.

Together, these examples show the core RAG sequence: embed the source content
and query, retrieve relevant context, then use that context to guide generation.

## Adding dependencies

Add a package from the relevant day's folder so uv updates that project's
`pyproject.toml` and `uv.lock`:

```powershell
uv add package-name
```

For example:

```powershell
uv add requests
```

After pulling changes that update `uv.lock`, run `uv sync` again.

<!-- Folder initilization -->
<!-- uv init day3, uv init .venv --python 3.11 -->
<!-- py -m venv .venv -->
<!-- Activation code: .\.venv\Scripts\activate.ps1 -->
<!-- uv add groq python-dotenv -->