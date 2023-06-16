from fastapi import APIRouter, Depends

from sqlalchemy import insert, select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_async_session

from src.employer.models import employer
from src.employer.schemas import EmployerBaseModelIn

router = APIRouter(
    prefix="/employer",
    tags=["employer"]
)


@router.post("/create")
async def create_employer(
        employer_create: EmployerBaseModelIn,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = insert(employer).values(**employer_create.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "create"}
    

@router.delete("/delete")
async def delete_employer(
        pk: int,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = delete(employer).where(employer.c.id == pk)
    await session.delete(stmt)
    await session.commit()
    return {"status": "delete"}


@router.get("/list")
async def list_employer(
        pk: int | None = None,
        session: AsyncSession = Depends(get_async_session),
        ):
    if pk:
        stmt = select(employer).where(employer.c.id == pk)
    else:
        stmt = select(employer)
    result = await session.execute(stmt)
    return {
        "status": "success",
        "data": result.all(),
        "details": None
    }


@router.patch("/edit")
async def edit_employer(
        pk: int,
        contender: EmployerBaseModelIn,
        session: AsyncSession = Depends(get_async_session),
        ):
    stmt = update(employer).where(employer.c.id == pk).values(**contender.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "edit"}


