# 5 · Handle low confidence and route by category

[⬅ Triage Agent](04-triage-agent.md) · [Next: Resolution Agent and preview ➡](06-resolution-agent-and-preview.md)

All four values on this page are in [`workflow-inputs/conditions-and-messages.txt`](../workflow-inputs/conditions-and-messages.txt).

## 5.1 First If/Else: is the classification confident?

1. Select the **+** icon **below** the *Triage-Agent* node.
2. Under **Flow**, select **If/Else**.
3. Select **Add a path**, then the **pencil** icon to edit the condition.
4. **Condition**:

   ```text
   Local.TriageOutputJson.confidence > 0.6
   ```

5. Select **Done**.

## 5.2 Else branch: ask for more details

1. Under the **Else** branch of this If/Else, select **+**.
2. Under **Basics**, select **Deliver a message**.
3. **Message to send**:

   ```text
   The support ticket classification has low confidence. Requesting more details about the issue: "{Local.CurrentTicket}"
   ```

4. Select **Done**.

## 5.3 Second If/Else (inside the If branch): is it a billing issue?

1. Under the **If** branch of the **first** If/Else, select **+**.
2. Under **Flow**, select **If/Else**.
3. Select **Add a path**, then the **pencil** icon.
4. **If condition**:

   ```text
   Local.TriageOutputJson.category = "Billing"
   ```

   (A single `=`, and straight quotes `"`, not curly quotes.)
5. Select **Done**.

## 5.4 If branch: escalate billing to a human

1. Under the **If** branch of the **second** If/Else, select **+**.
2. Under **Basics**, select **Deliver a message**.
3. **Message to send**:

   ```text
   Escalate billing issue to human support team.
   ```

4. Select **Done**, then **Save**.

✅ **Checkpoint:** *Triage-Agent* → If/Else (confidence) → [Else: ask for details] / [If: second If/Else (Billing) → If: escalate]. The second If/Else's **Else** branch is still empty; you fill it next.
