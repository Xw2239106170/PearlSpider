from selenium import webdriver
from lxml import etree
from selenium.webdriver.edge.options import Options


bro = webdriver.Edge()
bro.get("https://www.pearvideo.com/popular")

#显示等待
bro.implicitly_wait(10)

#获取页面原源码
page_text = bro.page_source
tree = etree.HTML(page_text)
fp = open("梨视频.html","w",encoding="utf-8")
fp.write(page_text)

list_li = tree.xpath("//*[@id='popularList']/li")
for li in list_li:
    video_url = "https://www.pearvideo.com/"+li.xpath("./a/@href")[0]
    bro.get(video_url)
    page = bro.page_source

    tree1 = etree.HTML(page)
    video_data = tree1.xpath("//*[@id='JprismPlayer']/video/@src")
    video_name = tree1.xpath("//*[@id='detailsbd']/div[1]/div[2]/div/div[1]/h1/text()")[0]
    print(video_data,video_name)
    with open("视频.txt", "a", encoding="utf-8") as f:
        print(video_data, video_name, file=f)





