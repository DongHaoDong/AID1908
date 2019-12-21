# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import requests
import json
from ..items import TencentItem
from scrapy_redis.spiders import RedisSpider

class TencentSpider(RedisSpider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566266592644&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1566266695175&postId={}&language=zh-cn'
    headers = { 'User-Agent':'Mozilla/5.0' }
    keyword = input('请输入职位类别:')
    keyword = parse.quote(keyword)
    # 第一页的URL地址
    # start_urls = [ one_url.format(keyword,1) ]
    redis_key = 'tencent:spider'
    # 把所有页的URL地址交给调度器入队列
    def parse(self,response):
        total = self.get_total()
        # 生成一级页面所有页的URL地址,交给调度器
        for index in range(1,50):
            url = self.one_url.format(self.keyword,index)
            yield scrapy.Request(
                url=url,
                callback=self.parse_one_page
            )

    # 获取总页数
    def get_total(self):
        url = self.one_url.format(self.keyword, 1)
        html = requests.get(url=url, headers=self.headers).json()
        count = html['Data']['Count']
        if count % 10 == 0:
            total = count // 10
        else:
            total = (count // 10) + 1

        return total

    # 一级页面:提取postid
    def parse_one_page(self,response):
        html = json.loads(response.text)
        for one in html['Data']['Posts']:
            # postId ,two_url
            postid = one['PostId']
            url = self.two_url.format(postid)
            yield scrapy.Request(
                url=url,
                callback=self.parse_two_page
            )

    # 解析二级页面
    def parse_two_page(self,response):
        item = TencentItem()
        html = json.loads(response.text)
        # 名称+类别+职责+要求+地址+时间
        item['job_name'] = html['Data']['RecruitPostName']
        item['job_type'] = html['Data']['CategoryName']
        item['job_duty'] = html['Data']['Responsibility']
        item['job_require'] = html['Data']['Requirement']
        item['job_address'] = html['Data']['LocationName']
        item['job_time'] = html['Data']['LastUpdateTime']

        yield item


