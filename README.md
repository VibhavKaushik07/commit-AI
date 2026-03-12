# commit-AI
A context-aware AI Git Agent powered by Gemini 2.0 that analyzes local diffs and autonomously suggests Conventional Commit messages.

# 🤖 Commit-Whisperer: AI Git Agent

Commit-Whisperer is a Python-based **AI Agent** designed to automate the most tedious part of the development workflow: writing meaningful commit messages. 

By utilizing the **Gemini 2.5 Flash** model, the agent "perceives" your staged code changes, "reasons" about the intent of your modifications, and "acts" by generating and executing a structured Git commit.

## 🧠 Agent Architecture
- **Perception:** Uses `subprocess` to read the raw `git diff --cached` output.
- **Reasoning:** Employs **Prompt Engineering** to constrain the LLM to the [Conventional Commits](https://www.conventionalcommits.org/) standard.
- **Action:** An interactive CLI loop that allows the user to approve and execute `git commit` directly from Python.

## 🚀 Features
- **Zero-Config Logic:** Automatically identifies "feat", "fix", and "chore" from code context.
- **Human-in-the-loop:** Interactive confirmation before any permanent changes are made.
- **Privacy Focused:** Uses `.env` for API key management to ensure secrets are never leaked.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **AI Model:** Google Gemini 2.5 Flash
- **Tools:** Git CLI, `google-genai` SDK, `python-dotenv`

## 📦 Installation & Setup
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/commit-whisperer.git](https://github.com/YOUR_USERNAME/commit-whisperer.git)
   cd commit-whisperer
