# -*- coding:utf-8 -*-
from utlis.utlis import SpiderVarible
import requests
import re


class NeihanSpider:
    def __init__(self):
        self.page = 1
        self.url = 'http://www.neihan8.com/article/list_5_'
        self.headers = {'User-Agent': SpiderVarible().get_random_user_agent()}
        self.proxy = {'http': 'http://' + SpiderVarible().get_random_proxy_addr()}
        # 用于爬取div中内容
        self.pattern_page = re.compile(r'<div class="f18 mb20">(.*?)</div>', re.S)
        # 用于爬取实用内容
        self.pattern_result = re.compile('<.*?>|&.*;|\s|' + u'\u3000'.encode('utf-8'))
        self.temp = False
        self.input_key = ''

    def write_file(self, info_list):
        """
        写入文件
        :return:
        """
        with open('neihan.txt', 'a')as f:
            f.write("第" + str(self.page) + '页:\n')
            for index, info_list in enumerate(info_list):
                print '[INFO]正在写入文件中...'
                content = str(index + 1) + '. ' + self.pattern_result.sub('', info_list)
                content += '\n'
                f.write(content)
            f.write('\n')

    def load_html(self, page):
        """
        获取html文件内容
        :return:
        """
        self.url = 'http://www.neihan8.com/article/list_5_' + str(page) + '.html'
        print '[INFO]正在请求网址%s' % self.url
        response = requests.get(self.url, headers=self.headers, proxies=self.proxy).content.decode('gbk').encode(
            'utf-8')
        return response

    def regex_step(self, content):
        """
        匹配正则
        :return: 匹配后的结果列表
        """
        info_list = re.findall(self.pattern_page, content)
        return info_list

    def main(self):
        while True:
            if self.input_key == 'q':
                break
            # 获取网页内容
            response = self.load_html(self.page)
            # 获取列表
            info_list = self.regex_step(response)
            # 写入文件
            self.write_file(info_list)

            self.page += 1
            self.input_key = raw_input('只有输入q退出循环:')


if __name__ == '__main__':
    NeihanSpider().main()
