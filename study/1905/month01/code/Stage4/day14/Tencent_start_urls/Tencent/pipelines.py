class TencentPipeline(object):
    def process_item(self, item, spider):
        print(dict(item))
        return item

import pymysql
from .settings import *

class TencentMysqlPipeline(object):
    def open_spider(self,spider):
        self.db = pymysql.connect(
          host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            charset=CHARSET
        )
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins='insert into tencenttab values(%s,%s,%s,%s,%s,%s)'
        L = [
            item['job_name'],
            item['job_type'],
            item['job_duty'],
            item['job_require'],
            item['job_address'],
            item['job_time']
        ]
        self.cursor.execute(ins,L)
        self.db.commit()

        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()