from pydantic import BaseModel


class EmployerBaseModelIn(BaseModel): 
    name: str
    hunter_site_id: int
    hr_search_id: int
