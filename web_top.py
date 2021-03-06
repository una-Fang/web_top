# https://s.weibo.com/top/summary/
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    news = []
    hot_url = 'https://s.weibo.com/top/summary/'
    # 热搜榜链接
    r = requests.get(hot_url)
    soup = BeautifulSoup(r.text, 'lxml')

    urls_titles = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > a')
    hotness = soup.select('#pl_top_realtimehot > table > tbody > tr > td.td-02 > span')

    for i in range(len(urls_titles)-1):
        hot_news = {}
        hot_news['title'] = urls_titles[i+1].get_text()
        hot_news['url'] = "https://s.weibo.com"+urls_titles[i]['href']
        hot_news['hotness'] = hotness[i].get_text()
        news.append(hot_news)
    
    print(news)

    import datetime
    today = datetime.date.today()
    f = open('./热搜榜-%s.csv'%(today), 'w', encoding='utf-8')
    for i in news:
        f.write(i['title'] + ',' + i['url'] + ','+ i['hotness'] + 'n')