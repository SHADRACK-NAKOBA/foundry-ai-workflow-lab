# 11 · Interview questions

[⬅ Troubleshooting](10-troubleshooting.md) · [Back to README](../README.md)

**1. Why use a workflow instead of one big agent prompt?**
A workflow separates *reasoning* (agents) from *control flow* (loops, conditions). Routing becomes explicit, testable and auditable, and each agent stays small and focused.

**2. Why JSON Schema output for the Triage Agent?**
Later nodes read `category` and `confidence` as fields. Strict schema output guarantees those fields exist with the right types, so there's no fragile text parsing and no "Unknown values" failures.

**3. Why escalate billing tickets instead of auto-replying?**
Money-related errors carry financial and trust risk. A human-in-the-loop for high-impact categories is a standard responsible-AI control.

**4. What does the 0.6 confidence threshold do, and how would you choose it in production?**
It stops low-certainty classifications from getting automatic replies. In production you'd tune it on labelled historical tickets, trading automation rate against misroute rate, and monitor it over time.

**5. How does the Python app call the workflow?**
`AIProjectClient` connects to the project endpoint with `DefaultAzureCredential`, gets an OpenAI-compatible client, creates a conversation, and calls `responses.create` with an `agent_reference` to the workflow name, streaming events until `response.completed`.

**6. Why `DefaultAzureCredential` and not an API key?**
It uses Microsoft Entra ID: your `az login` locally, a managed identity in Azure. No secrets in code or config, and access is controlled with Azure RBAC.

**7. How would you take this to production?**
Read tickets from a real queue or helpdesk API instead of a fixed array; run the client in Azure Functions or Container Apps with a managed identity; add evaluations for classification accuracy and reply quality; log runs and monitor latency, cost and escalation rate; version the workflow and agents.

**8. What would you test?**
A labelled set of tickets per category (including edge cases like "download my invoice" vs "charged twice"), low-confidence cases, prompt-injection attempts in ticket text, and that billing tickets never receive an AI-drafted reply.

### 60-second pitch

> "I built a customer-support triage workflow in Microsoft Foundry. A Triage Agent classifies each ticket into Billing, Technical or General with a confidence score, returned as strict JSON. Deterministic conditions then route it: low-confidence tickets ask for more details, billing issues are escalated to a human, and a Resolution Agent drafts replies for the rest. I then invoked the same workflow from Python with the Azure AI Projects SDK and Entra ID authentication, so it can plug into a real helpdesk. The key design idea: let the model classify, but let rules decide."
