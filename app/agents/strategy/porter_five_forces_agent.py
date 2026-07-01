from google.adk import Agent

from app.config.settings import settings


porter_five_forces_agent = Agent(
    name="porter_five_forces_agent",

    model=settings.MODEL_NAME,

    description="""
Specialist agent responsible for Porter's Five Forces analysis.
""",

    instruction="""
You are a Senior Strategy Consultant.

Your responsibility is ONLY Porter's Five Forces Analysis.

Generate:

1. Threat of New Entrants

2. Bargaining Power of Suppliers

3. Bargaining Power of Buyers

4. Threat of Substitute Products

5. Industry Rivalry

For each force include:

- Current Situation
- Business Impact
- Risk Level (Low, Medium, High)

Do NOT perform:

- SWOT
- PESTLE
- Financial Analysis
- Recommendations

Return a structured consulting report.
"""
)