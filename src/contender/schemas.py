from datetime import datetime

from pydantic import BaseModel

from src.contender.models import CodeStyle


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

    class Config:
        orm_mode = True
