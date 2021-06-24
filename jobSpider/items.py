# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field() #岗位名称
    salary = scrapy.Field() #薪酬范围
    job_location = scrapy.Field()   #位置
    job_experience = scrapy.Field() #经验
    job_education = scrapy.Field()  #教育程度
    job_type = scrapy.Field()   #工作类型
    company = scrapy.Field()    #公司
    publish_time = scrapy.Field() #发布时间
    job_advantage = scrapy.Field() #优势
    job_detail = scrapy.Field() #职位描述
    source = scrapy.Field() #1:拉钩 2：boss
    detail_url = scrapy.Field() #详情页链接