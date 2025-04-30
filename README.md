# Brand Name Generator

A web application that generates creative brand names and checks domain availability and LTD name conflicts using a multi-agent architecture.

---

## Features

- **Name Generation** – Create unique brand names based on industry, keywords, tone, and target audience.
- **Multiple Generation Models** – Choose from:
  - Local Pattern Generator (fastest, no API key required)
  - OpenAI GPT-3.5 Turbo (most creative, requires API key)
  - Hugging Face SmollAgent (balanced, requires API key)
  - Ollama Mistral (local LLM, requires Ollama)
- **Domain and LTD Checks** – Verify availability across multiple TLDs and UK Companies House.
- **Visual Indicators** – Color-coded results for quick status recognition.
- **Interactive UI** – Responsive frontend with tooltips and manual override options.

---

## Tech stack

- Python (FastAPI, Uvicorn)
- HTML, JavaScript, Tailwind CSS
- Multi-agent architecture (custom agents)
- OpenAI API, Hugging Face, Domainr API, Companies House API
- Ollama (for local LLM integration)

---

## Architecture

- **BrandNameAgent** – Generates brand names based on user inputs.
- **DomainCheckerAgent** – Checks domain availability across TLDs.
- **LTDCheckerAgent** – Checks for name conflicts on UK Companies House.
- Frontend communicates with backend APIs to display and interact with data in real time.

---

## API Endpoints

### POST `/generate-brand-names`
Generates brand name ideas.

**Request:**
```json
{
  "industry": "string",
  "keywords": ["string"],
  "tone": "string",
  "audience": "string",
  "generator_type": "string"
}
```

**Response:**
```json
{
  "names": {
    "name1": {},
    "name2": {},
    "name3": {}
  },
  "total_count": 3
}
```

---

### POST `/check-domain`
Checks domain availability.

**Request:**
```json
{
  "name": "string"
}
```

**Response:**
```json
{
  "domain_available": true,
  "available_domains": ["name.com", "name.co.uk"]
}
```

---

### POST `/check-ltd`
Checks LTD name availability.

**Request:**
```json
{
  "name": "string"
}
```

**Response:**
```json
{
  "ltd_available": true,
  "similar_names": []
}
```

---

## Setup the application

1. Clone the repository:

   ```bash
   git clone https://github.com/[your-username]/brand-name-generator.git
   cd brand-name-generator
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the `backend/` directory with:

   ```env
   OPENAI_API_KEY=your_api_key_here
   DOMAINR_API_KEY=your_domainr_api_key_here
   COMPANIES_HOUSE_API_KEY=your_companies_house_api_key_here
   MOCK_DOMAIN_CHECKS=false
   MOCK_LTD_CHECKS=false
   ```

---

## Run the application

```bash
cd name_generator/backend
uvicorn main:app --reload --port 8000 --ssl-keyfile=/path/to/key.pem --ssl-certfile=/path/to/cert.pem
```

API available at: `https://localhost:8000`

---

## License

MIT