# 📈 Agentic Financial Sentinel: Stock Analysis & Reasoning Workflow

[![Framework: LangGraph](https://img.shields.io/badge/Framework-LangGraph-blue)](https://python.langchain.com/langgraph/)
[![Engine: Gemini 1.5 Pro](https://img.shields.io/badge/Engine-Gemini%201.5%20Pro-orange)](https://deepmind.google/technologies/gemini/)
[![Data: yfinance](https://img.shields.io/badge/Data-yfinance-green)](https://pypi.org/project/yfinance/)

## 📖 Project Overview
The **Agentic Financial Sentinel** is an enterprise-grade automated intelligence layer designed to bridge the gap between **quantitative market data** and **qualitative news sentiment**. 

In high-stakes trading environments, a stock dropping 200 basis points (bps) is a data point; understanding *why* it dropped within seconds is a competitive advantage. This system autonomously monitors a watchlist, detects significant movements, and performs real-time root-cause analysis by correlating news data with market fluctuations.

---

## 🧠 Core Philosophy: Why Agentic?
Unlike traditional linear scripts, this system utilizes a **Stateful Graph** architecture (powered by LangGraph) to mimic the workflow of a financial analyst:

* **Contextual Awareness:** The agent understands that a -300 bps move during an earnings window requires different search parameters than a move during a macro-economic shift.
* **Self-Correction:** If initial news queries return "low-signal" results, the agent can autonomously pivot its search to industry peers or broader market indices to find a correlation.
* **Decoupled Logic:** Quantitative calculation (Math) is separated from Qualitative reasoning (LLM), ensuring high reliability and auditability.

---

## 🛠 Technical Deep-Dive

### 1. The Multi-Step Intelligence Pipeline
1.  **Ingestion & Quant-Analysis:**
    Connects to real-time equity feeds via `yfinance`. It calculates the variance from the previous session's Close Price, normalizing the move into **Basis Points ($1\text{ bps} = 0.01\%$)**.
2.  **Autonomous Information Retrieval (RAG):**
    Triggered only when the bps threshold is breached. The agent utilizes **Tavily AI** to perform "Time-Bound Search," restricting results to the most recent 6–12 hour window.
3.  **Cross-Correlation Reasoning:**
    The LLM (Gemini 1.5 Pro) receives the quantitative delta and the retrieved news snippets to determine if the move is "Justified" (fundamental) or "Noise" (technical/speculative).

### 2. Enterprise State Management
Built on **LangGraph**, the system supports:
* **Checkpointing:** Analysis state is saved at every node. If a network error occurs during news retrieval, the system resumes without re-running the expensive stock scan.
* **Human-in-the-Loop:** Optional hooks to allow a human analyst to approve or refine the search query before the final synthesis.

---

## 📂 Project Structure

stock_agent/
├── .env                # API Keys (OpenAI/Gemini, NewsAPI, Tavily)
├── .gitignore
├── README.md
├── requirements.txt
├── main.py             # Entry point to run the graph
├── src/
│   ├── __init__.py
│   ├── graph/          # LangGraph orchestration
│   │   ├── __init__.py
│   │   ├── state.py    # TypedDict schema for AgentState
│   │   ├── nodes.py    # Function logic for each node
│   │   └── edges.py    # Conditional routing logic
│   ├── tools/          # External integrations
│   │   ├── __init__.py
│   │   ├── finance.py  # yfinance / Bloomberg / AlphaVantage wrappers
│   │   └── news.py     # Tavily / NewsAPI / Serper wrappers
│   ├── agents/         # LLM prompt templates and configurations
│   │   ├── __init__.py
│   │   └── prompts.py
│   └── utils/          # Logging, math (bps calculations), and formatting
│       └── logger.py
└── tests/              # Unit tests for nodes and tools
    └── test_nodes.py