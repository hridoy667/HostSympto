from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def landing(request):
     
    return render(request,'Landing/landing_page.html')