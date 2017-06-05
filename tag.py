# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 19:16:37 2017

@author: vigh
"""

#requests+beautifulsuop 爬取豆瓣图书

import requests
import re
from bs4 import BeautifulSoup
import csv
import time

def get_html(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER'}
    response = requests.get(url,headers=headers)
    html = response.text
    return html


def get_books(url):
    max_span=125
    i=0
    csvfile = open('dygw.csv', 'w', newline='')  # , encoding='utf-8'  
    writer = csv.writer(csvfile)  
    writer.writerow(['书名', '出版信息','分数', '评价人数',  '链接','简介' ])
    for page in range(0, int(max_span)):
            time.sleep(1)
            page_url = url + '?start=' +str(i)+ str("&type=T")
            i=i+1
            
            html = get_html(page_url)
            
            soup=BeautifulSoup(html,"html.parser")
            
            a = soup.find("ul", {"class": "subject-list"})
            b=a.find("li",{"class": "subject-item"})
            
            bn=b.find("h2").find("a")['title'].encode('gbk', 'ignore').decode('gbk')
            print(bn)
            
            bi=b.find("div",{"class": "pub"}).string.encode('gbk', 'ignore').decode('gbk')
                               
            bf=b.find("span", class_="rating_nums")
            if bf==None:
                bf="无"
            else:
                bf=b.find("span", class_="rating_nums").string.encode('gbk', 'ignore').decode('gbk')
            
            bp=b.find("span" ,class_="pl").string.encode('gbk', 'ignore').decode('gbk')
                     
            bs=b.find("p")
            if bs==None:
                bs="无简介"
            else:
                bs=b.find("p").get_text().encode('gbk', 'ignore').decode('gbk')
                
            bl=b.a['href']
            
            writer.writerow([bn,bi,bf,bp,bl,bs])
    csvfile.close()  
    
    
  
    
    
              
              
if __name__ == '__main__':

    url = 'https://book.douban.com/tag/东野圭吾'
    get_books(url)
