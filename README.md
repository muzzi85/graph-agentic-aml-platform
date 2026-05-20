Business Problem

Modern financial institutions process massive volumes of transactional activity across:

retail banking
cross-border transfers
online banking payments
shell account activity
layered transaction routing
interconnected customer networks

Traditional AML investigation systems often rely on:

siloed transaction monitoring
delayed batch analysis
manual compliance reviews
static rules engines
disconnected investigation tooling

This creates major challenges:

delayed laundering detection
poor graph visibility
limited explainability
high false positives
weak topology intelligence
slow compliance escalation
fragmented investigation workflows

This platform solves the problem through an AI-assisted GraphRAG investigation architecture capable of:

analyzing suspicious transaction topology
detecting laundering connectivity patterns
identifying suspicious graph exposure
retrieving historical investigation context
generating explainable AML investigation reports
reducing hallucinations using symbolic reasoning
supporting enterprise-style compliance workflows

Enterprise-style GraphRAG AML investigation platform using:

LangGraph orchestration
Graph analytics
Symbolic reasoning
Knowledge RAG
Vector memory
Local LLM inference
DeepEval evaluation
Groundedness validation
Explainable AML investigation workflows
Overview

This project demonstrates how modern AI investigation systems can combine:

graph intelligence
symbolic AI
retrieval-augmented generation (RAG)
vector memory
orchestration frameworks
local LLMs

into a production-style AML investigation architecture.

The platform focuses on:

suspicious transaction topology
graph explainability
laundering pattern detection
connected suspicious accounts
AI-assisted compliance investigation

# Graph Agentic AML Platform

```text
                    ┌──────────────────────┐
                    │ Transaction Graph DB │
                    └──────────┬───────────┘
                               │
                               ▼
                 ┌─────────────────────────┐
                 │ Graph Analytics Engine  │
                 │ - centrality metrics    │
                 │ - suspicious neighbors  │
                 │ - cycle detection       │
                 └──────────┬──────────────┘
                            │
                            ▼
                ┌──────────────────────────┐
                │ Symbolic AML Reasoning   │
                │ - risk classification    │
                │ - topology assessment    │
                │ - escalation logic       │
                └──────────┬───────────────┘
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
┌───────────────────┐          ┌────────────────────┐
│ Knowledge RAG     │          │ Vector Memory RAG │
│ AML semantics     │          │ historical cases  │
└─────────┬─────────┘          └─────────┬──────────┘
          │                               │
          └──────────────┬────────────────┘
                         ▼
             ┌──────────────────────────┐
             │ LangGraph Orchestration  │
             │ - AML agent              │
             │ - Fraud agent            │
             │ - Investigation synthesis│
             └──────────┬───────────────┘
                        │
                        ▼
             ┌──────────────────────────┐
             │ Local LLM Summarization  │
             │ TinyLlama via Ollama     │
             └──────────┬───────────────┘
                        │
                        ▼
             ┌──────────────────────────┐
             │ Groundedness Validation  │
             │ + DeepEval Evaluation    │
             └──────────┬───────────────┘
                        │
                        ▼
          ┌────────────────────────────────┐
          │ Enterprise AML Investigation   │
          │ Report + Graph Explainability  │
          └────────────────────────────────┘
```

---

# Business Problem

Modern financial institutions process massive volumes of transactional activity across:

- retail banking
- cross-border transfers
- online banking payments
- shell account activity
- layered transaction routing
- interconnected customer networks

Traditional AML investigation systems often rely on:

- siloed transaction monitoring
- delayed batch analysis
- manual compliance reviews
- static rules engines
- disconnected investigation tooling

This creates major challenges:

- delayed laundering detection
- poor graph visibility
- limited explainability
- high false positives
- weak topology intelligence
- slow compliance escalation
- fragmented investigation workflows

This platform solves the problem through an AI-assisted GraphRAG investigation architecture capable of:

- analyzing suspicious transaction topology
- detecting laundering connectivity patterns
- identifying suspicious graph exposure
- retrieving historical investigation context
- generating explainable AML investigation reports
- reducing hallucinations using symbolic reasoning
- supporting enterprise-style compliance workflows

---

Enterprise-style GraphRAG AML investigation platform using:

- LangGraph orchestration
- Graph analytics
- Symbolic reasoning
- Knowledge RAG
- Vector memory
- Local LLM inference
- DeepEval evaluation
- Groundedness validation
- Explainable AML investigation workflows

---

# Overview

This project demonstrates how modern AI investigation systems can combine:

- graph intelligence
- symbolic AI
- retrieval-augmented generation (RAG)
- vector memory
- orchestration frameworks
- local LLMs

