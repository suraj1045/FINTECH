stock-agent-service/
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