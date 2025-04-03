# Brand Name Generator API

A FastAPI application that generates creative brand names using OpenAI's GPT models.

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
4. Create a `.env` file in the backend directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
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
    "audience": "string" (optional)
}
```

Response:
```json
{
    "names": ["string"]
}
```

### GET /health

Health check endpoint to verify the API is running.

## API Documentation

FastAPI automatically generates API documentation. Once the server is running, you can access:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`