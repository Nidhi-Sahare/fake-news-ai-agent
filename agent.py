from config import get_model_response
import re
def analyze_claim(claim: str):
    """
    Fake News Verification Intelligent Agent
    Uses Gemini for reasoning + structured analysis
    """
    prompt = f"""
You are an Intelligent Fake News Verification Agent.
Your task is to analyze the claim step-by-step like a reasoning system.
Follow this pipeline:
1. Extract the main claim
2. Identify type (fact / opinion / rumor / exaggeration)
3. Check logical consistency
4. Identify possible misinformation signals
5. Assign credibility score (0-100)
6. Give verdict:
   - True
   - False
   - Misleading
   - Unverified
7. Provide reasoning in bullet points
8. Give final recommendation
Rules:
- Be strict and analytical
- Do NOT assume real-world facts
- If unsure, mark as Unverified
INPUT CLAIM:
{claim}
OUTPUT:
Structured explanation with clear sections.
"""
    return get_model_response(prompt)
def extract_score(text: str):
    """
    Extract credibility score from Gemini response
    """
    matches = re.findall(r"\b(100|[1-9]?[0-9])\b", text)
    if matches:
        scores = [int(m) for m in matches]

        return min(max(scores[0], 0), 100)

    return 50


