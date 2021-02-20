from django.shortcuts import render , HttpResponse #import httpresponse
from datetime import datetime #for date
from Home.models import Contact
from django.contrib import messages

# Create your views here.
#gonna make function her
def index(request):
    context = {
        "variable1":"Rishi Is Great",
        "variable2":"Rishi Is MAHAN"
    }
    return render(request,'index.html',context) # first request second name of template third is variable
    #return HttpResponse("This is homepage") #renders and retrns str
def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is AboutPage") #renders and retrns str    
def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name') # the name we gave earlier
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact = Contact(
        name = name,  
        email = email, 
        desc = desc, 
        date = date
        )
        contact.save()
        messages.success(request, 'Your Form Is Submitted : )')
    return render(request,'contacts.html')
    #return HttpResponse("This is ContactsPage")    
def sdownload(request):
    return render(request,'sdownload.html')
def mdownload(request):
    return render(request,'mdownload.html')
def download(request):
    return render(request,'download.html')  
def game(request):
    return render(request,'game.html')            