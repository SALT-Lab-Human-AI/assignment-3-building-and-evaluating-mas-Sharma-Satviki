# Limitations Observed During Evaluation

## Evidence Depth

Since evidence came solely from Tavily search, several answers lacked research-grade citations. Blog articles and UX summaries were common sources, reducing the evidence quality score.

## Limited Rounds

To prevent timeouts, the system ran with a reduced number of agent rounds. As a result, revision cycles were shallow, and the Critic did not always prompt improvements.

## Model Token Restrictions

Lower token budgets were imposed due to performance concerns. This occasionally resulted in truncated explanations, especially for multi-component HCI concepts.

## UI Constraints

The Streamlit interface is optimized for fast prototyping and does not display the full conversational context, which limited transparency during debugging.
