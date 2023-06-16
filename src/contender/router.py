from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session

from src.contender.models import contender
from src.contender.schemas import ContenderBaseModelIn

router = APIRouter(
    prefix="/contender",
    tags=["contender"]
)


@router.post("/create")
async def create_contender(
        contender_create: ContenderBaseModelIn,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = insert(contender).values(**contender_create.dict(), reg_at=datetime.now())
    await session.execute(stmt)
    await session.commit()
    return {"status": "create"}
    

@router.delete("/delete")
async def delete_contender(
        pk: int,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = delete(contender).where(contender.c.id == pk)
    await session.delete(stmt)
    await session.commit()
    return {"status": "delete"}


@router.get("/list")
async def list_contender(
        pk: int | None = None,
        session: AsyncSession = Depends(get_async_session),
        ):
    try:
        if pk:
            stmt = select(contender).where(contender.c.id == pk)
        else:
            stmt = select(contender)
        result = await session.execute(stmt)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.patch("/edit")
async def edit_contender(
        pk: int,
        contender_edit: ContenderBaseModelIn,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = update(contender).where(contender.c.id == pk).values(**contender_edit.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "edit"}


