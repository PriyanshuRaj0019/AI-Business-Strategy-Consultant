from langgraph.graph import StateGraph, END

from app.graph.state import BusinessState
from app.graph.nodes import (
    research_node,
    market_node,
    competitor_node,
    swot_node,
    pestle_node,
    porter_node,
    finance_node,
    strategy_node,
    executive_node,
)

builder = StateGraph(BusinessState)

# ==========================
# Nodes
# ==========================

builder.add_node("research", research_node)
builder.add_node("market", market_node)
builder.add_node("competitor", competitor_node)
builder.add_node("swot", swot_node)
builder.add_node("pestle", pestle_node)
builder.add_node("porter", porter_node)
builder.add_node("finance", finance_node)
builder.add_node("strategy", strategy_node)
builder.add_node("executive", executive_node)

# ==========================
# Flow
# ==========================

builder.set_entry_point("research")

builder.add_edge("research", "market")
builder.add_edge("market", "competitor")
builder.add_edge("competitor", "swot")
builder.add_edge("swot", "pestle")
builder.add_edge("pestle", "porter")
builder.add_edge("porter", "finance")
builder.add_edge("finance", "strategy")
builder.add_edge("strategy", "executive")
builder.add_edge("executive", END)

# ==========================
# Compile
# ==========================

business_graph = builder.compile()