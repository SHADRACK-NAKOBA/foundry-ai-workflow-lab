# 6 · Draft replies with a Resolution Agent, then preview

[⬅ Conditions and routing](05-conditions-and-routing.md) · [Next: Run the workflow from code ➡](07-run-from-code.md)

## 6.1 Add the Resolution Agent (non-billing tickets)

1. Under the **Else** branch of the **second** If/Else (category *not* Billing), select **+**.
2. Under **Invoke**, select **Agent** → **Create new agent**.
3. Name: `Resolution-Agent` → **Create**. If asked for **Interaction mode**, choose **Text**.
4. Under **Details**, check a **model** is selected. Leave **Text format** as **Text** (this agent writes plain text).
5. **Instructions**: paste [`workflow-inputs/resolution-agent-instructions.txt`](../workflow-inputs/resolution-agent-instructions.txt):

   ```text
   You are a customer support resolution assistant for ContosoPay, a B2B payments and invoicing platform.

   Your task is to draft a clear, professional, and friendly support response based on the issue category and customer message.

   Guidelines:
   If the issue category is Technical:
   - Suggest 1-2 common troubleshooting steps at a high level.
   - Avoid asking for logs, credentials, or sensitive data.
   - Do not imply fault by the customer.

   If the issue category is General:
   - Provide a concise, helpful explanation or guidance.

   Keep the response under 5 sentences.

   Tone:
   - Professional, calm, and supportive
   - Clear and concise
   - No emojis

   Output:
   Return only the drafted response text.
   Do not include internal reasoning or analysis.
   ```

6. Select **Node settings**:
   - **Input message**: `Local.TriageOutputText` (the triage result carries both the issue and its category).
   - **Save agent output message as**: create a new variable `ResolutionOutputText`.
7. Select **Done**.

## 6.2 Save and preview

1. Select **Save**.
2. Select **Preview**.
3. In the chat box type:

   ```text
   Start processing support tickets.
   ```

4. Watch the nodes light up as each ticket goes through. Expected result:

   | Ticket | Category | What happens |
   |---|---|---|
   | API returns 403 when creating invoices | Technical | Resolution-Agent drafts troubleshooting steps |
   | Export all invoices as CSV? | General | Resolution-Agent explains how to export |
   | Charged twice for the same invoice | Billing | *"Escalate billing issue to human support team."* |

   Example reply for the first ticket:

   ```text
   Thank you for reaching out about the 403 error when creating invoices. This error typically
   indicates a permissions or access issue. Please ensure that your API key has the necessary
   permissions for invoice creation and that your request is being sent to the correct endpoint.
   ```

📸 **Screenshot** the finished canvas and the preview chat for your LinkedIn post.

> Got *"The '.' operator cannot be used on Unknown values"*? Go to [Troubleshooting](10-troubleshooting.md#unknown-values-error).
