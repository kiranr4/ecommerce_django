from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

##RK Custom added
def index(request):
    return render(request, "ecom\index.html")
