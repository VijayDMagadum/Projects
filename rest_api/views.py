from django.shortcuts import render
from django.http import *
from .models import *

# Create your views here.
def index(request):
    try:
         shelf=books.objects.all()
         context={'d':shelf}    
         return render(request,"index.html",context)
    except:
         return render(request,"index.html")

    return render(request,"index.html")
def login(request):
 
    
    try:
        if request.method=="POST":
            obj=user.objects.all()
            for i in obj:
                if i is not None:
                    if i.password==request.POST.get('pass'):
                        return HttpResponseRedirect("/adminlog/")
                    else:
                        m="Invalid Password"
                        return render(request,"login.html",{'c':m})
           
    except:

        return render(request,"login.html",{'a':"Invalid Account check Username or Password"})        

    return render(request,"login.html")

def reg(request):
    if request.method=="POST":
       users=user(fname=request.POST.get('firstname'),
                 lname=request.POST.get('lastname'),password=request.POST.get('pass'),
                 password2=request.POST.get('pass2'),email=request.POST.get('email'))
       users.save()

    return render(request,"signup.html")
def adminlog(request):
    shelf=books.objects.all()
    try:
         shelf=books.objects.all()
         if request.method=="POST":
            if request.POST.get('bookinput')!='':
               book=books(bookname=request.POST.get('bookinput'))
               book.save()

   
        
         context={'d':shelf}    
   
         return render(request,"admin-page.html",context)
    except:
           return render(request,"admin-page.html")

   
   

    

def update (request):
    shelf=books.objects.all()
    if request.method=="POST":
        a=request.POST.get('bookupdate')
        r=request.POST.get('bookupdate2')
        c=0
        try:
            t = books.objects.get(bookname=a)
            t.bookname = r 
            t.save()
        except:
            w="Invalid name"
            context={'d':shelf,
                 'w':w } 
    context={'d':shelf,
               } 
    return render(request,"admin-page.html",context)

def delete (request):
    shelf=books.objects.all()
    
    books.objects.filter(bookname=request.POST.get("delete")).delete()
    
    context={'d':shelf} 
    return render(request,"admin-page.html",context)