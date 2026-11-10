# 3 · Create the workflow, the ticket list and the loop

[⬅ Create a Foundry project](02-create-foundry-project.md) · [Next: Triage Agent ➡](04-triage-agent.md)

> 📋 Every value you paste in this lab is also in the [`workflow-inputs/`](../workflow-inputs) folder, ready to copy without formatting problems.

## 3.1 Create a blank workflow

1. On the Foundry home page, select **Build** in the top toolbar.
2. In the left menu select **Agents**, then the **Workflows** tab.
3. Upper right: **Create** → **Blank workflow**.
   (This is a *sequential* workflow; starting blank just makes adding nodes simpler.)
4. Select **Save** in the visualizer. Name it exactly:

   ```text
   ContosoPay-Customer-Support-Triage
   ```

   and select **Save**.

   ⚠️ Your Python code calls the workflow **by this name**. If you use a different name, put it in `WORKFLOW_NAME` in your `.env` later.

## 3.2 Create the ticket array variable

1. In the visualizer, select the **+** icon to add a node.
2. Under **Data transformation**, select **Set variable**.
3. **Variable name**: `SupportTickets` (it appears as `Local.SupportTickets`).
4. **To value**: paste the array from [`workflow-inputs/support-tickets.json`](../workflow-inputs/support-tickets.json):

   ```json
   [
     "The API returns a 403 error when creating invoices, but our API key hasn't changed.",
     "Is there a way to export all invoices as a CSV?",
     "I was charged twice for the same invoice last Friday and my customer is also seeing two receipts. Can someone fix this?"
   ]
   ```

5. Select **Done**.

## 3.3 Add a for-each loop

1. Select the **+** icon **below** the *Set variable* node → **For each**.
2. **Select the items to loop for each**: `Local.SupportTickets`.
3. **Loop Value Variable**: create a new variable named `CurrentTicket`.
4. Select **Done**, then **Save** (top of the visualizer).

✅ **Checkpoint:** the canvas shows *Set variable* → *For each*.
