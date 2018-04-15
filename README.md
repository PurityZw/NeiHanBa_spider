# NeiHanBa_spider
爬取网址:
http://www.neihan8.com/article/list_5_1.html

```
# 用于爬取div中内容
self.pattern_page = re.compile(r'<div class="f18 mb20">(.*?)</div>', re.S)
# 用于爬取实用内容
self.pattern_result = re.compile('<.*?>|&.*;|\s|' + u'\u3000'.encode('utf-8'))
```