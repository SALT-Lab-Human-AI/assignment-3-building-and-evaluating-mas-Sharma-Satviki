## Tested Queries Documentation

This document describes the queries used during evaluation of the multi-agent research system. All queries originated from data/example_queries.json but were selectively tested based on runtime constraints, model latency, and timeout tuning.

Evaluation Configuration

Total Queries in Dataset: 10

Queries Tested: 5 (reduced due to timeout sensitivity when switching OpenAI models)

Evaluation Date: 2025-12-06

Evaluation Mode: Multi-agent pipeline + LLM-as-a-Judge evaluation

Models Used: gpt-4o-mini for agents, gpt-4o for judge

Search Backend: Tavily Web Search

Tested Queries
Query 1: Cognitive Load in Interface Design

Query: "How can interface designers reduce cognitive load for first-time users?"
Category: cognitive_load
Ground Truth Summary:
Effective strategies include progressive disclosure, reducing simultaneous choices, predictable interaction patterns, visual hierarchy, and clear onboarding flows.
Status: ✅ Tested
Expected Topics: mental effort, chunking, onboarding, progressive disclosure, novice users

Query 2: Trust Calibration in AI Systems

Query: "What factors influence trust calibration in AI decision-support systems?"
Category: trust_in_ai
Ground Truth Summary:
User trust depends on feedback transparency, explanation clarity, error communication, perceived competence, and opportunities for user correction or override.
Status: ✅ Tested
Expected Topics: overtrust, undertrust, transparency, reliability, user control

Query 3: Mobile Gesture Usability

Query: "How do gesture-based interactions affect usability compared to traditional tap interactions on mobile devices?"
Category: mobile_gestures
Ground Truth Summary:
Gestures increase expressiveness and reduce screen clutter but introduce discoverability challenges, higher learning curves, and inconsistent cross-app behavior.
Status: ✅ Tested
Expected Topics: discoverability, learnability, error rates, gesture mapping, user familiarity

Query 4: AI-Mediated Collaboration

Query: "What role does AI play in improving remote collaborative work?"
Category: collaboration_ai
Ground Truth Summary:
AI improves coordination through summarization, task extraction, intelligent recommendations, automated note-taking, and context-aware assistance during meetings.
Status: ✅ Tested
Expected Topics: productivity tools, meeting assistive AI, summarization, decision support

Query 5: Accessibility in Voice Interfaces

Query: "What accessibility challenges arise in voice-based interfaces?"
Category: voice_accessibility
Ground Truth Summary:
Challenges include speech recognition errors, dialect bias, background noise, limited error recovery, cognitive load from memory-based commands, and privacy concerns.
Status: ✅ Tested
Expected Topics: speech bias, noise issues, repair mechanisms, memory load, privacy

Additional Queries in Dataset (Not Tested)

These queries exist in data/example_queries.json but were not evaluated in this run due to prolonged response times and model switching:

Multimodal Learning: "How can multimodal interaction improve learning outcomes in educational apps?"

Emotion-Aware Interfaces: "What are the limitations of emotion detection in adaptive interfaces?"

Health Wearable Engagement: "Which factors drive long-term engagement with health wearables?"

AI-Driven Prototyping: "How is AI reshaping rapid UI/UX prototyping workflows?"

Cross-Platform Design Consistency: "What strategies ensure consistency across mobile, tablet, and desktop interfaces?"
