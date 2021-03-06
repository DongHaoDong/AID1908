from urllib import parse

import requests
from lxml import etree
import time
import random


class TiebaImageSpider(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?'
        self.headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

    # 功能函数1:获取html
    def get_html(self,url,params={}):
        res = requests.get(url=url,params=params,headers=self.headers)
        html = res.content
        return html

    # 功能函数2:解析
    def xpath_func(self,html,xpath_bds):
        parse_obj = etree.HTML(html)
        r_list = parse_obj.xpath(xpath_bds)
        return r_list

    # 做事情
    def parse_html(self,url,params):
        # 1. 提取帖子链接
        one_html = self.get_html(url,params).decode()
        xpath_bds = '//li[@class=" j_thread_list clearfix"]//a[@class="j_th_tit "]/@href'
        # tlink_list: ['/html/xxx','','']
        tlink_list = self.xpath_func(one_html,xpath_bds)
        print(tlink_list)
        # 2. for遍历
        for tlink in tlink_list:
            tlink = 'http://tieba.baidu.com' + tlink
            # 对1个帖子链接做完所有事情
            # 向帖子发请求+提取图片链接+向图片链接发请求+保存图片
            self.get_image(tlink)

    # 向帖子发请求+提取图片链接+向图片链接发请求+保存图片
    def get_image(self,tlink):
        html = self.get_html(tlink).decode()
        xpath_bds = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
        image_link_list = self.xpath_func(html,xpath_bds)
        print(image_link_list)
        for img_link in image_link_list:
            # 保存图片
            self.save_image(img_link)

    # 保存图片
    def save_image(self,img_link):
        html = self.get_html(img_link)
        filename = img_link[-10:]
        with open(filename,'wb') as f:
            f.write(html)
        print(filename,'下载成功')

    # 入口函数
    def run(self):
        name = input("请输入贴吧名:")
        start = int(input('起始页:'))
        end = int(input("终止页:"))
        for page in range(start,end+1):
            pn = (page-1)*50
            params = {
                'kw':name,
                'pn':str(pn)
            }
            self.parse_html(self.url,params)

if __name__ == "__main__":
    spider = TiebaImageSpider()
    spider.run()
