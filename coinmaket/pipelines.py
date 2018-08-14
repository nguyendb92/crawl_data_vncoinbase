# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import psycopg2
# from scrapy.conf import settings
# 
# 
# class CoinmaketPipeline(object):
#     def __init__(self):
#         self.connection = psycopg2.connect(
#             host=settings["HOST"],
#             database=settings["DB_NAME"],
#             user=settings["USER"],
#             password=settings['PASSWORD']
#             )
#         self.cursor = self.connection.cursor()
# 
#     def process_item(self, item, spider):
#         try:
#             self.cursor.execute(
#                 """CREATE TABLE IF NOT EXISTS coin_table (name varchar(200),
#              symbol varchar(200), market_cap varchar(200), price varchar(200),
#              ciculating_supply varchar(200), volume varchar(200),
#              change boolean);""")
# 
#             self.connection.commit()
#         except Exception as e:
#             print(e)
#         try:
#             self.cursor.execute(
#                 """INSERT INTO coin_table(name, symbol,
#                 market_cap, price, ciculating_supply, volume, change)
#                 VALUES
#                 (%s, %s, %s, %s, %s,%s,%s);""",
#                 (item["name"], item["symbol"], item["market_cap"],
#                  item["price"], item["ciculating_supply"],
#                  item["volume"], item["change"])
#                 )
# 
#             self.connection.commit()
#         except psycopg2.DatabaseError as e:
#             print("Error: {}".format(e))
# 
#         return item
from sqlalchemy.orm import sessionmaker
from .models import CoinItem, db_connect, create_coin_table


class CoinMarketPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_coin_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        obj = CoinItem(**item)
        try:
            session.add(obj)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        return item
