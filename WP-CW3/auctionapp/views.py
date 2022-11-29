from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from auctionapp.models import Account 
def index(request):
    getObject=Account.objects.all()
    return render(request,'auctionapp/index.html',{
        'n':getObject
    })
