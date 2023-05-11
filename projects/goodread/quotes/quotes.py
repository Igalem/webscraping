from infra.webscraper import Webscraper


URL = 'https://www.goodreads.com/quotes?page=1'


ws = Webscraper()
soup = ws.beautifuler(url=URL)



# def soupParser(soup, tag=None, attib=None, strip=None, all='n'):
#     if all.upper() != 'N':
#         element = soup.find_all(tag, class_= attib)
#     else:
#         element = soup.find(tag, class_= attib)

#     if strip=='text':
#         element_val = element.text.strip()
#     elif strip=='src':
#         element_val = element[strip]
#     else:
#         element_val = element

#     return element_val


# parsing all "quote" tag element - (response type: list)
quotes = ws.soupParser(soup=soup, tag='div', attib='quote', all='y')

for quote in quotes:
    try:
        qoute_parse = ws.soupParser(soup=quote, tag='div', attib='quoteText', strip='text').replace('\n', '').split('―')
        qoute_text = qoute_parse[0].strip()
        author = qoute_parse[1].strip()
        author_img = ws.soupParser(soup=quote, tag='img', strip='src')
        likes = ws.soupParser(soup=quote, tag='a', attib='smallText', strip='text').split(' ')[0]
    except:
        pass
    
    print(qoute_text)    
    print(author)
    print(author_img)
    print(likes)
    print('--------\n')
    

