🧠 May AI Vibes – Brand Name Generator Agent

A smart and flexible web app that generates unique brand name ideas and checks domain and UK LTD name availability—powered by a multi-agent system.

🚀 What It Does
The app helps generate brand names tailored to the user’s industry, tone, keywords, and optionally their target audience. It checks domain name availability and UK LTD name conflicts to help validate the best options.

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

🎯 Scope
The app helps generate brand names tailored to the user’s industry, tone, keywords, and optionally their target audience. It checks domain name availability and UK LTD name conflicts to help validate the best options.

⚙️ Behaviour
	•	Accepts user input via a modern web UI
	•	Generates names using selectable models (local, OpenAI, Hugging Face, Ollama)
	•	Calls APIs to check .com and .co.uk domain availability
	•	Checks UK Companies House for LTD conflicts
	•	Displays results with color-coded indicators for instant feedback

🧱 Tech Stack
	•	Frontend: HTML, Vanilla JS, Tailwind CSS
	•	Backend: Python, FastAPI, Uvicorn
	•	Agents: Custom logic for name generation, domain, and LTD checks
	•	APIs: Domainr (requires token), Companies House (requires token)
	•	Models: OpenAI GPT-3.5 Turbo (requires token), Hugging Face SmollAgen (requires token), Ollama Mistral (local running via Ollama) and local logic for testing fast

📅 Development Progress
	•	✅ Setup multi-agent architecture
	•	✅ Built endpoints with FastAPI
	•	✅ Integrated name generators (local + OpenAI + HF + Ollama)
	•	✅ Built domain + LTD checker agents
	•	✅ Designed frontend in HTML, JS and Tailwind CSS

