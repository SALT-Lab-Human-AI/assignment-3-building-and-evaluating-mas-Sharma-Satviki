# Submission Checklist & Reproducibility Guide

This document explains **exactly what is included in the submission**, **where each artifact lives**, and **how to fully reproduce the system**, including running the UI, generating outputs, and running evaluation.

---

# ✅ 1. Repository Structure & File Locations

The repository follows the structure required by the assignment.  
Below is a clear description of what each folder contains and why.

## **src/** — Core System Code
Contains all implementation code for the multi-agent research system.

### **src/agents/**
Implements all four required agents:
- `planner_agent.py` — Converts user query into structured research plan  
- `researcher_agent.py` — Performs Tavily web search and evidence extraction  
- `writer_agent.py` — Synthesizes final written response  
- `critic_agent.py` — Evaluates response and signals approval or revision  

Also includes:
- `base_agent.py` — Shared logic and interface definitions

### **src/guardrails/**
Implements the complete safety pipeline:
- `input_guardrail.py` — Validates query relevance, detects harmful or injected input  
- `output_guardrail.py` — Validates outgoing text for PII, hallucinated URLs, harm  
- `safety_manager.py` — Central controller for logging & safety event routing  

### **src/tools/**
Implements tool integrations:
- `web_search.py` — Tavily search API wrapper  
- `paper_search.py` — Included for compatibility (unused in your system)  
- `citation_tool.py` — Extracts and formats citations for UI display  

### **src/evaluation/**
Implements LLM-as-Judge evaluation:
- `judge.py` — Model-based scoring rubric for all criteria  
- `evaluator.py` — Runs evaluation over the test query set  

### **src/ui/**
Contains the complete Streamlit interface:
- `streamlit_app.py` — Main interactive UI with agent traces, safety logs, exports  
- `cli.py` — Optional command-line interface for query processing  

### **src/autogen_orchestrator.py**
The orchestration engine coordinating Planner → Researcher → Writer → Critic.  
Handles:
- role routing  
- termination token detection  
- citation extraction  
- metadata tracking  
- safety checks  
- error catching and timeout management  

---

# 📁 2. Additional Repository Contents

## **config.yaml**
Defines:
- model settings (OpenAI)  
- safety configuration  
- maximum rounds  
- agent prompts  
- evaluation preferences  

## **.env.example**
Template showing required environment variables:
OPENAI_API_KEY=
TAVILY_API_KEY=


## **data/example_queries.json**
Contains 6 queries used during evaluation.

## **outputs/**
Auto-generated folder containing:
- conversation JSON files  
- markdown responses  
- evaluation summaries  
- evaluation judge reports  

(These regenerate automatically when running evaluation or exporting from the UI.)

---

# 🚀 3. How to Reproduce the System Locally (Step-by-Step)

## **Step 1 — Install Dependencies**
```bash
pip install -r requirements.txt
Step 2 — Set Environment Variables

Create .env:

cp .env.example .env


Fill in:

OPENAI_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here

Step 3 — Run the Streamlit Web Interface
streamlit run src/ui/streamlit_app.py


This launches:

Query input field

Real-time agent processing

Agent trace visualizer

Safety event visualizer

Export buttons (JSON, Markdown)

Example queries sidebar

Step 4 — Run CLI Version (Optional)
python main.py --mode cli

Step 5 — Run Evaluation Mode

Runs 6 queries through the full agent pipeline and evaluates them.

python main.py --mode evaluate


This will:

Process all example queries

Score them with LLM-as-Judge

Save results to outputs/:

evaluation_*.json

evaluation_summary_*.txt

evaluation_report_*.md