into a production-style AML investigation architecture.

The platform focuses on:

- suspicious transaction topology
- graph explainability
- laundering pattern detection
- connected suspicious accounts
- AI-assisted compliance investigation
<img width="1536" height="1024" alt="ChatGPT Image May 21, 2026, 12_20_46 AM" src="https://github.com/user-attachments/assets/0c0a515c-5a48-4496-942b-f8a289e0548e" />

---

# Enterprise Architecture

```text
Transaction Graph
        ↓
Graph Analytics Engine
        ↓
GraphRAG Retrieval
        ↓
Symbolic AML Reasoning
        ↓
Knowledge RAG
        ↓
Vector Memory Retrieval
        ↓
LangGraph Multi-Agent Orchestration
        ↓
LLM Summarization
        ↓
Groundedness Validation
        ↓
Final AML Investigation Report
```

---

# Core Features

## 1. GraphRAG Investigation Engine

The platform retrieves graph-based AML evidence including:

- suspicious neighboring accounts
- graph centrality metrics
- laundering cycle detection
- graph topology indicators
- suspicious transaction exposure

Example graph metrics:

- Degree Centrality
- Betweenness Centrality
- PageRank
- Clustering Coefficient

---

## 2. LangGraph Multi-Agent Orchestration

The platform uses LangGraph to orchestrate:

- context retrieval
- AML investigation agent
- fraud investigation agent
- investigation synthesis

Workflow:

```text
retrieve_context
       ↓
 ┌───────────────┐
 ↓               ↓
aml_agent    fraud_agent
       ↓        ↓
 synthesize_investigation
```

---

## 3. Symbolic AML Reasoning Layer

Instead of relying entirely on the LLM for reasoning, the platform computes:

- AML risk classifications
- suspicious connectivity assessments
- laundering cycle exposure
- intermediary routing risk
- escalation recommendations

using deterministic Python logic.

Example:

```python
if suspicious_neighbors > 50:

    connectivity_risk = (
        "High suspicious connectivity"
    )
```

This improves:

- explainability
- governance
- determinism
- hallucination reduction

---

# Graph Explainability Layer

The platform explains:

- why an account appears suspicious
- which linked accounts increase risk
- suspicious graph topology indicators
- fan-in / fan-out exposure
- intermediary routing behavior
- laundering cycle evidence

Example investigation output:

```text
Linked Suspicious Accounts:
- 9975 (AML Score: 0.0045)
- 9999 (AML Score: 0.0140)
- 9986 (AML Score: 0.0077)

Topology Indicators:
- elevated suspicious connectivity
- abnormal fan-out exposure
- intermediary routing behavior
```

---

# Subgraph Visualization Layer

The project is designed to support suspicious subgraph visualization.

Future capabilities include:

- laundering ring visualization
- suspicious transaction routing paths
- fan-in / fan-out diagrams
- intermediary transaction networks
- suspicious account clusters

Suggested libraries:

- networkx
- pyvis
- plotly
- graphistry

Example topology:

```text
6192 → 9975 → 9999 → 9986
```

This enables:

- explainable AI investigations
- analyst-facing graph intelligence
- compliance review support

---

# Knowledge RAG Layer

The system includes a semantic AML knowledge base.

Knowledge examples:

- AML scoring interpretation
- graph metric interpretation
- laundering topology semantics
- escalation guidance

Example:

```text
High betweenness centrality may indicate
intermediary laundering behavior.
```

Knowledge retrieval uses:

- ChromaDB
- semantic embeddings
- vector similarity search

---

# Vector Memory Layer

Historical investigations are stored as:

- semantic behavioral patterns
- topology summaries
- escalation outcomes

The memory layer helps the platform:

- compare similar investigations
- reuse prior investigation knowledge
- support investigation consistency

Example memory:

```text
Previous investigations involving
abnormal intermediary routing behavior
required AML escalation.
```

---

# DeepEval Evaluation Layer

The platform integrates DeepEval for:

- hallucination evaluation
- faithfulness scoring
- contextual precision
- contextual recall
- answer relevancy

This enables:

- AI governance
- investigation quality validation
- groundedness measurement

---

# Groundedness Validation Layer

A lightweight hallucination detection layer prevents unsupported AML narratives.

Forbidden concepts include:

- malware
- ransomware
- cyberattacks
- terrorism
- weapons

This reduces:

- domain drift
- unsupported narratives
- cross-domain hallucinations

---

# Local LLM Integration

The platform uses local Ollama-hosted models.

Example:

