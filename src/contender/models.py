import enum

from datetime import datetime

from sqlalchemy import Date, Enum, Float, MetaData, Table, Column, \
    Integer, String, TIMESTAMP, ForeignKey

from src.hunters.models import hunter_site

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


contender = Table(
    'contender',
    metadata,
    Column("id", Integer, primary_key=True),
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
