from django.urls import path

from . import views

app_name = "pokedex"

urlpatterns = [
    path("", views.PokemonListView.as_view(), name="pokemon_list"),
    path("create/<str:pokemon_name>", views.createPokemon, name="pokemon_create"),
    path("loadInitialData", views.loadInitialData, name="initial_create"),
    path("getInfo/<int:pk>", views.PokemonDetailView.as_view(), name="pokemon_detail"),
    path("delete/<int:pk>", views.PokemonDeleteView.as_view(), name="pokemon_delete"),
]