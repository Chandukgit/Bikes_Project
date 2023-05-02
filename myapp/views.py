from django.shortcuts import redirect, render
from .models import Login,Register,ContactForm
from django import views
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import re
# from django.contrib.auth.decorators import login_required
# @login_required(login_url='login')
def LoginForm(requests):
        if requests.method=="POST":
            username=requests.POST.get('username')
            password=requests.POST.get('password')
            User= authenticate(requests,username=username,password=password)
            if User is not None:
                login(requests,User)
                return redirect("home")
            else:
                return HttpResponse("email and password are incorrect")
        return render(requests,"loginpage.html")
def register(requests):
     if requests.method=="POST":
          username=requests.POST.get('username')
          email=requests.POST.get('email')

          createpassword=requests.POST.get('create_password')
          conformpassword=requests.POST.get('conform_password')
          if createpassword!=conformpassword:
               return HttpResponse("Your password and conform password are not same ")
          else :
               user=User.objects.create_user(username,email,createpassword)
               user.save()
               return redirect('login')
          
     return render(requests,"register.html")
# Index.html code for upcoming bikes 
url = 'https://www.zigwheels.com/bikes/launches'
html_text = requests.get(url)
soup = BeautifulSoup(html_text.text, 'html.parser')
upcomingimage = soup.find_all('div', class_='mke-lft')
upbikesname = soup.find_all('div', class_='mke-ryt')
upprice = soup.find_all("div", {'title': ' Ex-Showroom Price'})
upcomingLink = []
upcom_images = []
upcom_price = []
upcom_name = []

for i in upcomingimage:
    img = i.find('img', {'data-gsll-src': True})
    if img:
        upcom_images.append(img['data-gsll-src'])

    k = "https://www.zigwheels.com/bikes/"
    upcomingLink.append(k)

for j in upprice:
    price = re.sub(r"[\n\t]", "", j.text)
    upcom_price.append(price)

for k in upbikesname:
    t = k.a["title"]
    upcom_name.append(t)

upcominglist=zip(upcomingLink, upcom_images, upcom_price, upcom_name )
def Home(requests):
     return render(requests,"index.html",{"upcominglist":upcominglist})
def Logout(requests):
     logout(requests)
     return redirect('login')
def Contact(requests):
     if requests.method=="POST":
          Firstname=requests.POST.get('firstname')
          Lastname=requests.POST.get('lastname')
          Email=requests.POST.get('email')
          Address=requests.POST.get('address')
          Message=requests.POST.get('message')
          contact=ContactForm(Firstname=Firstname ,Lastname=Lastname,Email=Email,Address=Address,Message=Message)
          contact.save()
     return render(requests,"Contact.html")

url='https://www.bikewale.com/hero-bikes/'
html_text=requests.get(url)
soup=BeautifulSoup(html_text.text,'html.parser')
heroimage=soup.find_all('div',class_='imageWrapper')
heroname=soup.find_all('div',class_='bikeDescWrapper')
heroprice=soup.find_all('div',class_='text-bold')
Herolink=[]
Hero_images=[]
Hero_price=[]
Hero_name=[]
for i in heroimage:
    img=i.a.img["src"]
    k="https://www.bikewale.com/hero-bikes/"+i.a["href"]
    t=i.a.img["title"]
    Hero_images.append(img)
    Hero_name.append(t)
    Herolink.append(k)
for k in heroprice:
    span=k.find('span')
    price = span.text if span else 'will be updated'
    Hero_price.append(price)
mylist=zip(Herolink,Hero_images,Hero_name,Hero_price,)
def Hero(requests):
     return render(requests,"hero.html",{"mylist":mylist})

from bs4 import BeautifulSoup
import requests
url="https://www.bikewale.com/bajaj-bikes/"
Content=requests.get(url)
soup=BeautifulSoup(Content.text,'html.parser')
Bajajimage=soup.find_all('div', class_='imageWrapper')
Bajajame=soup.find_all('div',class_='bikeDescWrapper')
Bajajprice=soup.find_all('div',class_='text-bold')
Bajajlink=[]
Bajaj_images=[]
Bajaj_price=[]
Bajaj_name=[]
for i in Bajajimage:
    img=i.a.img["src"]
    k="https://www.bikewale.com/bajaj-bikes/"+i.a["href"]
    t=i.a.img["title"]
    Bajaj_images.append(img)
    Bajaj_name.append(t)
    Bajajlink.append(k)
for j in Bajajprice:
    span = j.find('span')
    price = span.text if span else 'will be updated'
    Bajaj_price.append(price)

BajajList=zip(Bajajlink,Bajaj_images,Bajaj_name,Bajaj_price,)
def Bajaj(requests):
     return render(requests,"bajaj.html",{"BajajList":BajajList})

url="https://www.bikewale.com/honda-bikes/"
Content=requests.get(url)
soup=BeautifulSoup(Content.text,'html.parser')
Hondaimage=soup.find_all('div', class_='imageWrapper')
Hondaname=soup.find_all('div', class_='bikeDescWrapper')
Hondaprice=soup.find_all('div', class_='text-bold')
Hondalink=[]
Honda_images=[]
Honda_price=[]
Honda_name=[]
for i in Hondaimage:
    img=i.a.img["src"]
    k="https://www.bikewale.com/honda-bikes/"+i.a["href"]
    t=i.a.img["title"]
    Honda_images.append(img)
    Honda_name.append(t)
    Hondalink.append(k)
for j in Hondaprice:
    span = j.find('span')
    price = span.text if span else 'will be updated'
    Honda_price.append(price)

HondaList=zip(Hondalink, Honda_images, Honda_name, Honda_price )
def Honda(requests):
     return render(requests,"honda.html",{"HondaList":HondaList})
