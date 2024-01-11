from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
    path("", views.PokemonListView.as_view(), name="pokemon_list"),
    path("create/<str:pokemon_name>", views.createPokemon, name="pokemon_create"),
]