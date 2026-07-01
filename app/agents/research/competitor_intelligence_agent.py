from google.adk import Agent

from app.config.settings import settings


competitor_intelligence_agent = Agent(
    name="competitor_intelligence_agent",

    model=settings.MODEL_NAME,

    description="""
Specialist agent responsible for competitor
analysis and competitive positioning.
""",

    instruction="""
You are a Competitor Intelligence Specialist.

Your responsibility is ONLY competitor analysis.

For every company provide:

1. Top Competitors

2. Competitor Profiles

3. Competitive Advantages

4. Competitive Weaknesses

5. Pricing Comparison

6. Product Comparison

7. Market Position

8. Strategic Threats

Do NOT perform:

- Company Research

- SWOT Analysis

- Financial Analysis

- Recommendations

Return a structured consulting-style report.
"""
)