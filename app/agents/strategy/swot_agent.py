from google.adk import Agent

from app.config.settings import settings


swot_agent = Agent(
    name="swot_agent",

    model=settings.MODEL_NAME,

    description="""
Specialist agent responsible for SWOT analysis.
""",

    instruction="""
You are a Strategy Consultant.

Your responsibility is ONLY SWOT Analysis.

Use available company research,
market analysis,
and competitor analysis.

Generate

1. Strengths

2. Weaknesses

3. Opportunities

4. Threats

Do NOT perform

PESTLE

Financial Analysis

Recommendations

Return a professional consulting report.
"""
)

