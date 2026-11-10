# 9 · Clean up

[⬅ Share your learnings](08-share-your-learnings.md) · [Next: Troubleshooting ➡](10-troubleshooting.md)

Delete the resources so you stop paying.

1. Open the Azure portal at <https://portal.azure.com>.
2. In the search bar, type **Resource groups** and open it.
3. Open the resource group of your Foundry project:
   - `rg-prince-workflow` if you created it on page 2, or
   - the one shown in the Foundry portal under your project's **Overview** → **Project details** → **Resource group**.
4. Check it only contains this lab's resources (a Foundry / AI Services resource and its project).
5. Select **Delete resource group**, type the resource group name, select **Delete**.
6. Wait for the *Deleted resource group* notification (2–5 minutes).

> ⚠️ Don't delete a resource group that other projects use. If the Foundry resource is shared, delete only the project: Foundry portal → project drop-down → **Manage** → your project → **Delete**.

Locally, you can delete the `labenv` folder. The repo stays on your machine.
