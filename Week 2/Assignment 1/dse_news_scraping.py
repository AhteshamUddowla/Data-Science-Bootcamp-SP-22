!pip install requests-html

from requests_html import HTMLSession
session = HTMLSession()

def dse_news_scraping(year):
    url = f"https://dsebd.org/old_news.php?startDate={year}-01-01&endDate={year}-12-30&criteria=4&archive=news"
    r=session.get(url)
    dse_news = r.html.find(".table-news")[0].text
    
    dse_news_lst = dse_news.split('\n')
    trading_code = dse_news_lst[1::8]
    news_title = dse_news_lst[3::8]
    news = dse_news_lst[5::8]
    post_date = dse_news_lst[7::8]
    
    trading_code, news_title, news, post_date = trading_code[:-4], news_title[:-4], news[:-4], post_date[:-3]
        
    with open(f"{year}.txt", "w", encoding="utf-8") as f:
        f.write("No, Trading_code, News_title, News, Post_date\n")
        for i, t, nt, n, p in zip(range(1, len(trading_code)+1), trading_code, news_title, news, post_date):
            f.write(f"{i}, {t}, {nt}, {n}, {p}")
            f.write("\n")

dse_news_scraping(2020)