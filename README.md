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

Run these commands from the repository's `Jaykant_AI_Learning` folder. For
days 1–4, choose the day you want to work on:

```powershell
Set-Location .\week1\day1
# Or use .\week1\day2, .\week1\day3, or .\week1\day4.
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
```

The day 1 Groq example needs an API key. Create a `.env` file in that day's
folder (the same folder as `pyproject.toml`) with:

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
  [resume evaluator](./week1/day5/resume_evaluator/README.md).

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