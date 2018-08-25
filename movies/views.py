import json

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from .recommendations import *
from .models import Movies
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from bs4 import BeautifulSoup
import urllib.request

#function for scraping youtube
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

# Create your views here.

def get_recom(request):
	if request.method=='POST':
		input_title= request.POST.get("title")
		#capitalize the input
		input_title=input_title.title()
		print(input_title)
		m="a"
	else:
		input_title=""
		title=list(md['title'])
		genres=list(md['genres'])
		photo=list(md['poster_path'])
		imdb=list(md['imdb_score'])
		m=""

	try:
		dic=get_recommendations(input_title)[0:20]
		# dics=list(dic)
		title=list(dic['title'])
		genres=list(dic['genres'])
		photo=list(dic['poster_path'])
		imdb=list(dic['imdb_score'])
		mid=[]
		for i in photo:
			a,b=i.split("_")
			c,d=b.split(".")
			mid.append(c)

		
		
		# print(dic['title'])
		# print(dic['genres'])
		a="MOVIES SIMILAR TO"+" "+input_title
	except:
		a='We could not find the movie with title'+" "+input_title
		m=""
		title={}
		genres={}
		photo={}
		imdb={}
		mid={}
	
	
	    
	# return HttpResponse("Hello")
	return render(request,'movies/recomm.html',{"mid":mid,'title':title,'genres':genres,'photo':photo,'imdb':imdb,'a':a,'myvalue':m,'recompage':"recompage"})

def index(request):
	movies_list=Movies.objects.all()[0:200]
	paginator = Paginator(movies_list, 21)
	page = request.GET.get('page')
	try:
		movies = paginator.page(page)
	except PageNotAnInteger:
		movies = paginator.page(1)
	except EmptyPage:
		movies = paginator.page(paginator.num_pages)
	
	context={
	'movies':movies
	}
	return render(request,"movies/allmovies.html",context)
def detail(request,movietitle_or_id):
	try:
		movie=get_object_or_404(Movies,pk=movietitle_or_id)
	except:
		try:
			movie=Movies.objects.get(title=movietitle_or_id.title())
		except:
			message="Movie with name  '"+movietitle_or_id+"'  not found!!!"
			return render(request,'index.html',{'message':message})
	return render(request,'movies/detail.html',{'movie':movie})

def watchingtrailer(request,moviename):
	trailerurl = SearchVid(moviename.replace(" ","%20")+"%20trailer")
	print(trailerurl)
	return render(request,"trailer.html",{'moviename':moviename,'trailerurl':trailerurl})

def searchmovie(request,search_text):
	search_text=search_text.title()
	movies=Movies.objects.filter(title__contains=search_text)
	mylist=[]
	for i in movies:
		mylist.append(i.title)
	mylist=json.dumps(mylist)
	return JsonResponse(mylist, safe=False)

def homepage(request):
	return render(request,'index.html')