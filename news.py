import urllib.request
from bs4 import BeautifulSoup
import csv

titles = []
new_title = []
another_title=[]
news_link = []
NEWS=[]
with urllib.request.urlopen("http://kathmandupost.ekantipur.com/") as url:
    s = url.read()
    print(s)
soup = BeautifulSoup(s, 'html.parser')

for link in soup.find_all('a'):
    if link.has_attr('href'):
        filter = link.attrs['href']
        if '/news/2016-07' in filter:
            news_link.append('http://kathmandupost.ekantipur.com' + filter)


new_title.append(list(set(news_link)))
# print(new_title)
# for i in range(len(new_title[0])):
#    print(new_title[0][i])


# print(new_title)
for i in range(70):
    with urllib.request.urlopen(new_title[0][i]) as url:
        s = url.read()
    soup = BeautifulSoup(s, 'html.parser')

    # for link in soup.find_all('h1'):
    #     # print(link.string)
    #     titles.append(link.string)
    #
    #
    #     # print(titles[i].string)
    #
    #     # with open('mycsv.txt', "w") as output:
    #     #     writer = csv.writer(output, lineterminator='\n')
    #     #     writer.writerow(titles[i].string)


    for link in soup.find_all('p'):
        print(link.string)
        target = open("hellotxt.csv", 'a')
        target.write(str(link.string))
        target.close()

        with open('mycsv.csv', "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for val in str(link.string):
                writer.writerow([val])

    target = open("hellotxt.csv", 'a')
    target.write("\n")
    target.close()



            # with open('hello.txt', "w") as output:
            #     writer = csv.writer(output, lineterminator='\n')
            #     writer.writerow(link.string)
            #     for val in link.string:
            #         writer.writerow([val])

    # with open('hellotxt.csv','r') as file:
    #     data = file.readlines()
    #     for each in data:
    #         print(each)