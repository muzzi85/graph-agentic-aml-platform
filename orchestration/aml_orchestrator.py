from typing import TypedDict
import ollama

class AMLState(TypedDict):

    account_id: int

    investigation_context: dict

    aml_analysis: str

    fraud_analysis: str

    final_report: str

from rag.graph_retrieval import (
    build_investigation_context
)

def retrieve_context(
    state: AMLState
):

    account_id = state["account_id"]

    context = build_investigation_context(
        account_id
    )

    return {
        "investigation_context": context
    }

def analyze_aml_risk(
    state: AMLState
):

    context = state[
        "investigation_context"
    ]

    suspicious_neighbors = len(
        context["suspicious_neighbors"]
    )

    cycles = len(
        context["cycles"]
    )

    graph_metrics = context[
        "graph_metrics"
    ][0]

    analysis = f"""

    AML Investigation Summary

    Account ID:
    {context["account_id"]}

    Suspicious Neighbors:
    {suspicious_neighbors}

    Detected Cycles:
    {cycles}

    Degree Centrality:
    {graph_metrics["degree_centrality"]:.6f}

    Betweenness Centrality:
    {graph_metrics["betweenness_centrality"]:.6f}

    Final AML Score:
    {graph_metrics["final_aml_score"]:.6f}

    """

    return {
        "aml_analysis": analysis
    }

def aml_agent(
    state: AMLState
):

    context = state[
        "investigation_context"
    ]

    graph_metrics = context[
        "graph_metrics"
    ][0]

    suspicious_neighbors = len(
        context["suspicious_neighbors"]
    )

    cycles = len(
        context["cycles"]
    )

    prompt = f"""

    You are an AML investigation AI.

    ONLY use the provided graph evidence.

    DO NOT mention:
    - malware
    - ransomware
    - cybersecurity
    - hacking
    - attacks

    ONLY discuss:
    - transaction behavior
    - suspicious graph topology
    - laundering indicators
    - suspicious connectivity

    CASE DATA:

    Account ID:
    {context["account_id"]}

    Final AML Score:
    {graph_metrics["final_aml_score"]:.6f}

    Suspicious Neighbors:
    {suspicious_neighbors}

    Detected Cycles:
    {cycles}

    Degree Centrality:
    {graph_metrics["degree_centrality"]:.6f}

    Betweenness Centrality:
    {graph_metrics["betweenness_centrality"]:.6f}

    Explain:
    1. Why this account appears suspicious
    2. Graph-based laundering concerns
    3. Recommended AML action

    Keep answer concise and professional.

    """

    response = ollama.chat(

        model="tinyllama",

        messages=[

            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    analysis = response[
        "message"
    ][
        "content"
    ]

    return {

        "aml_analysis": analysis
    }

def aml_agent_without_LLM(
    state: AMLState
):

    context = state[
        "investigation_context"
    ]

    graph_metrics = context[
        "graph_metrics"
    ][0]

    suspicious_neighbors = len(
        context["suspicious_neighbors"]
    )

    cycles = len(
        context["cycles"]
    )

    analysis = f"""

    AML Investigation Analysis

    Account:
    {context["account_id"]}

    Final AML Score:
    {graph_metrics["final_aml_score"]:.6f}

    Suspicious Neighbors:
    {suspicious_neighbors}

    Cycles Detected:
    {cycles}

    Assessment:
    Account demonstrates suspicious
    graph topology behavior consistent
    with potential laundering activity.

    """

    return {
        "aml_analysis": analysis
    }

def fraud_agent(
    state: AMLState
):

    context = state[
        "investigation_context"
    ]

    suspicious_neighbors = len(
        context["suspicious_neighbors"]
    )

    if suspicious_neighbors > 5:

        severity = "HIGH"

    else:

        severity = "MEDIUM"

    analysis = f"""

    Fraud Risk Analysis

    Neighbor Fraud Exposure:
    {suspicious_neighbors}

    Fraud Severity:
    {severity}

    Assessment:
    Account shows elevated exposure
    to suspicious entities.

    """

    return {
        "fraud_analysis": analysis
    }

def synthesize_investigation(
    state: AMLState
):

    aml_analysis = state[
        "aml_analysis"
    ]

    fraud_analysis = state[
        "fraud_analysis"
    ]

    context = state[
        "investigation_context"
    ]

    graph_metrics = context[
        "graph_metrics"
    ][0]

    suspicious_neighbors = len(
        context["suspicious_neighbors"]
    )

    cycles = len(
        context["cycles"]
    )

    final_report = f"""

    ===================================
    ENTERPRISE AML INVESTIGATION REPORT
    ===================================

    Account ID:
    {context["account_id"]}

    Final AML Score:
    {graph_metrics["final_aml_score"]:.6f}

    Suspicious Neighbor Count:
    {suspicious_neighbors}

    Detected Cycles:
    {cycles}

    -----------------------------------
    AML AGENT FINDINGS
    -----------------------------------

    {aml_analysis}

    -----------------------------------
    FRAUD AGENT FINDINGS
    -----------------------------------

    {fraud_analysis}

    -----------------------------------
    FINAL INVESTIGATION DECISION
    -----------------------------------

    Account demonstrates elevated
    suspicious graph behavior and
    requires compliance review.

    Recommended Action:
    Escalate to AML investigation team.

    """

    return {
        "final_report": final_report
    }
from langgraph.graph import StateGraph

graph_builder = StateGraph(
    AMLState
)

# --------------------------------------------------
# ADD NODES
# --------------------------------------------------

graph_builder.add_node(
    "retrieve_context",
    retrieve_context
)

graph_builder.add_node(
    "aml_agent",
    aml_agent
)

graph_builder.add_node(
    "fraud_agent",
    fraud_agent
)

graph_builder.add_node(
    "synthesize_investigation",
    synthesize_investigation
)

# --------------------------------------------------
# ENTRY POINT
# --------------------------------------------------

graph_builder.set_entry_point(
    "retrieve_context"
)

# --------------------------------------------------
# EDGES
# --------------------------------------------------

graph_builder.add_edge(
    "retrieve_context",
    "aml_agent"
)

graph_builder.add_edge(
    "retrieve_context",
    "fraud_agent"
)

graph_builder.add_edge(
    "aml_agent",
    "synthesize_investigation"
)

graph_builder.add_edge(
    "fraud_agent",
    "synthesize_investigation"
)

# --------------------------------------------------
# COMPILE
# --------------------------------------------------

graph = graph_builder.compile()

# --------------------------------------------------
# RUN
# --------------------------------------------------

result = graph.invoke({

    "account_id": 6192
})

print(result["final_report"])