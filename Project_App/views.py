from django.shortcuts import render, HttpResponse
from datetime import datetime
from Project_App.models import Contact
# Create your views here.
def home(request):
    return render(request,'Home.html')
def index(request):
    return render(request,'index.html')
    #return HttpResponse("This is index page")
def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        name=request.POST.get('name')
        contact=Contact(name=name,phone=phone,email=email,date=datetime.today())
        contact.save()
    return render(request ,'contact.html')
def signin(request):
    return HttpResponse("This is signin page.!!!!!!!!!!!!!!!!!!!!!!!")
def book_now(request):
    return render(request,'book_now.html')