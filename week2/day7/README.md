# Day 7 — ReAct and Tool Calling

## Topics

- A ReAct-style loop: model decision, tool action, observation, and next step.
- Exposing Python functions as tools the model can request.
- Limiting the number of agent iterations.

The example provides product-price lookup and a calculator, parses an action
from the model response, executes it, and returns the observation for another
step.

## Run

From this folder:

```powershell
uv sync
uv run python .\reAct.py
```

Set `GROQ_API_KEY` in a `.env` file in this folder first.

## Interview questions

**1. What does ReAct mean in an LLM workflow?**  
It combines reasoning with actions: the model selects an action, receives its
result, and uses that observation to continue.

**2. What is an observation in a tool-using agent?**  
It is the result returned by an executed tool and added back to the conversation
as input for the model's next decision.

**3. Why restrict tool names and arguments?**  
Allowlisting tools and validating their inputs limits what model-generated
requests can execute and makes failures easier to handle.

**4. Why is Python `eval` unsafe for user-controlled expressions?**  
It can execute arbitrary Python expressions, not just arithmetic. Use a
restricted parser or a purpose-built safe calculator instead of evaluating
untrusted input.
