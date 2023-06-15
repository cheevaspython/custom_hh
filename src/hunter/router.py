from datetime import datetime
import time

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from hunter.models import hunter_site, hr_search, employer, contender
from hunter.schemas import HRsearchBaseModel, ContenderBaseModelIn, \
    EmployerBaseModel, HunterSiteBaseModel

router = APIRouter(
    prefix="/hunter",
    tags=["hr_hunter"]
)


@router.post("/create_employer")
async def list_employer(
        contender: ContenderBaseModelIn,
        session: AsyncSession = Depends(get_async_session),
        ):
    query = employer.insert().values(
        hunter_site_id = contender.hunter_site_id,
        name = contender.name,
        birthday = contender.birthday,
        email = contender.email,
        code_style = contender.code_style,
        reg_at = datetime.now(),
        about_me = contender.about_me,
        experience = contender.experience,
        owned_tech = contender.owned_tech,
        selery = contender.selery,
    )
    
