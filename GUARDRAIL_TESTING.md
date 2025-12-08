# Guardrail Testing Results

## Input Guardrail Testing

Several crafted test cases were submitted to verify that the input guardrail correctly distinguishes safe HCI research queries from unsafe or irrelevant input.

### Blocked Cases (as expected)
- Queries with explicit harmful instructions  
- Attempts to override system prompts using quotation-breaking sequences  
- Requests unrelated to HCI, such as tax advice or unauthorized account recovery  
- Long repetitive prompts designed to overwhelm the model  

### Passed Cases
- All valid HCI-focused research questions  
- Queries comparing UX methodologies  
- AR usability and accessibility design questions  

The input guardrail occasionally issued “soft warnings” for borderline queries but did not block them.

## Output Guardrail Testing

### Detected Violations
- Instances where Tavily returned URLs containing email contact information  
- One case where the Writer hallucinated a fake domain name  
- A safety violation triggered by an unfiltered profanity present in a scraped snippet  

### Safe Responses
Most Writer outputs passed safety checks immediately. The Critic’s role indirectly reduced safety issues by removing unnecessary examples containing sensitive information.

## Overall Reliability

The safety system behaved predictably, blocking genuinely unsafe content while permitting all academically-appropriate HCI queries.
