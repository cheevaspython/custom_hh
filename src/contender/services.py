# from sqlalchemy import select
# from database import get_async_session
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from fastapi import Depends
# from contender.models import contender


# async def get_all_contenders(
#         pk: int,
#         session: AsyncSession = Depends(get_async_session),
#     ) -> list:
#
#     result = await session.execute(select(City).order_by(City.population.desc()).limit(20))
#     return result.scalars().all()
#
#
# def add_citysession(session: AsyncSession = Depends(get_async_session), name: str, population: int):
#     new_city = City(name=name, population=population)
#     session.add(new_city)
#     return new_city
