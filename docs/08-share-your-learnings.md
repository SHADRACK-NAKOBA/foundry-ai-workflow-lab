# 8 · Share your learnings

[⬅ Run from code](07-run-from-code.md) · [Next: Clean up ➡](09-cleanup.md)

Hands-on work you can show is worth more than certificates you can only list. Share it before you delete the resources.

## What to capture

1. The finished workflow canvas in the Foundry portal.
2. The **Preview** chat showing a drafted reply and the billing escalation.
3. The VS Code terminal output from `python workflow.py`.

## LinkedIn post template

> **I built an AI support triage workflow in Microsoft Foundry, and called it from Python.**
>
> **Problem:** support teams waste hours sorting tickets, and an AI that auto-answers billing disputes is a risk.
>
> **What I built:** a workflow that loops through tickets, uses a Triage Agent with **strict JSON output** to classify each one (Billing / Technical / General + confidence), then:
> - asks for more details when confidence is low (≤ 0.6),
> - **escalates billing issues to a human**,
> - lets a Resolution Agent draft replies for technical and general questions.
>
> **How:** Microsoft Foundry workflows (variables, for-each, If/Else, agent nodes), JSON Schema structured outputs, and the Azure AI Projects SDK to run the same workflow from Python.
>
> **What I learned:** let the model classify, but let deterministic rules decide what happens next.
>
> [screenshots]
>
> #MicrosoftFoundry #AIAgents #AzureAI #GenAI #Automation #Python

Tag **Prince** so the post reaches more people, and share your screenshots in the **Prince** community lab thread.
