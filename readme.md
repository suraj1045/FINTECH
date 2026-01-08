# 🏦 FinTech AI/ML Project Portfolio

Welcome to my specialized repository featuring AI and Machine Learning applications within the financial technology sector. This repository serves as a centralized hub for my work in **Agentic Workflows**, **Market Analysis**, and **Financial Automation**.

---

## 🛠 Global Tech Stack
Across these projects, I utilize a high-performance stack designed to handle real-time data and complex AI reasoning:

### **Backend (Intelligence Layer)**
* **Language:** Python
* **API Framework:** FastAPI (served via Uvicorn)
* **AI Orchestration:** LangGraph, LangChain
* **LLMs:** Google GenAI (Gemini)
* **Financial Data & Tools:** `yfinance` (Stock Data), Tavily (Real-time Web Search)
* **Testing:** Pytest

### **Frontend (User Interface)**
* **Framework:** React 19
* **Build Tool:** Vite
* **Styling:** Tailwind CSS v4
* **Iconography:** Lucide React

---

## 📖 Project Documentation Standard
To maintain clarity, every project within this repository is documented using the following framework:

1. **Overview:** The financial problem the project addresses.
2. **Tech Stack:** Specific libraries or models unique to that project.
3. **Project Structure:** A breakdown of how the logic is separated between the AI backend and the UI.
4. **Key Features:** Core functionalities (e.g., Sentiment analysis, Technical indicators).
5. **Installation:** Step-by-step guide to get the project running locally.

---

## 🚀 Featured Project: Stock Agent
The **Stock Agent** is an autonomous financial research assistant that leverages Agentic AI to provide deep insights into market equity.

### **Project Architecture**
The project is structured with a clean separation of concerns:
* **Root Directory:** Contains the Python/FastAPI backend and AI agent logic.
* **`front_end/` Directory:** A dedicated React application for the user dashboard.

### **Core Functionalities**
* **Agentic Reasoning:** Uses **LangGraph** to create stateful, multi-step research loops.
* **Real-time Analysis:** Combines historical stock data from `yfinance` with live news via **Tavily Search**.
* **Modern UI:** A responsive, high-performance interface built with **React 19** and **Tailwind v4**.

---

## ⚙️ Quick Start Guide

### **1. Backend & AI Setup**
Navigate to the project root:
```bash
# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI server
# (Assuming server.py contains the FastAPI 'app' instance)
uvicorn server:app --reload