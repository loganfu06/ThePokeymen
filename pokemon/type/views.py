from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from pokedex.models import Type

import json
import http.client
import requests

# Create your views here.
class TypeListView(ListView):
    model = Type
    template_name = "type/type_list.html"
class TypeDetailView(DetailView):
    model = Type
    template_name = "type/type_detail.html"