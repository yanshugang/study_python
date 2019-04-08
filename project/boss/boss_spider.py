# -*- coding: utf-8 -*-

# @Author: ysg
# @Contact: yanshugang11@163.com
# @Time: 2019/3/13 下午1:44

"""
多线程爬取boss直聘
"""
import time

import requests
import threading
from queue import Queue

from lxml import etree


# TODO: 添加自动重试机制、ip代理机制、请求头代理机制。
def get_request(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
    }
    response = requests.get(url, headers=headers).content
    html = etree.HTML(response)
    return html


def get_job_list(job_title, q):
    """
    抓取职位列表页
    """

    def parse_job_list(elem):
        # parse: 职位id、职位名称、薪资范围、工作地点、经验要求、学历要求、公司名称、公司所属行业、融资阶段、公司规模
        job_id = elem.xpath("div[@class='info-primary']/h3/a/@data-jid")[0]  # 职位id
        job_name = elem.xpath("div[@class='info-primary']/h3/a/div[@class='job-title']/text()")[0]  # 职位名称
        money = elem.xpath("div[@class='info-primary']/h3/a/span/text()")[0]  # 薪资范围
        working_info = elem.xpath("div[@class='info-primary']/p/text()")  # 工作地点、经验要求、学历要求
        company_name = elem.xpath("div[@class='info-company']/div/h3/a/text()")[0]  # 公司名称
        company_info = elem.xpath("div[@class='info-company']/div/p/text()")  # 公司所属行业、融资阶段、公司规模

        return vars()

    base_url = "https://www.zhipin.com/c101010100/?query={job_title}&page={page}"
    for i in range(10):  # boss直聘只展示十页。
        url = base_url.format(job_title=job_title, page=i + 1)
        html = get_request(url)

        job_list = html.xpath("//ul/li/div[@class='job-primary']")
        for elem in job_list:
            item = parse_job_list(elem)
            item.pop("elem")
            # print(item)
            q.put(item)

        print("page-{page} crawl success!".format(page=i + 1))
        print("current queue size: {q_size}".format(q_size=q.qsize()))
        time.sleep(20)


def get_job_info(q):
    """
    抓取职位详情页
    """

    def parse_job_info(html):
        elem_list = html.xpath("//div[@class='detail-content']/div[1]//text()")
        # 清洗数据
        job_info = "".join(elem_list).replace("\n", "").replace("\t", "").strip()
        return job_info

    while True:
        if q.qsize() == 0:
            time.sleep(3)
        else:
            item = q.get()
            q.task_done()  # TODO: task_done怎么使用
            job_id = item.get("job_id")
            url = "https://www.zhipin.com/job_detail/{job_id}.html".format(job_id=job_id)
            html = get_request(url)
            job_info = parse_job_info(html)
            item["job_info"] = job_info
            print(item)


def run(job_title):
    q_job_url = Queue(maxsize=100)
    thread_job_list = threading.Thread(target=get_job_list, args=(job_title, q_job_url))

    for i in range(10):
        thread_job_info = threading.Thread(target=get_job_info, args=(q_job_url,))
        thread_job_info.start()

    thread_job_list.start()

    q_job_url.join()


def main():
    job_title = "大数据开发工程师"
    run(job_title)


def test():
    job_title = "大数据开发"
    q = Queue()
    get_job_list(job_title, q)


if __name__ == '__main__':
    main()
    # test()
