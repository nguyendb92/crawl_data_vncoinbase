from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from scrapy.conf import settings


DeclarativeBase = declarative_base()


def db_connect():
    db_url = URL(**settings['DATABASE'])
    return create_engine(db_url)

def create_coin_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class CoinItem(DeclarativeBase):
    __tablename__ = "coin"
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    symbol = Column('symbol', String)
    market_cap = Column('market_cap', String)
    price = Column('price', String)
    ciculating_supply = Column('ciculating_supply', String)
    volume = Column('volume', String)
    change = Column('change', String)

