import requests
from bs4 import BeautifulSoup
import lxml
import json

def get_first_news():
    url = 'https://www.securitylab.ru/news/'
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    req = requests.get(url=url, headers=headers)
    soap = BeautifulSoup(req.text,'lxml')

    article_cards = soap.find_all('a',class_= 'article-card inline-card')

    news_dict = {}

    for articles in article_cards:
        article_type = articles.find('h2',class_ = 'article-card-title').text.strip()
        article_details = articles.find('p').text
        article_url = f"https://www.securitylab.ru{articles.get('href')}"
        article_data_time = articles.find('time').text

        article_id = article_url.split('/')[-1][:-4]
        
        news_dict[article_id] = {
            'time:' : article_data_time,
            'title:' : article_type,
            'url:' : article_url,
            'details:' : article_details
        }

    with open('news_dict.json', 'w', encoding ='utf8') as file:
        json.dump(news_dict,file,indent=4,ensure_ascii=False)

# def news_check_update():
    # with open("news_dict.json") as file:
    #     news_dict = json.load(file)

    # url = 'https://www.securitylab.ru/news/'
    # headers = {
    #     'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    # }

    

    # req = requests.get(url=url, headers=headers)
    # soap = BeautifulSoup(req.text,'lxml')

    # article_cards = soap.find_all('a',class_= 'article-card inline-card')

    # fresh_dict = {}

    # for articles in article_cards:
    #     article_id = article_url.split('/')[-1][:-4]
    #     article_url = f"https://www.securitylab.ru{articles.get('href')}"

    #     if articles in news_dict:
    #         continue
    #     else:
    #         article_type = articles.find('h2',class_ = 'article-card-title').text.strip()
    #         article_details = articles.find('p').text
    #         article_data_time = articles.find('time').text

       
        
    #         news_dict[article_id] = {
    #             'time:' : article_data_time,
    #             'title:' : article_type,
    #             'url:' : article_url,
    #             'details:' : article_details
    #         }

    #         fresh_dict[article_id] = {
    #             'time:' : article_data_time,
    #             'title:' : article_type,
    #             'url:' : article_url,
    #             'details:' : article_details
    #         }
    
    # with open("news_dict.json", "w",encoding='utf-8') as file:
    #     json.dump(news_dict, file, indent=4, ensure_ascii=False)

    # return fresh_dict  


def main():
    get_first_news()
    #print(news_check_update())
    


if  __name__ == '__main__':
    main()
