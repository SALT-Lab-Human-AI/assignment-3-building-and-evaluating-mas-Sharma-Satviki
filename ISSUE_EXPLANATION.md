# Issue Explanation: Model Switching and Timeout Instability

## Description of the Issue

During development, the system frequently stalled during the Researcher and Writer stages. This occurred primarily when switching between different OpenAI models, each with its own latency and token throughput. Because the multi-agent workflow chains several LLM calls sequentially, any slowdown cascaded through the entire system.

## Symptoms

- Planner executed normally but Researcher calls delayed for several seconds.  
- Critic responses occasionally timed out mid-evaluation.  
- Streamlit displayed “processing…” indefinitely despite the agent chain having frozen.  
- Evaluation mode aborted early due to orchestrator timeout.

## Root Cause

The orchestrator used a fixed timeout value that did not account for slower models. Switching between faster models (e.g., GPT-4o-mini) and heavier models (e.g., GPT-4o) resulted in unpredictable delays. The asynchronous handler also accumulated latency when several Tavily requests occurred in close succession.

## Resolution

- Increased timeout values in both orchestrator and evaluation scripts.  
- Reduced max agent rounds from 5 → 2 for evaluation.  
- Standardized all agents to a single OpenAI model to eliminate variability.  
- Reduced max tokens to shorten LLM inference time.

## Outcome

After stabilization, all agents completed within expected durations, and evaluation passed consistently without freezing.
