# 2 · Create a Microsoft Foundry project

[⬅ Prerequisites](01-prerequisites-and-cost.md) · [Next: Build the workflow ➡](03-build-the-workflow.md)

A Foundry **project** organizes the models, agents and workflows for one solution.

1. Open the Foundry portal at <https://ai.azure.com> and sign in with your Azure account.
2. At the top, make sure the **New Foundry** toggle is **On**.
3. If you're prompted to create a project, select **Create a new project**.
   If not, open the **project drop-down** in the upper left and select **Create new project**.
4. **Project name**: `prince-workflow-project`.
5. If you see **Advanced options**, expand it and check:
   - **Resource group** → **Create new** → `rg-prince-workflow`. A dedicated resource group makes [clean up](09-cleanup.md) one click.
   - **Region**: keep the default (East US 2 or Sweden Central work well).
6. Select **Create** and wait 1–3 minutes until the Foundry home page opens with your project selected.
7. Close the **Welcome to the new Microsoft Foundry** dialog if it appears. You'll create agents later, inside the workflow.

## Check you have a model deployment

The agents need a chat model.

1. In the top toolbar select **Build**, then **Models** in the left menu.
2. If you see a deployment (for example `gpt-4.1-mini`, `gpt-5-mini` or `gpt-4o-mini`), you're done: go to the next page.
3. If the list is empty, select **Deploy a base model** → search **gpt-5-mini** (or any chat model offered) → **Deploy** → keep the defaults → **Deploy**.

> If the deploy fails with a **quota** error, pick another model from the list or another region. See [Troubleshooting](10-troubleshooting.md#no-model--quota).

✅ **Checkpoint:** the project is selected at the top of the portal and has one model deployment.
