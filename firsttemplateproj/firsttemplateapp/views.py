from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    mydict={"usemehere":"This is printing from view we are happy!!"}
    return render(request,'firsttemplateapp/index.html',context=mydict)