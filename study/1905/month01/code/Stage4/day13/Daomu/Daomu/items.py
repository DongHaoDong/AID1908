# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 1. 一级页面标题 - 创建文件夹需要
    title = scrapy.Field()
    # 2. 二级页面标题 - 创建文件需要
    name = scrapy.Field()
    # 3. 小说内容
    content = scrapy.Field()
