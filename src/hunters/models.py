from sqlalchemy import Float, MetaData, Table, Column, \
    Integer, String, ForeignKey
                                    
metadata = MetaData()


hunter_site = Table(
    'hunter_site',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

hr_search = Table(
    'hr_search',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, unique=True, index=True, nullable=False),
    Column("hunter_site_id", Integer, ForeignKey(hunter_site.c.id)),
    Column("experience", Float, nullable=False),
    Column("owned_tech", String, nullable=False),
    Column("selery", Float, nullable=False),
)
