from google.adk import Agent

from app.config.settings import settings

# Research Team
from app.agents.research.company_research_agent import (
    company_research_agent,
)
from app.agents.research.market_intelligence_agent import (
    market_intelligence_agent,
)
from app.agents.research.competitor_intelligence_agent import (
    competitor_intelligence_agent,
)

# Strategy Team
from app.agents.strategy.swot_agent import swot_agent
from app.agents.strategy.pestle_agent import pestle_agent
from app.agents.strategy.porter_five_forces_agent import (
    porter_five_forces_agent,
)

# Finance Team
from app.agents.finance.financial_analysis_agent import (
    financial_analysis_agent,
)

# Executive Team
from app.agents.executive.recommendation_agent import (
    recommendation_agent,
)
from app.agents.executive.executive_report_agent import (
    executive_report_agent,
)

# MCP Server
from app.mcp.company_server import CompanyMCPServer


company_server = CompanyMCPServer()


business_strategy_manager = Agent(
    name="business_strategy_manager",

    model=settings.MODEL_NAME,

    description="""
Root agent responsible for coordinating all business consulting agents.
""",

    instruction="""
You are the Business Strategy Manager.

Your job is to coordinate specialist business consulting agents.

Before delegating research tasks, use the Company MCP tool to retrieve
available company information.

Use that information as context for downstream agents.

Delegate work as follows:

• Company overview
→ company_research_agent

• Industry analysis
→ market_intelligence_agent

• Market analysis
→ market_intelligence_agent

• Competitor analysis
→ competitor_intelligence_agent

• SWOT analysis
→ swot_agent

• PESTLE analysis
→ pestle_agent

• Porter's Five Forces
→ porter_five_forces_agent

• Financial analysis
→ financial_analysis_agent

• Strategic recommendations
→ recommendation_agent

• Executive report
→ executive_report_agent

Never perform specialist analysis yourself.

Always delegate to the appropriate specialist agent.

Return the final response in a structured professional consulting format.
""",

    sub_agents=[
        company_research_agent,
        market_intelligence_agent,
        competitor_intelligence_agent,
        swot_agent,
        pestle_agent,
        porter_five_forces_agent,
        financial_analysis_agent,
        recommendation_agent,
        executive_report_agent,
    ],

    tools=[
        company_server.get_company,
    ],
)