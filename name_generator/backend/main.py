from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from agents.name_generator import name_generator_factory
import os
import logging

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:8080"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get the absolute path to the frontend static directory
frontend_static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend/static"))

# Mount static files
app.mount("/static", StaticFiles(directory=frontend_static_dir), name="static")

class NameRequest(BaseModel):
    industry: str
    keywords: List[str]
    tone: str
    audience: Optional[str] = None
    generator_type: str = "local"  # Changed from model_type to generator_type

@app.get("/")
async def read_root():
    return FileResponse(os.path.join(frontend_static_dir, "index.html"))

@app.post("/generate-names")
async def generate_names(request: NameRequest):
    try:
        # Create the appropriate name generator
        generator = name_generator_factory.create_generator(request.generator_type)
        
        # Generate names
        names = generator.generate_names(
            request.industry,
            request.keywords,
            request.tone,
            request.audience
        )
        
        logging.info(f"Generated names length is 100?: {len(names) == 100}")
    
        # Ensure we have exactly 100 names
        while len(names) < 100:
            # If we got fewer than 100 names, make another call to get more
            additional_names = generator.generate_names(request.industry, request.keywords, request.tone, request.audience)
            names.extend(additional_names[:100 - len(names)])  # Add only what's needed
        
        logging.info(f"Generated names FINAL LENGTH: {len(names)}")
        return {"names": names}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        ssl_keyfile="ssl/key.pem",
        ssl_certfile="ssl/cert.pem",
        reload=True
    )