from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse

from .models import Pokemon, Type

# Create your views here.
class PokemonListView(ListView):
    model = Pokemon
    
def createPokemon(request, pokemon_name):
    print("this works")
    return redirect("pokedex:pokemon_list")