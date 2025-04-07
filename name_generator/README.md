# Brand Name Generator

A web application that generates creative brand names and checks domain availability and LTD name conflicts using a multi-agent architecture.

## Features

- **Name Generation**: Create unique brand names based on industry, keywords, tone, and target audience
- **Multiple Generation Models**: Choose from different name generation models:
  - Local Pattern Generator (fastest, no API key required)
  - OpenAI GPT-3.5 Turbo (most creative, requires API key)
  - Hugging Face SmollAgent (good balance, requires API key)
  - Ollama Mistral (local LLM, requires Ollama installation)
- **Domain Availability Check**: Check if domain names are available across multiple TLDs (.com, .co.uk)
- **LTD Name Conflict Check**: Check if company names are available for UK Companies House registration
- **Visual Status Indicators**: Color-coded status indicators for domain and LTD availability
- **Interactive UI**: Modern, responsive interface with tooltips and real-time feedback

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the backend directory with your API keys:
   ```
   OPENAI_API_KEY=your_api_key_here
   DOMAINR_API_KEY=your_domainr_api_key_here
   COMPANIES_HOUSE_API_KEY=your_companies_house_api_key_here
   MOCK_DOMAIN_CHECKS=false
   MOCK_LTD_CHECKS=false
   ```

## Running the Application

Run the application using uvicorn:

```bash
cd name_generator/backend
uvicorn main:app --reload --port 8000 --ssl-keyfile=/path/to/key.pem --ssl-certfile=/path/to/cert.pem
```

The API will be available at `https://localhost:8000`

## API Endpoints

### POST /generate-brand-names

Generates brand name ideas based on the provided criteria.

Request body:
```json
{
    "industry": "string",
    "keywords": ["string"],
    "tone": "string",
    "audience": "string" (optional),
    "generator_type": "string" (optional, default: "local")
}
```

Response:
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

### POST /check-domain

Checks domain availability for a single name.

Request body:
```json
{
    "name": "string"
}
```

Response:
```json
{
    "domain_available": true,
    "available_domains": ["name.com", "name.co.uk"]
}
```

### POST /check-ltd

Checks LTD name conflicts for a single name.

Request body:
```json
{
    "name": "string"
}
```

Response:
```json
{
    "ltd_available": true,
    "similar_names": []
}
```

## Architecture

The application uses a multi-agent architecture:

- **BrandNameAgent**: Generates brand names based on user criteria
- **DomainCheckerAgent**: Checks domain availability across multiple TLDs
- **LTDCheckerAgent**: Checks for name conflicts with UK Companies House

## Frontend

The frontend is built with HTML, CSS, and JavaScript, using Tailwind CSS for styling. It provides:

- A form for entering name generation criteria
- A model selector for choosing the generation method
- Results display with color-coded availability indicators
- Tooltips showing detailed availability information
- Manual check buttons for domain and LTD availability

## Feature Flags

The application supports feature flags for testing and development:

- `MOCK_DOMAIN_CHECKS`: Set to `true` to use mock data for domain checks
- `MOCK_LTD_CHECKS`: Set to `true` to use mock data for LTD checks

## License

MIT