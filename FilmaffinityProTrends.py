from bs4 import BeautifulSoup
import requests
import time
import string
import csv
URL_BASE = "https://www.filmaffinity.com"
URL_ALLFILMS = URL_BASE+"/es/allfilms"
MAX_REGS = 100000
counter = 0
review_list=[]
#for all the characters of the alphabet TODO: Indlude not letter chars
for c in string.ascii_uppercase:
    if (counter < MAX_REGS):
        print("Obteniendo Criticas Peliculas Empezadas Por Letra "+c)
        #obtaining the total pages containing links for a given letter
        html = requests.get(URL_ALLFILMS+"_"+c+"_1.html")
        statusCode = html.status_code
        if statusCode == 200:
            html.encoding = ('utf-8')
            text = html.text
            soup = BeautifulSoup(text,'lxml')
            td = soup.find_all(attrs={'class:',"pager"})
            atags=td[0].find_all("a")
            lastpage=atags[len(atags)-2]
            #getting all the links for a given letter
            for i in range(1,int(lastpage.text)):
                if(counter<MAX_REGS):
                    print("Obteniendo Pag "+str(i)+" letra "+ c)
                    time.sleep(1)

                    html = requests.get(URL_ALLFILMS + "_" + c + "_"+str(i)+".html")
                    statusCode = html.status_code
                    if statusCode == 200:
                        html.encoding=('utf-8')
                        soup = BeautifulSoup(html.text, 'lxml')
                        td = soup.find_all(attrs={ 'class:', "all-films-movie"})
                        for tr in td:
                            if (counter < MAX_REGS):
                                # getting title
                                title=tr.div.find_all(attrs={'class:', "mc-title"})[0].a.text
                                print("obteniendo criticas para " + title)
                                time.sleep(1)

                                url=URL_BASE+tr.a['href']
                                req = requests.get(url)
                                #checking that the request returns a Status Code = 200
                                statusCode = req.status_code
                                if statusCode == 200:
                                    req.encoding = ('utf-8')
                                    text = req.text
                                    soup = BeautifulSoup(text, 'lxml')
                                    #getting other fields
                                    try:
                                        datePublished = soup.findAll(attrs={"itemprop": "datePublished"})[0].text
                                    except:
                                        datePublished ="unknow"
                                    try:
                                        directors = soup.findAll(attrs={"itemprop": "director"})[0].text.strip()
                                    except:
                                        directors = "unknow"
                                    try:
                                        duration = soup.findAll(attrs={"itemprop": "duration"})[0].text
                                    except:
                                        duration = "unknow"
                                    try:
                                        genre = soup.findAll(attrs={"itemprop": "genre"})[0].text
                                    except:
                                        genre = "unknow"
                                    actorsstring=""
                                    try:
                                        actors = soup.findAll(attrs={"itemprop": "actor"})
                                    except:
                                        actors = "unknow"

                                    for act in actors:
                                        actorsstring += act.text.strip()

                                    tr = soup.find_all(attrs={'class:', "pro-crit-med"})

                                    for td in tr:
                                        try:
                                            autormedi = td.text.split(":", 1)
                                            autor = autormedi[0]
                                            if len(autormedi) > 1:
                                                medi = autormedi[1]
                                            else:
                                                medi = "unknow"
                                        except:
                                            autor="uknow"
                                            medi = "unknow"

                                        try:
                                            tendencia = td.i['title'].split(": ", 1)[1]
                                        except:
                                            tendencia ="unknow"

                                        # TODO FUTURE WORK:

                                        '''

                                        if (tendencia == "neutral"):
                                            tendencia = 0
                                        if (tendencia == "positiva"):
                                            tendencia = 1
                                        if (tendencia == "negativa"):
                                            tendencia = -1

                                        '''

                                        review_list.append([title,datePublished,duration,directors,genre,autor, medi,tendencia,actorsstring])
                                        counter += 1
                                        print(counter)

    print("Letra "+c+" DONE")

#Adding rows to csv File

writer = csv.writer(open('filmaffinity.csv', "a",newline='',encoding='utf-8') ,delimiter=";")
writer.writerow(["pelicula","date","duracio","director","genre","autor","medi","tendencia","actors"])
for row in review_list:
  writer.writerow(row)

print("Writing complete")