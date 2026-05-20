from typing import TypedDict
import ollama
from langgraph.graph import StateGraph

class AMLState(TypedDict):

    account_id: int

    investigation_context: dict

    aml_analysis: str

    fraud_analysis: str

    final_report: str

from orchestration.symbolic_reasoning import (
    compute_symbolic_risk
)



from memory.vector_memory import (
    retrieve_similar_cases
)

from rag.graph_retrieval import (
    build_investigation_context
)

from rag.knowledge_rag import (
    retrieve_knowledge
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

# --------------------------------------------------
# HALLUCINATION / GROUNDEDNESS CHECK
# --------------------------------------------------

FORBIDDEN_TERMS = [

    "malware",
    "ransomware",
    "hacker",
    "cyberattack",
    "drugs",
    "counterfeit",
    "terrorism",
    "weapon"
]


def groundedness_check(
    llm_output
):

    hallucinations = []

    lower_output = llm_output.lower()

    for term in FORBIDDEN_TERMS:

        if term in lower_output:

            hallucinations.append(term)

    return hallucinations

# --------------------------------------------------
# AML AGENT
# --------------------------------------------------

from rag.knowledge_rag import (
    retrieve_knowledge
)

from memory.vector_memory import (
    retrieve_similar_cases
)
def aml_agent(
    state: AMLState
):

    # ------------------------------------------
    # RETRIEVE INVESTIGATION CONTEXT
    # ------------------------------------------

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

    # ------------------------------------------
    # SYMBOLIC AML REASONING
    # ------------------------------------------

    symbolic_findings = compute_symbolic_risk(

        graph_metrics,

        suspicious_neighbors,

        cycles
    )

    # ------------------------------------------
    # SYMBOLIC AML CLASSIFICATION
    # ------------------------------------------

    aml_score = graph_metrics[
        "final_aml_score"
    ]

    if aml_score > 0.005:

        risk_level = "HIGH"

    elif aml_score > 0.001:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    # ------------------------------------------
    # CONNECTIVITY ASSESSMENT
    # ------------------------------------------

    if suspicious_neighbors > 50:

        connectivity_risk = (
            "High suspicious connectivity"
        )

    elif suspicious_neighbors > 10:

        connectivity_risk = (
            "Moderate suspicious connectivity"
        )

    else:

        connectivity_risk = (
            "Low suspicious connectivity"
        )

    # ------------------------------------------
    # CYCLE ASSESSMENT
    # ------------------------------------------

    if cycles > 10:

        cycle_risk = (
            "Potential laundering cycles detected"
        )

    elif cycles > 0:

        cycle_risk = (
            "Limited laundering cycle exposure"
        )

    else:

        cycle_risk = (
            "No laundering cycles detected"
        )

    # ------------------------------------------
    # CENTRALITY ASSESSMENT
    # ------------------------------------------

    if (

        graph_metrics[
            "betweenness_centrality"
        ] > 0.5

    ):

        routing_risk = (
            "High intermediary routing behavior"
        )

    else:

        routing_risk = (
            "Limited intermediary routing exposure"
        )
    formatted_findings = "\n".join(

        f"- {finding}"

        for finding in symbolic_findings
    )

    # ------------------------------------------
    # LINKED SUSPICIOUS ACCOUNTS
    # ------------------------------------------

    linked_accounts = [

        f"{acc['ACCOUNT_ID']} "
        f"(AML Score: "
        f"{acc['final_aml_score']:.4f})"

        for acc in context[
            "suspicious_neighbors"
        ][:5]
    ]

    formatted_accounts = "\n".join(

        f"- {acc}"

        for acc in linked_accounts
    )

    # ------------------------------------------
    # BUILD INVESTIGATION SUMMARY
    # FOR VECTOR MEMORY RETRIEVAL
    # ------------------------------------------

    investigation_summary = f"""

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

    PageRank:
    {graph_metrics["pagerank"]:.6f}

    """

    # ------------------------------------------
    # KNOWLEDGE RAG
    # ------------------------------------------

    knowledge_context = retrieve_knowledge(

        "AML scoring framework and "
        "betweenness centrality"
    )

    # ------------------------------------------
    # VECTOR MEMORY RETRIEVAL
    # ------------------------------------------

    similar_cases = retrieve_similar_cases(

        investigation_summary,
        n_results=1
    )

    # ------------------------------------------
    # AML PROMPT
    # ------------------------------------------

    prompt = f"""

    Generate a concise AML investigation
    summary using the findings below.

    CURRENT ACCOUNT

    Account ID:
    {context["account_id"]}

    AML Risk Level:
    {risk_level}

    Connectivity Assessment:
    {connectivity_risk}

    Cycle Assessment:
    {cycle_risk}

    Routing Assessment:
    {routing_risk}

    Linked Suspicious Accounts:

    {formatted_accounts}

    Use a professional AML tone.

    Keep response under 150 words.

    """

    # ------------------------------------------
    # LLM GENERATION
    # ------------------------------------------

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

    # ------------------------------------------
    # GROUNDEDNESS CHECK
    # ------------------------------------------

    hallucinations = groundedness_check(
        analysis
    )

    if hallucinations:

        analysis += f"""

        ==========================================
        GROUNDING WARNING
        ==========================================

        Potential unsupported concepts detected:

        {hallucinations}

        """

    # ------------------------------------------
    # RETURN AML ANALYSIS
    # ------------------------------------------

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