from fastapi import Depends

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

from src.hunters.models import hr_search
from src.contender.models import CodeStyle, contender
from src.tasks import send_invite_to_meet


async def hr_hunting(
        site_pk: int,
        hr_pk: int,
        code_style: CodeStyle,
        session: AsyncSession = Depends(get_async_session),
        ):
    """search members for hr filter, send invite"""
    cur_hr = select(hr_search).where(hr_search.c.id == hr_pk)
    cur_contenders = select(contender).where(
        contender.c.hunter_site_id == site_pk,
        contender.c.code_style == code_style,
        contender.c.selery < cur_hr.c.selery,
        contender.c.experience > cur_hr.c.experience,
        contender.c.owned_tech == cur_hr.c.owned_tech
        ).order_by(contender.c.selery)

    result = await session.execute(cur_contenders)
    hr = await session.execute(cur_hr)
    send_invite_to_meet([cond.email for cond in result], [c_hr.email for c_hr in hr][0])

