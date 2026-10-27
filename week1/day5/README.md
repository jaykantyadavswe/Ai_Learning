# Day 5 — Resume Evaluation

## Topics

- Extracting text from PDF and DOCX resumes.
- Using an LLM to organize candidate information and compare it with a job
  description.
- Reviewing generated match scores and evaluations.

The runnable project is nested in
[`resume_evaluator`](./resume_evaluator/README.md). It processes resumes placed
directly in that project's `resumes` folder. AI-generated evaluations should
be reviewed by a person and should not be the sole basis for hiring decisions.

## Interview questions

**1. Why extract text before analyzing a resume?**  
The model needs text it can process; document parsing converts supported file
content into that text.

**2. Why compare resumes against a job description?**  
The job description provides role-specific criteria for evaluating relevant
skills and experience rather than assessing a resume in isolation.

**3. What are limitations of PDF text extraction?**  
Image-only or scanned PDFs may not contain extractable text and generally need
OCR before their contents can be analyzed.

**4. Why should a person review AI-generated hiring evaluations?**  
The model may overlook context, make unsupported inferences, or produce
inconsistent scores. Hiring decisions require human judgment and appropriate
handling of personal data.

For environment setup and run instructions, see the
[Resume Evaluator README](./resume_evaluator/README.md).
