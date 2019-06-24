import requests
import re


# 获取网页源代码
def get_html_content(url):
    return requests.get(url).text


# 解析获取的源代码，提取有用的内容
def parse_html(html_con):
    # 正则进行解析
    r = re.compile(r'<p class="name"><.*?>(?P<title>.*?)</a></p>' +
                   '.*?<p.*?>(?P<actor>.*?)</p>' +
                   '.*?<a href="(?P<url>.*?)" title=".*?>', re.S)
    obj = r.finditer(html_con)
    for i in obj:
        info = {
            'title': i.group('title'),
            'actor': i.group('actor').strip(),
            'movie_url': 'https://maoyan.com' + i.group('url')

        }
        yield info


def main(nums):
    url = 'https://maoyan.com/board/4?offset=%s' % nums

    get_html = get_html_content(url)
    for i in parse_html(get_html):
        print(i)


if __name__ == '__main__':
    for i in range(0, 101, 10):
        main(i)

