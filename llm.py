import google.generativeai as genai
from google.api_core.exceptions import ResourceExhausted, GoogleAPIError

# 🔴 DIRECT API KEY (for local testing only)
genai.configure(api_key="AIzaSyB_gnRek0-HLxviVLiZtfCuoNQ-qldVM7o")

# ✅ v1beta compatible model
MODEL = "gemini-2.5-flash"
model = genai.GenerativeModel(MODEL)


def analyze_clause(text, question):
    prompt = f"""
Clause:
{text}

Question:
{question}

Provide:
- Simple explanation
- Risk score (0–10)
- Obligations
- Missing points
"""
    return _generate(prompt)


def extract_clauses(text):
    prompt = f"""
Extract clauses in JSON format:
[
  {{"id": 1, "title": "...", "text": "..."}}
]

Document:
{text}
"""
    return _generate(prompt)


def compare_clauses(a, b):
    prompt = f"""
Compare clauses A and B.

Return:
- Differences
- Similarities
- Risk analysis
- Which is safer for user?
- Negotiation suggestions

Clause A:
{a}

Clause B:
{b}
"""
    return _generate(prompt)


def _generate(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text

    except ResourceExhausted:
        return "AI quota exceeded. Please try again later."

    except GoogleAPIError as e:
        return f"AI service error: {str(e)}"

    except Exception as e:
        return f"Unexpected error: {str(e)}"
