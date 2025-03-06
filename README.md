
# 📊 Multi-Agent Financial Research System

This project implements a **multi-agent AI system** using `phidata`, focusing on financial research and real-time data gathering. It consists of individual agents, a team-based agent system, and a playground UI for exploration.

---

## 📂 Project Overview

### 1️⃣ Simple Groq Agent
File: `1_simple_groq_agent.py`  
- A basic agent using **Groq (Llama 3)**.  
- Prompts it directly to generate answers.  
- Example Task: Write about the Indian stock market.

---

### 2️⃣ Finance Agent
File: `2_finance_agent.py`  
- Agent specialized for financial data retrieval.  
- Uses `YFinanceTools` to get stock prices, analyst recommendations, and fundamentals.  
- Also uses a **custom tool** (`get_company_symbol()`) to map company names to ticker symbols.

---

### 3️⃣ Team of Agents
File: `3_agent_teams.py`  
- Combines **Web Agent** (DuckDuckGo search) and **Finance Agent** (financial data).  
- They work together to gather data and draft reports.  
- Example Task: Summarize NVDA’s latest news and analyst recommendations.

---

### 4️⃣ Playground UI
File: `playground.py`  
- Provides a **web-based playground UI** to interact with agents.
- Uses **GPT-4o** (so this will only work if a valid OpenAI key is provided).
- Agents store their history in **SQLite (`agents.db`)** for persistence.

---

## 🛠️ Requirements
Create `requirements.txt` with:
```
phidata
dotenv
```

Install with:
```bash
pip install -r requirements.txt
```

---

## 📥 Environment Variables
All files load their environment from `.env`. Example:

**.env**
```
GROQ_API_KEY=your-groq-api-key
OPENAI_API_KEY=your-openai-api-key  # Needed only for playground.py
TAVILY_API_KEY=your-tavily-api-key  # Optional if adding web search agents
```

---

## ▶️ How to Run

**1_simple_groq_agent.py**
```bash
python 1_simple_groq_agent.py
```

**2_finance_agent.py**
```bash
python 2_finance_agent.py
```

**3_agent_teams.py**
```bash
python 3_agent_teams.py
```

**playground.py** (Only works if you have a valid OpenAI API Key)
```bash
python playground.py
```

---

## ⚠️ Important
- `playground.py` requires GPT-4o, so it needs a **working OpenAI API key**.
- If using `secret_key.py`, remember this file should **NOT** be pushed to GitHub if it contains real keys.

---

## 💡 Future Improvements
- Replace GPT-4o with **Groq** or **Gemini** in `playground.py` (so it’s fully free to run).
- Add more tools for web scraping, PDF reading, or financial analysis.
- Improve `Agent.team` by adding a **Summary Agent** to refine the final response.
