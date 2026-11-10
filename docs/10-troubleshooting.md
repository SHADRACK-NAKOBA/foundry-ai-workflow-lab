# 10 · Troubleshooting

[⬅ Clean up](09-cleanup.md) · [Next: Interview questions ➡](11-interview-questions.md)

| # | Symptom | Jump to |
|---|---|---|
| 1 | *"The '.' operator cannot be used on Unknown values"* in Preview | [Unknown values error](#unknown-values-error) |
| 2 | Agent has no model / quota error when deploying | [No model / quota](#no-model--quota) |
| 3 | Billing ticket gets an AI reply, or nothing is escalated | [Wrong routing](#wrong-routing) |
| 4 | `pip install` fails building a package | [Python 3.14](#python-314) |
| 5 | *"running scripts is disabled on this system"* | [Activate.ps1 blocked](#activateps1-blocked) |
| 6 | `IndentationError` / `SyntaxError` in workflow.py | [Indentation](#indentation) |
| 7 | *"PROJECT_ENDPOINT is not set"* | [Endpoint not set](#endpoint-not-set) |
| 8 | `DefaultAzureCredential failed`, 401, tenant or MFA errors | [az login](#az-login) |
| 9 | 404 / *agent not found* / workflow not found | [Workflow name](#workflow-name) |
| 10 | Script stops mid-stream or a broken virtual environment | [Rebuild the environment](#rebuild-the-environment) |

---

### Unknown values error

`Unhandled workflow failure ... (ConditionGroup) -> Error: The '.' operator cannot be used on Unknown values.`

The condition reads `Local.TriageOutputJson.confidence`, but `TriageOutputJson` is empty. Fix:

1. Open **Triage-Agent** → **Parameters** → **Text format** must be **JSON Schema** with the `category_response` schema ([page 4.2](04-triage-agent.md#42-force-json-output-the-step-that-prevents-most-errors)).
2. **Node settings** → **Save the output json_object as** must be exactly `TriageOutputJson`.
3. Save the workflow, then **Preview** again (a new preview, not the old chat).

### No model / quota

**Build** → **Models** → **Deploy a base model**. If you get a quota error, try another model (gpt-5-mini, gpt-4o-mini, gpt-4.1-mini) or create the project in another region (East US 2, Sweden Central). Then open each agent and select the deployment under **Details**.

### Wrong routing

- Billing condition must be `Local.TriageOutputJson.category = "Billing"` with straight quotes and a capital **B**.
- The *Escalate* message must be on the **If** branch of the **second** If/Else; the Resolution-Agent on its **Else** branch.
- The second If/Else must sit under the **If** branch of the **first** If/Else, not under its Else.

### Python 3.14

Some dependencies have no 3.14 build yet. Install **Python 3.13** and create the environment with it:

```powershell
py -3.13 -m venv labenv
```

### Activate.ps1 blocked

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\labenv\Scripts\Activate.ps1
```

This only affects the current terminal.

### Indentation

Everything after `with (...):` must be indented **4 spaces**; inside `for` and `if`, 8 and 12. Compare with [`Python/solution/workflow.py`](../Python/solution/workflow.py), or run the finished version directly:

```powershell
python solution\workflow.py      # macOS/Linux: python solution/workflow.py
```

### Endpoint not set

Run the script from the **Python** folder, check the file is named `.env` (not `.env.txt` or `.env.example`), paste the endpoint between the quotes, and save with **Ctrl+S**.

### az login

```powershell
az login --use-device-code
az account set --subscription "<subscription name or id>"
```

If your account is in several tenants: `az login --tenant <tenant-id>` (Azure portal → **Microsoft Entra ID** → **Tenant ID**). The account you sign in with must have access to the Foundry project.

### Workflow name

`WORKFLOW_NAME` in `.env` must match the name in **Build** → **Agents** → **Workflows** exactly, including case and dashes. Make sure you selected **Save** in the visualizer.

### Rebuild the environment

**Windows (PowerShell)**

```powershell
deactivate
Remove-Item -Recurse -Force labenv
python -m venv labenv
.\labenv\Scripts\Activate.ps1
pip install -r requirements.txt
az login
python workflow.py
```

(`rmdir /s /q` only works in Command Prompt, not PowerShell.)

**macOS / Linux**

```bash
deactivate; rm -rf labenv
python3 -m venv labenv && source labenv/bin/activate && pip install -r requirements.txt
az login && python workflow.py
```

---

Still stuck? Post the **page and step number** and a screenshot of the **full** error (hide your endpoint and subscription ID) in the **Prince** community lab thread.
