# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class JobspiderPipeline:
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(host='localhost',port=27017)
        self.db = self.conn['recruit_requirement']
        self.recruit_requirement_detail	=self.db.recruit_requirement_detail
        
    def process_item(self, item, spider):
        self.recruit_requirement_detail.insert(
            {
                "job_name":item['job_name'],
                "salary":item['salary'],
                "job_location":item['job_location'],
                "job_experience":item['job_experience'],
                "job_education":item['job_education'],
                "job_type":item['job_type'],
                "company":item['company'],
                "publish_time":item['publish_time'],
                "job_advantage":item['job_advantage'],
                "job_detail":item['job_detail'],
                "detail_url":item['detail_url']
            }
        )
    
    def close_spider(self,spider):
        self.conn.close()
