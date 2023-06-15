from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.hunter.models import CodeStyle


class ContenderBaseModelIn(BaseModel):
    hunter_site_id: int
    name: str
    email: str
    code_style: CodeStyle
    birthday: datetime
    reg_at: datetime
    about_me: str
    experience: float
    owned_tech: str
    selery: float

    # class Config:
    #     orm_mode = True


class HunterSiteBaseModel(BaseModel):
    id: int
    name: str


class EmployerBaseModel(BaseModel): 
    id: int
    name: str
    hunter_site_id: int
    hr_search_id: int


class HRsearchBaseModel(BaseModel): 
    id: int
    name: str
    hunter_site_id: int
    code_style: Optional[CodeStyle]
    experience: float
    owned_tech: str
    selery: float





