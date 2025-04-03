from typing import List, Optional
from pydantic import BaseModel

class NameRequest(BaseModel):
    industry: str
    keywords: List[str]
    tone: str
    audience: Optional[str] = None

class NameGenerationRequest(BaseModel):
    industry: str
    keywords: List[str]
    tone: str
    audience: Optional[str] = None

class NameGenerationResponse(BaseModel):
    names: List[str]