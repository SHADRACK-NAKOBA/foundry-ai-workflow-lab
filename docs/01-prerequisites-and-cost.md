# 1 · Prerequisites and cost

[⬅ Overview](00-overview-and-concepts.md) · [Next: Create a Foundry project ➡](02-create-foundry-project.md)

## You need

| Item | Notes |
|---|---|
| **Azure subscription** | Free Trial or paid. You need **Owner** or **Contributor** on it to create a Foundry project. |
| **Edge or Chrome** | For the Foundry portal. |
| **Visual Studio Code** | <https://code.visualstudio.com/> (a Windows VM in the cloud works too). |
| **Python 3.13 (or 3.12)** | <https://www.python.org/downloads/>. ⚠️ **Not 3.14**: some packages have no 3.14 build yet and `pip install` fails. Tick **Add python.exe to PATH** in the installer. |
| **Git** | <https://git-scm.com/downloads> |
| **Azure CLI** | <https://learn.microsoft.com/cli/azure/install-azure-cli>, used for `az login`. |

### Check your tools

Open a **new** terminal (PowerShell on Windows) and run:

```powershell
python --version
git --version
az --version
```

`python --version` must show **3.12.x** or **3.13.x**. If it shows 3.14, install 3.13 and run `py -3.13 --version` to use it (see [Troubleshooting](10-troubleshooting.md#python-314)).

## Cost

| Item | Cost |
|---|---|
| Foundry project | No charge on its own |
| Model calls (about 3 tickets × 2 agents per run) | A few cents per run |
| **Total for the lab** | **About US $0.20** if you [clean up](09-cleanup.md) at the end |

Pricing: <https://azure.microsoft.com/pricing/details/ai-foundry/>

> 💡 Set a **budget alert** first: Azure portal → **Cost Management** → **Budgets** → **+ Add** → amount $5 → alert at 80%.
