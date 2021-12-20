import requests
import csv

print('---- WEB SCRAPING PRODUCT ----')
print('----- FROM WEB BUKALAPAK -----')
print('------ by Asep Sopiyan ------')


keywords = input('\ninput keywords : ')
rangepage = input('input range page : ')
tokens = input('input Enter the latest token : ')

keywords = str(keywords)
rangepage = int(rangepage)
tokens = str(tokens)

print('\n--------- RESULT DATA ---------')

datas = []
url = 'https://api.bukalapak.com/multistrategy-products'
count = 0

for rangepage in range(1,rangepage+1):
    parameter = {
        'keywords': keywords,
        'limit': 50,
        'offset': 50,
        'page': rangepage,
        'facet': True,
        'access_token': tokens
    }
    headers = {'user-agent':
                   'Mozilla/5.0'}

    r = requests.get(url, params=parameter, headers=headers)
    content = r.json()

    if r.status_code != 200:
        print('!! TOKEN IS EXPIRED !!')
    else:
        None

        products = content['data']
        for p in products:
            title = p['name']
            price = p['price']
            stock = p['stock']
            count += 1
            print('No :', count, '||', 'Title :', title, '||', 'Price :', price, '||', 'Stock :', stock)

            datas.append([count,title,price,stock])


field = ['No','Title','Price','Stock']
writer = csv.writer(open('result/{}_{}.csv'.format(keywords,rangepage),'w',newline=''))
writer.writerow(field)
for d in datas : writer.writerow(d)
