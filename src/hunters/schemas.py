from typing import Optional

from pydantic import BaseModel

from src.contender.models import CodeStyle


class HunterSiteBaseModelIn(BaseModel):
    name: str


class HRsearchBaseModelIn(BaseModel): 
    name: str
    hunter_site_id: int
    code_style: Optional[CodeStyle]
    experience: float
    owned_tech: str
    selery: float




