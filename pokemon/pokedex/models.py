from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=25)
    hp = models.SmallIntegerField()
    attack = models.SmallIntegerField()
    defense = models.SmallIntegerField()
    special_attack = models.SmallIntegerField()
    special_defense = models.SmallIntegerField()
    speed = models.SmallIntegerField()
    image = models.CharField(max_length=250)
    pokemon_type = models.ManyToManyField(Type)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
    		return self.name
    
    
class Type(models.Model):
    name = models.CharField(max_length=50)
    