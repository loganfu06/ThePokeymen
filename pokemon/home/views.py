from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import ListView
import json
# Create your views here.
def index(request):
   #return HttpResponse("Hello, world. You're at the games index.")
   title_page = "The Pokeymen"
   return render(request, "home/index.html",
                 context={'title_page':title_page})