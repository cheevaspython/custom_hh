from fastapi import APIRouter, Depends

from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.contender.models import CodeStyle
from src.database import get_async_session

from src.hunters.models import hunter_site, hr_search
from src.hunters.schemas import HRsearchBaseModelIn, HunterSiteBaseModelIn
from src.hunters.services import hr_hunting

router = APIRouter(
    prefix="/hunters",
    tags=["hr_hunters"]
)

@router.post("/filter_contender")
async def filter(
        hh_site: int,
        hr_id: int,
        code_style: CodeStyle,
        ):
    await hr_hunting(hh_site, hr_id, code_style)
    return {"status": "filter added"}

@router.post("/create")
async def create_hunter_site(
        hunter_site_create: HunterSiteBaseModelIn,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = insert(hunter_site).values(**hunter_site_create.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "create"}
    

@router.delete("/delete")
async def delete_hunter_site(
        pk: int,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = delete(hunter_site).where(hunter_site.c.id == pk)
    await session.delete(stmt)
    await session.commit()
    return {"status": "delete"}


@router.get("/list")
async def list_hunter_site(
        pk: int | None = None,
        session: AsyncSession = Depends(get_async_session),
        ):
    if pk:
        stmt = select(hunter_site).where(hunter_site.c.id == pk)
    else:
        stmt = select(hunter_site)
    result = await session.execute(stmt)
    return {
        "status": "success",
        "data": result.all(),
        "details": None
    }


@router.patch("/edit")
async def edit_hunter_site(
        pk: int,
        hunters_data: HunterSiteBaseModelIn,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = update(hunter_site).where(hunter_site.c.id == pk).values(**hunters_data.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "edit"}


@router.post("/create")
async def create_hr(
        hr_create: HRsearchBaseModelIn,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = insert(hr_search).values(**hr_create.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "create"}
    

@router.delete("/delete")
async def delete_hr(
        pk: int,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = delete(hr_search).where(hr_search.c.id == pk)
    await session.delete(stmt)
    await session.commit()
    return {"status": "delete"}


@router.get("/list")
async def list_hr(
        pk: int | None = None,
        session: AsyncSession = Depends(get_async_session),
        ):
    if pk:
        stmt = select(hr_search).where(hr_search.c.id == pk)
    else:
        stmt = select(hr_search)
    result = await session.execute(stmt)
    return {
        "status": "success",
        "data": result.all(),
        "details": None
    }


@router.patch("/edit")
async def edit_hr(
        pk: int,
        hr_data: HunterSiteBaseModelIn,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = update(hr_search).where(hr_search.c.id == pk).values(**hr_data.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "edit"}
