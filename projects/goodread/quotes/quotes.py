from infra.webscraper import Webscraper
import infra.etl as etl


DB_NAME = 'quotes'
HOST_ARGS = {
            'host' : 'localhost',
            'user' : 'root',
            'password' : 'root',
            'database' : DB_NAME
            }

MRR_TABLE = DB_NAME


ws = Webscraper()
etl = etl.ETL(**HOST_ARGS)

data=[]
pages = 101
for page in range(1,pages):
    URL = f'https://www.goodreads.com/quotes?page={page}'
    print(URL)
    soup = ws.beautifuler(url=URL)

    # parsing all "quote" tag element - (response type: list)
    quotes = ws.soupParser(soup=soup, tag='div', attib='quote', all='y')

    data_page = []
    for quote in quotes:
        qoute_parse = ws.soupParser(soup=quote, tag='div', attib='quoteText', strip='text').replace('\n', '').split('―')
        qoute_text = qoute_parse[0].strip()[1:-1]
        
        try:
            author = qoute_parse[1].strip().split(',')[0]
            book = qoute_parse[1].strip().split(',')[1].strip()
        except:
            author = qoute_parse[1].strip()
            book = None

        author_img = ws.soupParser(soup=quote, tag='img', strip='src')
        likes = ws.soupParser(soup=quote, tag='a', attib='smallText', strip='text').split(' ')[0]

        row = [qoute_text, author, book, author_img, likes]
        data.append(row)
 
etl.insert_bulk(table=DB_NAME, truncate='y', data=data)    