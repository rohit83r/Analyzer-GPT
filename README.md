# 📊 Analyzer GPT – AI-Powered Digital Data Analyst

Analyzer GPT is an **AI-driven multi-agent system** that can analyze CSV datasets using natural language queries.
Just upload your data, ask a question, and let the AI generate Python code, run it safely in Docker, and return results (tables/plots).

---

## ✨ Features

✅ Upload CSV files and ask questions in plain English

✅ AI agent generates **Python + Pandas/Matplotlib code** automatically

✅ Code runs **securely inside Docker** using `amancevice/pandas` image

✅ Streamlit-based interactive UI

✅ Supports **charts, plots, and tabular insights**

✅ Extensible architecture (add SQL, Excel, JSON support easily)

---

## 🛠️ Tech Stack

* **LLM**: OpenAI (recommended for best results ⚡)
* **Agents**: [autogen-agentchat](https://github.com/microsoft/autogen) (Data Analyzer + Code Executor)
* **Code Execution**: Docker container (`amancevice/pandas`)
* **Frontend**: Streamlit
* **Backend**: Python (asyncio, autogen)

---

## 📂 Project Structure

```
analyzer-gpt/
│── agents/
│   ├── Data_analyzer_agent.py      # AI agent to analyze data & generate Python code
│   ├── Code_executor_agent.py      # Executes generated code safely
│
│── teams/
│   ├── analyzer_gpt.py             # Multi-agent team setup
│
│── config/
│   ├── constants.py                # Config (WORK_DIR, TIMEOUT, etc.)
│   ├── docker_util.py              # Docker start/stop helpers
│
│── models/
│   ├── openai_model_client.py      # OpenAI client for Data Analyzer
│
│── streamlit.py                          # Streamlit app entry
│── main.py                         # CLI runner example
│── requirements.txt
│── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/rohit83r/analyzer-gpt.git
cd analyzer-gpt
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start Docker

Make sure Docker is running on your system.

Analyzer GPT uses the lightweight **`amancevice/pandas`** image for Pandas + Python.

### 4️⃣ Run the Streamlit App

```bash
streamlit run streamlit.py
```

---

## 💻 Example

Upload `iris.csv` and ask:

> **“Can you give me a graph of types of flowers in my data?”**

✅ Data Analyzer generates Python code

✅ Code Executor runs it inside Docker

✅ Output: a clean bar chart of flower species 🎉

---

## 📷 Demo
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/510357e7-3406-4f25-a246-0d0147bcb744" />

<img width="1115" height="849" alt="Screenshot 2025-08-26 121006" src="https://github.com/user-attachments/assets/5d753529-aae8-4b94-a311-4f22699c599b" />

<img width="745" height="901" alt="Screenshot 2025-08-26 121032" src="https://github.com/user-attachments/assets/5a5c19e6-0958-4472-8510-f7da963e2fa1" />







---

## ⚠️ Disclaimer

Analyzer GPT uses AI models to generate Python code for data analysis.

For the **best results**, please use **OpenAI models** (GPT-4 / GPT-4.1).

Other models may work, but accuracy may vary.

---

## 🔮 Future Enhancements

* Support for Excel, JSON, and SQL databases
* Multi-turn contextual Q\&A
* Export insights as PDF/Markdown reports
* SaaS deployment for teams


