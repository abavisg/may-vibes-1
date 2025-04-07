from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class NameRequest(BaseModel):
    industry: str
    keywords: List[str]
    tone: str
    audience: Optional[str] = None
    generator_type: str = "local"

class NameGenerationRequest(BaseModel):
    industry: str
    keywords: List[str]
    tone: str
    audience: Optional[str] = None

class NameGenerationResponse(BaseModel):
    names: List[str]

class DomainAvailabilityResponse(BaseModel):
    names: Dict[str, bool]
    available_count: int
    total_count: int

class NameAvailabilityInfo(BaseModel):
    domain_available: bool
    ltd_available: bool
    fully_available: bool

class BrandNameResponse(BaseModel):
    names: Dict[str, dict]
    total_count: int