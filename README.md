# Multi-Agent Research System for HCI

## Overview

This project implements a multi-agent research assistant designed to help users explore questions in Human–Computer Interaction (HCI). The system combines coordinated LLM-driven agents, automated evidence gathering through Tavily search, safety guardrails, and an evaluation framework based on LLM-as-a-Judge. Users interact with the system through a Streamlit web interface that displays responses, citations, agent traces, and safety diagnostics.

The system uses **OpenAI models** for all agent reasoning and **Tavily Search API** for external information retrieval. All research, synthesis, critique, and safety decisions are performed through an integrated orchestration layer that manages the full workflow.

---

## System Architecture

### Research Workflow

The system processes queries through four coordinated agents:

1. **Planner** – Interprets the query, identifies subtopics, and outlines a research plan.  
2. **Researcher** – Executes targeted searches using Tavily and prepares structured findings.  
3. **Writer** – Synthesizes findings into a coherent, citation-supported response.  
4. **Critic** – Reviews the draft for clarity, completeness, and potential inconsistencies.

This ordered flow guarantees that each query goes through planning → evidence collection → synthesis → quality review before being returned to the user.

The `AutoGenOrchestrator` manages these roles, routes messages, enforces handoff tokens, and maintains conversation history.

---

## Streamlit Web Interface

### Main Features

The Streamlit UI provides an intuitive environment for interacting with the system:

- **Query Input Panel** – Accepts HCI-related research questions.  
- **Real-Time Status Updates** – Displays progress indicators during agent processing.  
- **Agent Traces** – Optional visualization of agent messages showing how the plan, research, writing, and critique unfold.  
- **Safety Events** – Real-time logs showing input/output safety evaluations.  
- **Citation Extraction** – Automatic detection and formatting of URLs and APA-style references.  
- **Quality Scoring** – Simple scoring based on sources used, conversation depth, and critic involvement.  
- **Export Utilities** – Download conversation JSON or Markdown formatted responses.

Example UI features implemented in your code include:

- Agent traces grouped by role  
- Safety log toggles  
- Query history sidebar  
- Preview + expand for long agent messages  

---

## Safety Guardrails

Safety is handled through a custom LLM-mediated system including:

### Input Guardrail  
- Detects toxic or unsafe language  
- Filters irrelevant or off-topic queries  
- Prevents prompt injection patterns  
- Enforces basic length and formatting requirements  

### Output Guardrail  
- Identifies unsafe or inappropriate model outputs  
- Detects the presence of PII via regex patterns  
- Ensures final responses remain appropriate for academic contexts  

Safety events are recorded and optionally shown in the Streamlit UI.

---

## Evaluation Framework

The project includes an evaluation pipeline based on LLM-as-a-Judge:

- **Multiple perspectives**: Academic and user-oriented evaluation styles  
- **Five scoring criteria**: relevance, evidence quality, factual accuracy, safety compliance, clarity  
- **Automatic aggregation**: Weighted scores combined into an overall evaluation score  

Evaluation results are saved into the `outputs/` directory.

---

## Running the System

### Run the Web Interface
```bash
streamlit run src/ui/streamlit_app.py
