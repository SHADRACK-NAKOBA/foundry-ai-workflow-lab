import os, json, re, sys
from dotenv import load_dotenv

# Add references




def print_workflow_output(output_text):
    """Print each ticket as: category, confidence, issue, then the workflow's response.

    Falls back to the raw text if the output doesn't look like the expected format.
    """
    tickets = re.findall(r"(\{.*?\})(.*?)(?=\{|$)", output_text, re.DOTALL)
    if not tickets:
        print(output_text)
        return

    try:
        for ticket_number, (ticket_json, response_text) in enumerate(tickets, start=1):
            ticket = json.loads(ticket_json)
            print("\n" + "=" * 80)
            print(f"Ticket {ticket_number}: {ticket['category']} ({float(ticket['confidence']):.0%} confidence)")
            print("-" * 80)
            print(f"Issue: {ticket['customer_issue']}")
            print("\nResponse:")
            print(response_text.strip())
        print("=" * 80 + "\n")
    except (ValueError, KeyError, TypeError):
        print(output_text)


load_dotenv()

# Accept the variable name used in this repo or the one the Foundry portal shows.
endpoint = os.getenv("PROJECT_ENDPOINT") or os.getenv("AZURE_EXISTING_AIPROJECT_ENDPOINT")
if not endpoint or "your_project_endpoint" in endpoint:
    sys.exit(
        "PROJECT_ENDPOINT is not set. Copy .env.example to .env, paste your project endpoint "
        "(Foundry portal > your workflow > Code > .env variables), save the file and run again."
    )
workflow_name = os.getenv("WORKFLOW_NAME", "ContosoPay-Customer-Support-Triage")

# Connect to the AI Project client
# (Step 2 of "Invoke the workflow from code". Everything after this block is
#  indented by 4 spaces so it runs INSIDE the "with" block.)


    # Specify the workflow


    # Create a conversation and run the workflow


    # Process events from the workflow run


    # Clean up resources