```python
response = ollama.chat(

    model="tinyllama",

    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
```

The project demonstrates how small local LLMs can be enhanced using:

- symbolic reasoning
- graph intelligence
- constrained prompting
- retrieval grounding

---

# Example Investigation Output

```text
ENTERPRISE AML INVESTIGATION REPORT

Account ID:
6192

AML Risk Level:
MEDIUM

Connectivity Assessment:
High suspicious connectivity

Routing Assessment:
Limited intermediary routing exposure

Linked Suspicious Accounts:
- 9975
- 9999
- 9986

Recommended Action:
Escalate to AML investigation team.
```

---

# Installation Guide

## 1. Clone Repository

```bash
git clone <your-repository-url>
cd graph-agentic-aml-platform
```

---

## 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

Activate environment:

### Linux / WSL

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Core packages:

```bash
pip install langgraph langchain networkx pandas chromadb ollama deepeval
```

---

## 4. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Then pull local model:

```bash
ollama pull tinyllama
```

Optional larger models:

```bash
ollama pull mistral
ollama pull llama3
```

---

## 5. Start Ollama

```bash
ollama serve
```

Default endpoint:

```text
http://localhost:11434
```

---

# Project Structure

```text
graph-agentic-aml-platform/
│
├── orchestration/
├── graph/
├── rag/
├── memory/
├── validation/
├── data/
└── requirements.txt
```

---

# Major Development Steps

## Step 1 — Build Transaction Graph

Convert banking transactions into graph structures.

Example:

```python
G.add_edge(sender, receiver)
```

---

## Step 2 — Generate Graph Features

Compute graph intelligence metrics.

Example:

```python
nx.degree_centrality(G)
nx.betweenness_centrality(G)
```

Features include:

- suspicious neighbors
- cycle detection
- graph topology indicators
- fan-in / fan-out exposure

---

## Step 3 — Build Symbolic AML Engine

Create deterministic AML reasoning logic.

```python
if suspicious_neighbors > 50:

    connectivity_risk = (
        "High suspicious connectivity"
    )
```

---

## Step 4 — Add Knowledge RAG

Retrieve semantic AML knowledge using ChromaDB.

```python
collection.query(
    query_texts=[
        "betweenness centrality"
    ]
)
```

---

## Step 5 — Add Vector Memory Layer

Store historical investigation patterns.

```python
memory_collection.add(
    documents=[summary]
)
```

---

## Step 6 — Build LangGraph Workflow

Workflow:

```text
retrieve_context
       ↓
aml_agent
       ↓
fraud_agent
       ↓
synthesize_investigation
```

---

## Step 7 — Add Local LLM Summarization

```python
response = ollama.chat(
    model="tinyllama",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)
```

---

## Step 8 — Add Groundedness Validation

```python
hallucinations = groundedness_check(
    analysis
)
```

---

## Step 9 — Add DeepEval Evaluation

Run evaluation:

```bash
python -m orchestration.evaluation.deepeval_test
```

---

# Running The Platform

## Run AML Investigation Workflow

```bash
python -m orchestration.aml_orchestrator
```

## Run DeepEval Testing

```bash
python -m orchestration.evaluation.deepeval_test
```

## Run Knowledge RAG Retrieval

```bash
python -m rag.knowledge_rag
```

## Run Vector Memory Retrieval

```bash
python -m memory.vector_memory
```

---

# Technologies Used

- Python
- LangGraph
- Ollama
- TinyLlama
- ChromaDB
- NetworkX
- DeepEval
- GraphRAG

---

# Future Improvements

## Planned Enhancements

- temporal graph analysis
- suspicious transaction path tracing
- adaptive AML threshold calibration
- human-in-the-loop review workflows
- graph visualization dashboards
- sanctions screening integration
- analyst feedback loops
- autonomous investigation agents

---

# Key AI Engineering Concepts Demonstrated

This project demonstrates:

- GraphRAG architectures
- multi-agent orchestration
- neuro-symbolic AI
- retrieval-augmented generation
- vector memory systems
- explainable AI
- groundedness validation
- enterprise AML reasoning workflows

---

# Conclusion

This repository demonstrates how enterprise AML investigation systems can combine:

- graph analytics
- symbolic reasoning
- retrieval systems
- orchestration frameworks
- local LLMs

to create explainable, AI-assisted financial crime investigation platforms.

The project evolves beyond a simple chatbot into:

```text
AI-powered AML Investigation Platform
```

with:

- explainable graph intelligence
- deterministic AML reasoning
- retrieval-enhanced investigation workflows
- grounded AI reporting
- enterprise-style orchestration

