from sqlalchemy import MetaData, Table, Column, \
    Integer, String, ForeignKey

from src.hunters.models import hunter_site, hr_search
                                    
metadata = MetaData()


employer = Table(
    'employer',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("hunter_site_id", Integer, ForeignKey(hunter_site.c.id)),
    Column("hr_search_id", Integer, ForeignKey(hr_search.c.id)),
)




