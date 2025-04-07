from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import List, Optional, Dict
import uvicorn
from agents.agent_manager import AgentManager
from agents.brand_name_agent import BrandNameAgent
from agents.name_generator import NameGeneratorAgent
from agents.domain_checker_agent import DomainCheckerAgent
from agents.ltd_checker import LTDCheckerAgent
from models.schemas import (
    NameRequest, 
    DomainAvailabilityResponse, 
    BrandNameResponse
)
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

@app.get("/")
async def read_root():
    return FileResponse(os.path.join(frontend_static_dir, "index.html"))

@app.post("/generate-brand-names")
async def generate_brand_names(request: NameRequest):
    """
    Generate brand names without checking availability
    """
    try:
        brand_name_agent = BrandNameAgent()
        # Use the brand name agent to generate names only
        result = brand_name_agent.execute({
            "industry": request.industry,
            "keywords": request.keywords,
            "tone": request.tone,
            "audience": request.audience,
            "generator_type": request.generator_type
        })
        
        # Calculate total count of names
        total_count = len(result.get("names", {}))
        
        return BrandNameResponse(
            names=result.get("names", {}),
            total_count=total_count
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/agents")
async def list_agents():
    """
    List all available agents
    """
    try:
        agent_manager = AgentManager()
        return {"agents": agent_manager.list_agents()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/check-domain")
async def check_domain(request: Dict[str, str]):
    """
    Check domain availability for a single name
    """
    try:
        name = request.get("name")
        if not name:
            raise HTTPException(status_code=400, detail="Name is required")
        
        domain_checker = DomainCheckerAgent()
        result = domain_checker.execute({"names": [name]})
        
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
            
        return result["domain_results"].get(name, {})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/check-ltd")
async def check_ltd(request: Dict[str, str]):
    """
    Check LTD availability for a single name
    """
    try:
        name = request.get("name")
        if not name:
            raise HTTPException(status_code=400, detail="Name is required")
        
        ltd_checker = LTDCheckerAgent()
        result = ltd_checker.execute({"names": [name]})
        
        if "error" in result:
            raise HTTPException(status_code=500, detail=result["error"])
            
        return result["ltd_results"].get(name, {})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        ssl_keyfile="/Users/giorgos/Workspace/Projects/ssl-certs/cursor/key.pem",
        ssl_certfile="/Users/giorgos/Workspace/Projects/ssl-certs/cursor/cert.pem",
        reload=True
    )