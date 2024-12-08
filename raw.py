import requests
from bs4 import BeautifulSoup
import lxml

# tr = column
# td = isolated

url = 'https://www.iban.com/currency-codes'
r = requests.get('https://www.iban.com/currency-codes')
html_text = r.text
soup = BeautifulSoup(html_text, 'lxml')

Columns = soup.find_all('tr')
Isolated = soup.find_all('td')

list_ = []

for item in Columns:
    td_list = item.find_all('td')
    list_.append(td_list)
list_.pop(0)

list_of_dicts = []

for entry in list_:
    Dictionary = {
        'Country': entry[0],
        'Code': entry[2],
        'UC': entry[1]
    }
    list_of_dicts.append(Dictionary)
print('Welcome to the Currency Negotiator')
print('Choose by the list number the country you want to check the currency code for.\n')
y = 0
x = 0
Countries_with_hashtags = []
for dict_ in list_of_dicts:
    x = x + 1
    if len(list_of_dicts[x - 1].get('Code').text) == 0:
        list_of_dicts.remove(list_of_dicts[x])
    else:
        y = y + 1
        Countries = {
            'P': '#' + str(y) + ' ' + list_of_dicts[x - 1].get('Country').text,
            'C': list_of_dicts[x - 1].get('Code').text
        }
        Countries_with_hashtags.append(Countries)

for dict_ in Countries_with_hashtags:
    print(dict_.get('P'))
while True:
    while True:
        try:
            x = int(input('Select the country #:'))
            if x < 270:
                break
            else:
                print('Choose a number from the list')
        except ValueError:
            print('That is not a number')

    print('You chose: ' + Countries_with_hashtags[x - 1].get('P'))
    print('The currency code for the country is: ' + Countries_with_hashtags[x - 1].get('C'))

    second_input = str(input('Do you want to check another code? Y/N \n'))
    if second_input == 'Y':
        pass
    elif second_input == 'N':
        break

    while second_input != 'Y' or second_input != 'N':
        print('Answer with "Y" or "N" only')
        second_input = str(input())
        if second_input == 'N' or second_input == 'Y':
            break
    if second_input == 'N':
        break
