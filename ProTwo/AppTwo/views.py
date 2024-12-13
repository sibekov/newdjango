from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict={'insert_me':"Now I am comming from App Two Hello I am from views.py!"}
    return render(request,'AppTwo/index.html',context=my_dict)