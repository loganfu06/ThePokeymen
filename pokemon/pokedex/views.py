from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse

from .models import Pokemon, Type

import json
import http.client
import requests

# Create your views here.
class PokemonListView(ListView):
    model = Pokemon
    
def createPokemon(request, pokemon_name):
    api_url = 'https://pokeapi.co/api/v2/pokemon/{fname}'.format(fname = pokemon_name)
    response = requests.get(api_url)

    if response.status_code == 200:
        pokemon_data = response.json()
        if Pokemon.objects.filter(name=pokemon_data['name']).exists():
            messages.add_message(
                request, messages.ERROR,
            'Pokemon "{pname}" already exists.'.format(pname=pokemon_data['name'].capitalize()))
        else:
            current_pokemon = Pokemon(
                name = pokemon_data['name'],
                hp = pokemon_data['stats'][0]['base_stat'],
                attack = pokemon_data['stats'][1]['base_stat'],
                defense = pokemon_data['stats'][2]['base_stat'],
                special_attack = pokemon_data['stats'][3]['base_stat'],
                special_defense = pokemon_data['stats'][4]['base_stat'],
                speed = pokemon_data['stats'][5]['base_stat'],
                image = pokemon_data['sprites']['front_default']
            )
            current_pokemon.save()
            for i in pokemon_data['types']:
                type_name = i['type']['name']
                try:
                    current_type = Type.objects.get(name=type_name)
                except:
                    messages.add_message(
                        request, messages.ERROR,
                    'Please load types before adding Pokemon')
                    return redirect("pokedex:pokemon_list")
                current_pokemon.type.add(current_type)
            current_pokemon.save()

            messages.add_message(
                request, messages.SUCCESS,
            'Pokemon "{pname}" successfully added.'.format(pname = pokemon_data['name'].capitalize()))
    else:
        messages.add_message(
                request, messages.ERROR,
            'Please enter a valid Pokemon name.')

    return redirect("pokedex:pokemon_list")

def loadTypes(request):
    if len(Type.objects.filter()) == 0:
        for i in range(18):
            current_num = i + 1
            api_url = 'https://pokeapi.co/api/v2/type/{tnum}'.format(tnum = current_num)
            response = requests.get(api_url)
            type_data = response.json()

            current_type = Type(
                name = type_data['name'],
                damage_relations = type_data['damage_relations']
            )
            current_type.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Successfully loaded all Types.'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'Types are already loaded.'
        )

    return redirect("pokedex:pokemon_list")
