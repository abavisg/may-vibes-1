# 🧠 May AI Vibes – Day 1: Brand Name Generator Agent  
> Hashtag: **#may-ai-vibes**  
> Project: Build an AI agent that generates 100 business name ideas with `.com` domain availability and no UK LTD conflict.  
> Goal: Publish a blog post + LinkedIn breakdown after the build.

---

## ✅ Scope

This project covers:

1. **User Input**: Brief for the brand (industry, keywords, tone, audience).
2. **AI Name Generation**: 100 creative brand name ideas using OpenAI.
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

## 📢 Planned LinkedIn Post (Draft)

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

---

## ✍️ Blog Post (Coming Soon)

_Title_: **From Idea to Identity in Minutes – Building an AI Naming Agent in Cursor**  
_Link_: _Coming soon after full project completion_
