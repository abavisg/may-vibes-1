# Brand Name Generator API

A FastAPI application that generates creative brand names using OpenAI's GPT models and checks domain availability and LTD name conflicts using a multi-agent architecture.

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
   ```

## Running the Application

Run the application using uvicorn:

```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

### POST /generate-names

Generates 100 brand name ideas based on the provided criteria.

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
    "names": ["string"]
}
```

### POST /check-domains

Checks domain availability for a list of domain names.

Request body:
```json
["domain1", "domain2", "domain3"]
```

Response:
```json
{
    "names": {
        "domain1": true,
        "domain2": false,
        "domain3": true
    },
    "available_count": 2,
    "total_count": 3
}
```

### POST /check-ltd

Checks LTD name conflicts for a list of names.

Request body:
```json
["name1", "name2", "name3"]
```

Response:
```json
{
    "names": {
        "name1": true,
        "name2": false,
        "name3": true
    },
    "available_count": 2,
    "total_count": 3
}
```

### POST /generate-brand-names

Generates brand names and checks domain availability and LTD conflicts in one step.

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
        "name1": {
            "domain_available": true,
            "ltd_available": true,
            "fully_available": true
        },
        "name2": {
            "domain_available": false,
            "ltd_available": true,
            "fully_available": false
        },
        "name3": {
            "domain_available": true,
            "ltd_available": false,
            "fully_available": false
        }
    },
    "domain_available_count": 2,
    "ltd_available_count": 2,
    "fully_available_count": 1,
    "total_count": 3
}
```

### GET /agents

Lists all available agents in the system.

Response:
```json
{
    "agents": ["NameGenerator", "DomainChecker", "LTDChecker", "BrandName"]
}
```

## Multi-Agent Architecture

The application uses a multi-agent architecture to handle different aspects of the brand name generation process:

1. **NameGenerator Agent**: Generates creative brand names based on the provided criteria.
2. **DomainChecker Agent**: Checks domain availability for the generated names.
3. **LTDChecker Agent**: Checks LTD name conflicts for the generated names.
4. **BrandName Agent**: Orchestrates the entire process, combining the results from all agents.

Each agent is responsible for a specific task and can be used independently or as part of the complete process.

## API Keys

### Domainr API

The application uses the Domainr API to check domain availability. If no API key is provided, it will fall back to a simulated check (not accurate).

To get a Domainr API key:
1. Sign up at https://domainr.com/
2. Navigate to the API section
3. Generate an API key
4. Add the key to your `.env` file

### Companies House API

The application uses the Companies House API to check LTD name conflicts. If no API key is provided, it will fall back to a simulated check (not accurate).

To get a Companies House API key:
1. Sign up at https://developer.company-information.service.gov.uk/
2. Create a new application
3. Generate an API key
4. Add the key to your `.env` file

## API Documentation

FastAPI automatically generates API documentation. Once the server is running, you can access:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`