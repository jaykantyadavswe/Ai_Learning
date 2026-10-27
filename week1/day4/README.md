# Day 4 — Structured JSON with Pydantic

## Topics

- Asking a model to extract fields from unstructured text.
- Using a Pydantic model to define the expected data shape.
- Requesting JSON output, parsing it, and validating it with Pydantic.

The example extracts contact and issue details from a customer ticket, parses
the JSON response, and accesses the validated `Ticket` fields.

## Run

From this folder:

```powershell
uv sync
uv run python .\json_pydantic.py
```

Set `GROQ_API_KEY` in a `.env` file in this folder first.

## Interview questions

**1. What is structured output?**  
It is model output constrained to a predictable data format, such as JSON with
known fields.

**2. What does a Pydantic model provide here?**  
It defines the expected fields and validates parsed data against their types
and requirements.

**3. Why parse JSON before creating a `Ticket`?**  
Parsing converts the JSON string into Python data; the model can then validate
that data and expose it through typed attributes.

**4. Is asking the model for JSON enough to guarantee valid data?**  
No. Validate the response, handle malformed or missing data, and treat model
output as untrusted input.
