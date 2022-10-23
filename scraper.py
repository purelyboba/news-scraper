from requests_html import HTMLSession

session = HTMLSession()

def getArticles(url):
    r = session.get(url)
    r.html.render(sleep=1, scrolldown=0)
    articles = r.html.find('article')
    articleList = []
    for item in articles:
        try:
            newsitem = item.find('h3', first=True)
            newsArticle = {
            'title' : newsitem.text,
            'link'  : newsitem.absolute_links
            }
            articleList.append(newsArticle)
        except:
            pass
    return articleList

def getArticleText(url):
    r = session.get(url)
    r.html.render(sleep=1, scrolldown=0)
    article = r.html.find('article', first=True)
    try:
        text = article.text
        return(text)
    except:
        pass

def main():
    articleList = getArticles('https://news.google.com/home?hl=en-US&gl=US&ceid=US%3Aen')

    print(articleList[0])

    url = str(articleList[0]['link'])[2:-2]
    content = getArticleText(url)
    print(content)

    file = open('article.txt', 'w')
    file.write(content)

if __name__ == '__main__':
    main()