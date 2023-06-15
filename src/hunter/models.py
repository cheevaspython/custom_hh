import uuid, enum
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Date, Enum, Float, MetaData, Table, Column, \
    Integer, String, TIMESTAMP, ForeignKey
                                    
metadata = MetaData()


class CodeStyle(enum.Enum):
    """Основной язык кода"""
    python = 'Пайтон'
    java = 'Джава'
    js ='Джаваскрипт'
    ruby = 'Руби'
    go = 'Голанг'
    c = 'Си'
    rust = 'Раст'


hunter_site = Table(
    'hunter_site',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)

contender = Table(
    'contender',
    metadata,
    Column("id", Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)),
    Column("hunter_site_id", Integer, ForeignKey(hunter_site.c.id)),
    Column("name", String, nullable=False),
    Column("birthday", Date),
    Column("email", String, unique=True, index=True, nullable=False),
    Column("code_style", Enum(CodeStyle), default=CodeStyle.python, nullable=False),
    Column("reg_at", TIMESTAMP, default=datetime.utcnow),
    Column("about_me", String, nullable=False),
    Column("experience", Float, nullable=False),
    Column("owned_tech", String, nullable=False),
    Column("selery", Float, nullable=False),
)

hr_search = Table(
    'hr_search',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("hunter_site_id", Integer, ForeignKey(hunter_site.c.id)),
    Column("experience", Float, nullable=False),
    Column("owned_tech", String, nullable=False),
    Column("selery", Float, nullable=False),
)

employer = Table(
    'employer',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("hunter_site_id", Integer, ForeignKey(hunter_site.c.id)),
    Column("hr_search_id", Integer, ForeignKey(hr_search.c.id)),
)




