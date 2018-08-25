from bs4 import BeautifulSoup
import urllib.request


def SearchVid(search):
    responce = urllib.request.urlopen('https://www.youtube.com/results?search_query='+search)

    soup = BeautifulSoup(responce)    
    divs = soup.find_all("div", { "class" : "yt-lockup-content"})


    for i in divs:
        href= i.find('a', href=True)
        a,b=(href['href']).split("=")
        trailer_url=("\nhttps://www.youtube.com/embed/"+b)
        break
    return trailer_url


print("What are you looking for?")
SearchString = input()
x=SearchVid(SearchString.replace(" ", "%20"))
print(x)