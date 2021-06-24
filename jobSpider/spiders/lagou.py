import jobSpider
from time import sleep
import scrapy
from scrapy import item
from selenium import webdriver
from ..items import JobspiderItem
import random

class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    keyword = '爬虫'    #关键词
    filter = '/p-city_213?px=default#filterBox' #筛选条件
    start_urls = ['https://www.lagou.com/jobs/list_'+keyword+filter]

    def __init__(self):
        super(LagouSpider,self).__init__()
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path='E:\\CodeProjects\PythonScrapypractice\chromedriver.exe',chrome_options=options)
        
    def close(self,spider):
        self.driver.close()
        print('close Spider')
         
    def parse(self, response):
        links = response.xpath('//a[@class="position_link"]/@href').extract() #获取详情页链接
        #for link in links:
            #yield scrapy.Request(link,callback=self.parse_detail,meta={'detail_url':link})
        link  = random.choice(links)
        yield scrapy.Request(link,callback=self.parse_detail,meta={'detail_url':link}) #详情页回调
 
    def parse_detail(self, response):
        job_name = response.xpath('//span[@class="position-head-wrap-position-name"]/text()').extract_first()
        job_salary = response.xpath('//span[@class="salary"]/text()').extract_first()

        #地址
        job_city = response.xpath('//div[@class="work_addr"]/a[1]/text()').extract_first()
        job_cityarea = response.xpath('//div[@class="work_addr"]/a[2]/text()').extract_first()
        job_citydistrict = response.xpath('//div[@class="work_addr"]/a[3]/text()').extract_first()
        job_location = job_city+job_cityarea
        #job_hebing = job_city+job_cityarea+job_citydistrict
        job_experience=response.xpath('//dd[@class="job_request"]/h3/span[2]/text()').extract_first().strip('/')
        job_education=response.xpath('//dd[@class="job_request"]/h3/span[3]/text()').extract_first().strip('/')
        job_type=response.xpath('//dd[@class="job_request"]/h3/span[4]/text()').extract_first().strip()
        company=response.xpath('//em[@class="fl-cn"]//text()').extract_first().strip()
        publish_time=response.xpath('//p[@class="publish_time"]//text()').extract()[2].strip()
        job_advantage=response.xpath('//dd[@class="job-advantage"]/p/text()').extract_first()
        job_details=response.xpath('//div[@class="job-detail"]/text()').extract()
        job_detail = ''.join(job_details).strip()
        detail_url = response.meta['detail_url']
        #print('职位:'+job_name)
        #print('薪水:'+job_salary)
        #print(job_location)
        #print('经验:'+job_experience)
        #print('教育:'+job_education)
        #print('类型:'+job_type)
        #print('公司:'+company)
        #print('发布时间:'+publish_time)
        #print('优势:'+job_advantage)
        #print('描述:'+job_detail)
        item = JobspiderItem()
        item['job_name']=job_name
        item['salary']=job_salary
        item['job_location']=job_location
        item['job_experience']=job_experience
        item['job_education']=job_education
        item['job_type']=job_type
        item['company']=company
        item['publish_time']=publish_time
        item['job_advantage']=job_advantage
        item['job_detail']= job_detail
        item['detail_url']=detail_url
        print(item)
        yield item
