from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from pokedex.models import Type, Pokemon

import json
import http.client
import requests

# Create your views here.
class TypeListView(ListView):
    model = Type
    template_name = "type/type_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_pokemon'] = Pokemon.objects.all()
        return context

class TypeDetailView(DetailView):
    model = Type
    template_name = "type/type_detail.html"

def battlePokemon(request, first_id, second_id):
    first_pokemon = Pokemon.objects.get(id=first_id)
    second_pokemon = Pokemon.objects.get(id=second_id)

    pokemon_context = {}
    pokemon_context["p1types"] = {}
    pokemon_context["p2types"] = {}

    for ptype in first_pokemon.type.all():
        type_name = ptype.name
        current_multiplier = 1
        info_string = ""
        for ptype in second_pokemon.type.all():
            current_relations = ptype.damage_relations
            for i in current_relations['double_damage_from']:
                if type_name == i['name']:
                    current_multiplier = current_multiplier * 2
            for i in current_relations['half_damage_from']:
                if type_name == i['name']:
                    current_multiplier = current_multiplier * 0.5
            for i in current_relations['no_damage_from']:
                if type_name == i['name']:
                    current_multiplier = current_multiplier * 0
        
        if current_multiplier == 0:
           info_string = type_name.capitalize() + " does no damage against " + second_pokemon.name.capitalize() + "."
        else:
            info_string = type_name.capitalize() + " does " + str(current_multiplier) + " times damage against " + second_pokemon.name.capitalize() + "."
        pokemon_context["p1types"][type_name] = info_string
    
    for ptype in second_pokemon.type.all():
        type_name = ptype.name
        current_multiplier = 1
        info_string = ""
        for ptype in first_pokemon.type.all():
            current_relations = ptype.damage_relations
            for i in current_relations['double_damage_from']:
                if type_name == i['name']:
                    current_multiplier = current_multiplier * 2
            for i in current_relations['half_damage_from']:
                if type_name == i['name']:
                    current_multiplier = current_multiplier * 0.5
            for i in current_relations['no_damage_from']:
                if type_name == i['name']:
                    current_multiplier = current_multiplier * 0
        
        if current_multiplier == 0:
           info_string = type_name.capitalize() + " does no damage against " + first_pokemon.name.capitalize() + "."
        else:
            info_string = type_name.capitalize() + " does " + str(current_multiplier) + " times damage against " + first_pokemon.name.capitalize() + "."
        pokemon_context["p2types"][type_name] = info_string
    
    context = {
        'type_context': pokemon_context,
        'p1_name': first_pokemon.name.capitalize(),
        'p1_image': first_pokemon.image,
        'p2_name': second_pokemon.name.capitalize(),
        'p2_image': second_pokemon.image,
    }
    return render(request, 'type/battle.html', context)