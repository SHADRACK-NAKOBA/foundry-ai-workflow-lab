# 7 · Run the workflow from Python (VS Code)

[⬅ Resolution Agent and preview](06-resolution-agent-and-preview.md) · [Next: Share your learnings ➡](08-share-your-learnings.md)

Now call the same workflow from code, like an application would, with the **Azure AI Projects SDK**.

## 7.1 Get the code

1. Open **VS Code**.
2. Press **Ctrl+Shift+P** (Mac: **⌘+Shift+P**) → type **Git: Clone** → Enter.
3. Paste:

   ```text
   https://github.com/SHADRACK-NAKOBA/foundry-ai-workflow-lab.git
   ```

4. Pick or create a folder (for example `Documents\labs`) → **Select as Repository Destination** → **Open**.
5. In the Explorer, expand the **Python** folder: `workflow.py` (you complete it), `solution/workflow.py` (finished version), `requirements.txt`, `.env.example`.

## 7.2 Copy your project endpoint

1. In the browser, go back to your workflow in the Foundry portal.
2. Upper right, select **Code** → **.env variables**.
3. Copy the value of **AZURE_EXISTING_AIPROJECT_ENDPOINT**. It looks like
   `https://<resource>.services.ai.azure.com/api/projects/<project>`.

## 7.3 Create the virtual environment

1. In VS Code, right-click **Python/requirements.txt** → **Open in Integrated Terminal**.
2. Run, one line at a time:

   **Windows (PowerShell)**

   ```powershell
   python -m venv labenv
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   .\labenv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

   **macOS / Linux**

   ```bash
   python3 -m venv labenv
   source labenv/bin/activate
   pip install -r requirements.txt
   ```

   The prompt now starts with `(labenv)`. The `Set-ExecutionPolicy` line fixes *"running scripts is disabled on this system"* for this terminal only.

## 7.4 Create your .env file

1. In the same terminal:

   ```powershell
   Copy-Item .env.example .env      # macOS/Linux: cp .env.example .env
   ```

2. Open **Python/.env** and replace `your_project_endpoint` with the endpoint you copied (keep the quotes).
3. If you named your workflow differently, change `WORKFLOW_NAME` to match it **exactly**.
4. **Ctrl+S** to save.

> `.env` is in `.gitignore`, so your endpoint is never committed.

## 7.5 Complete workflow.py

Open **Python/workflow.py**. Add each block under its comment. **Indentation matters:** blocks 3–6 are indented 4 spaces because they run inside the `with` block. If you get stuck, compare with [`solution/workflow.py`](../Python/solution/workflow.py).

**1. Under `# Add references`**

```python
# Add references
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
```

**2. Under `# Connect to the AI Project client`** (no indentation)

```python
# Connect to the AI Project client
with (
    DefaultAzureCredential() as credential,
    AIProjectClient(endpoint=endpoint, credential=credential) as project_client,
    project_client.get_openai_client() as openai_client,
):
```

**3. Under `    # Specify the workflow`** (4 spaces)

```python
    # Specify the workflow
    workflow = {
        "name": workflow_name
    }
```

`workflow_name` comes from `WORKFLOW_NAME` in your `.env`.

**4. Under `    # Create a conversation and run the workflow`** (4 spaces)

```python
    # Create a conversation and run the workflow
    conversation = openai_client.conversations.create()
    print(f"Created conversation (id: {conversation.id})")

    stream = openai_client.responses.create(
        conversation=conversation.id,
        extra_body={"agent_reference": {"name": workflow["name"], "type": "agent_reference"}},
        input="Start",
        stream=True,
    )
```

**5. Under `    # Process events from the workflow run`** (4 spaces)

```python
    # Process events from the workflow run
    for event in stream:
        if event.type == "response.completed":
            print("\nResponse completed:")
            response = openai_client.responses.retrieve(event.response.id)
            print_workflow_output(response.output_text)
        elif event.type == "response.failed":
            print("\nThe workflow run failed:")
            print(getattr(event.response, "error", None))
            print("See docs/10-troubleshooting.md")
```

**6. Under `    # Clean up resources`** (4 spaces)

```python
    # Clean up resources
    openai_client.conversations.delete(conversation_id=conversation.id)
    print("\nConversation deleted")
```

Save with **Ctrl+S**.

> 💡 VS Code tip: select lines and press **Tab** / **Shift+Tab** to indent or unindent.

## 7.6 Sign in and run

1. Sign in to Azure (a browser window opens):

   ```powershell
   az login
   ```

   Pick the subscription that holds your Foundry project if asked. No browser, or MFA/tenant errors? Use `az login --use-device-code` (see [Troubleshooting](10-troubleshooting.md#az-login)).

2. Run:

   ```powershell
   python workflow.py
   ```

3. After 20–60 seconds you should see:

   ```text
   Created conversation (id: conv_...)

   Response completed:

   ================================================================================
   Ticket 1: Technical (100% confidence)
   --------------------------------------------------------------------------------
   Issue: API returns a 403 error when creating invoices, API key unchanged.

   Response:
   Thank you for contacting us about the 403 error when creating invoices ...
   ================================================================================
   Ticket 2: General (95% confidence)
   ...
   Ticket 3: Billing (98% confidence)
   ...
   Response:
   Escalate billing issue to human support team.
   ================================================================================

   Conversation deleted
   ```

   Your wording and confidence numbers will differ; the categories should match.

4. When done:

   ```powershell
   deactivate
   ```

📸 **Screenshot** the terminal output.

✅ **Checkpoint:** the code ran your portal-built workflow and printed all three tickets.
