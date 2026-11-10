# 4 · Classify each ticket with a Triage Agent

[⬅ Build the workflow](03-build-the-workflow.md) · [Next: Conditions and routing ➡](05-conditions-and-routing.md)

## 4.1 Add the agent node

1. Select the **+** icon **inside** the *For each* node.
2. Under **Invoke**, select **Agent**.
3. Under **Select an agent**, select **Create new agent**.
4. Name: `Triage-Agent` → **Create**. If asked for **Interaction mode**, choose **Text**.

## 4.2 Force JSON output (the step that prevents most errors)

1. Under **Details**, check a **model** is selected (pick your deployment if the box is empty).
2. Select the **Parameters** button next to the model name.
3. Next to **Text format**, select **JSON Schema**.
4. In **Add response format**, paste [`workflow-inputs/triage-response-format.json`](../workflow-inputs/triage-response-format.json) and select **Save**:

   ```json
   {
     "name": "category_response",
     "schema": {
       "type": "object",
       "properties": {
         "customer_issue": { "type": "string" },
         "category": { "type": "string" },
         "confidence": { "type": "number" }
       },
       "additionalProperties": false,
       "required": ["customer_issue", "category", "confidence"]
     },
     "strict": true
   }
   ```

   ⚠️ Confirm **Text format** now shows **JSON Schema**. If it still says *Text*, the next conditions fail with *"The '.' operator cannot be used on Unknown values"*.

## 4.3 Instructions

In **Instructions**, paste [`workflow-inputs/triage-agent-instructions.txt`](../workflow-inputs/triage-agent-instructions.txt):

```text
Classify the user's problem description into exactly ONE category from the list below. Provide a confidence score from 0 to 1.

Billing
- Charges, refunds, duplicate payments
- Missing or incorrect payouts
- Subscription pricing or invoices being charged

Technical
- API errors, integrations, webhooks
- Platform bugs or unexpected behavior

General
- How-to questions
- Feature availability
- Data exports, reports, or UI navigation

Important rules
- Questions about exporting, viewing, or downloading invoices are General, not Billing
- Billing ONLY applies when money was charged, refunded, or paid incorrectly
```

## 4.4 Node settings (inputs and outputs)

1. Select **Node settings**.
2. **Input message**: `Local.CurrentTicket`.
3. **Save agent output message as**: create a new variable `TriageOutputText`.
4. **Save the output json_object as**: create a new variable `TriageOutputJson`.
   (Spell both exactly like this; the conditions on the next page use them.)
5. Select **Done**, then **Save**.

✅ **Checkpoint:** inside *For each* you see the *Triage-Agent* node.
