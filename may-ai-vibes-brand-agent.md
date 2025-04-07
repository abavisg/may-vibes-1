# 🧠 May AI Vibes – Day 1: Brand Name Generator Agent  
> Hashtag: **#may-ai-vibes**  
> Project: Build an AI agent that generates 100 business name ideas with `.com` domain availability and no UK LTD conflict.  
> Goal: Publish a blog post + LinkedIn breakdown after the build.

---

## ✅ Scope

This project covers:

1. **User Input**: Brief for the brand (industry, keywords, tone, audience).
2. **AI Name Generation**: 100 creative brand name ideas using an LLM (OpenAI, HuggingFace, Llama).
3. **.com Domain Availability Check**: Using Domainr API (or fallback).
4. **UK Companies House LTD Conflict Check**: Via official UK API.
5. **Return Result**: A list of names with domain + LTD status flags.

---

## 🧾 Prompt for Cursor (Start Here)

\`\`\`plaintext
Build a FastAPI app in Python with the following endpoint:

**POST /generate-names**

Request Body:
- industry: str
- keywords: list[str]
- tone: str (e.g. playful, professional, luxury)
- audience: str (optional)

Behavior:
1. Use the OpenAI API (GPT-4 or GPT-3.5) to generate 100 brand name ideas based on the input fields.
2. The output should be diverse, creative, and tailored to the tone, industry, and keywords.
3. Return the 100 names in a JSON response.

Folder Structure:
- backend/
  - main.py (FastAPI app)
  - agents/name_generator.py (contains the logic to generate names via OpenAI)
  - models/schemas.py (Pydantic models for request/response)
  - requirements.txt (include openai, fastapi, uvicorn, pydantic)

No domain or LTD checks yet—just generation based on the brief.

The response JSON should look like:
{
  "names": ["Brandify", "Flowgen", "Codexa", ...]
}

Also scaffold a README with how to run the app locally with uvicorn.
\`\`\`

---

## 🗂️ Planned Folder Structure

\`\`\`
/brandbooster/
├── main.py
├── agents/
│   ├── name_generator.py
│   ├── domain_checker.py
│   └── ltd_checker.py
├── models/
│   └── schemas.py
├── requirements.txt
└── README.md
\`\`\`

---

## 🧱 Stack

- **IDE**: Cursor
- **Backend**: Python + FastAPI
- **AI**: OpenAI GPT-4
- **Domain Check**: Domainr API or fallback
- **Companies House Check**: UK Company Info API
- **No DB**: Everything in memory for now

---

## 🛠️ Development Progress Log

- [ ] Scaffolding project structure in Cursor
- [ ] Implemented `/generate-names` endpoint
- [ ] Integrated OpenAI for name generation
- [ ] Added domain availability check
- [ ] Added LTD name conflict check
- [ ] Combined + returned final result
- [ ] Tested with real prompts + input combos
- [ ] Wrote blog post draft
- [ ] Published LinkedIn update

---





🧠 May AI Vibes – Brand Name Generator Agent

A smart and flexible web app that generates unique brand name ideas and checks domain and UK LTD name availability—powered by a multi-agent system.

🚀 What It Does
	•	✨ Name Generation
Create standout brand names tailored to your industry, keywords, tone, and audience.
	•	🧠 Multiple Models Available
Choose your generator:
	•	Local Pattern Generator (fast, no API key)
	•	OpenAI GPT-3.5 Turbo (most creative, needs API key)
	•	Hugging Face SmollAgent (balanced, needs API key)
	•	Ollama Mistral (offline/local, requires Ollama)
	•	🌐 Domain Checker
Instantly see domain availability across TLDs like .com, .co.uk, etc.
	•	🏢 UK LTD Name Checker
Checks for conflicts in UK Companies House records.
	•	🔵 Real-Time Visual Feedback
Color-coded indicators show what’s available and what’s not.
	•	🖥️ Modern UI
Interactive, responsive interface with tooltips and real-time updates.

⸻

📘 Description

This agent is part of the #may-ai-vibes series — a month-long exploration of building AI-powered micro-tools. This one focuses on the very beginning of any business journey: naming.

🎯 Scope

The app helps generate brand names tailored to the user’s industry, tone, keywords, and optionally their target audience. It checks domain name availability and UK LTD name conflicts to help validate the best options.

⚙️ Behaviour
	•	Accepts user input via a modern web UI
	•	Generates names using selectable models (local, OpenAI, Hugging Face, Ollama)
	•	Calls APIs to check .com and .co.uk domain availability
	•	Checks UK Companies House for LTD conflicts
	•	Displays results with color-coded indicators for instant feedback

📅 Development Progress
	•	✅ Setup multi-agent architecture
	•	✅ Built FastAPI backend
	•	✅ Integrated name generators (local + OpenAI + HF + Ollama)
	•	✅ Built domain + LTD checker agents
	•	✅ Designed frontend

🧱 Tech Stack
	•	Frontend: HTML, Vanilla JS, Tailwind CSS
	•	Backend: Python, FastAPI, Uvicorn
	•	Agents: Custom logic for name generation, domain, and LTD checks
	•	APIs: Domainr, Companies House
	•	Models: OpenAI GPT-3.5 Turbo, Hugging Face SmollAgent, Ollama Mistral

⸻

📢 LinkedIn Post

> Day X of #may-ai-vibes  
>  
> I built the first part of an agent that helps you go from an idea 💡 to a real brand name 💥.  
> You give it your industry, keywords, and tone → it gives you 100 available `.com` names with no conflict on Companies House 🇬🇧.  
>  
> Next up: generate the landing page automatically.  
>  
> Want to try it or see the next post? Follow along.  
>  
> #buildinpublic #aiagents #founderstack #may-ai-vibes

✍️ Blog Post

_Title_: **From Idea to Identity in Minutes – Building an AI Naming Agent in Cursor**  
_Link_: _Coming soon after full project completion_

