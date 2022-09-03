!pip install requests-html

from requests_html import HTMLSession
session = HTMLSession()

def bangla_kobita_scraping(poem_name):
    url = f"https://www.bangla-kobita.com/nazrulislam/{poem_name}/"
    r = session.get(url)
    bangla_kobita = r.html.find("body > div.container > div.row.body-content > div.col-md-8")[0].text
    
    bangla_kobita_lst = bangla_kobita.split('\n')
    poem_name = bangla_kobita_lst[1]
    author = bangla_kobita_lst[2]
    poem_des = bangla_kobita_lst[3:14]
    poem_type = bangla_kobita_lst[16]
    poem_catagory = bangla_kobita_lst[19]
    commenter = bangla_kobita_lst[36:43:3]
    comment = bangla_kobita_lst[37:44:3]
    
    with open("banglaKobita.txt", "w", encoding="utf-8") as f:
        f.write("poem_name, author, poem_des, poem_type, poem_catagory, commenter,comment\n")
        f.write(f"{poem_name}, {author}")
        f.write("\n")
        for i in poem_des:
            f.write(f"{i}")
            f.write('\n')
        f.write(f"{poem_type},\n{poem_catagory}\n")
        for i, j in zip(commenter,comment):
            f.write(f"{i}, {j}")
            f.write('\n')

poem_name = ["akorun-piya"]

for i in poem_name:
    bangla_kobita_scraping(i)