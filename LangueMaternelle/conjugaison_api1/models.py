from django.db import models
from django.contrib import admin
from django.db import models

# Create your models here.

#le model pour la classe langue
class Langue(models.Model):
    nom_langue=models.CharField(max_length=50)
    regle_conjugaison=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nom_langue

#le model pour la classe temps_verbaux

class Temps_Verbaux(models.Model):
    nom_temps=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nom_temps

#le model pour la classe Niveau

class Niveau(models.Model):
    titre_niveau=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.titre_niveau


#le model pour la classe classe des verbes

class Classe_Verbe(models.Model):
    titre_classe=models.CharField(max_length=50)
    Langue=models.ForeignKey("conjugaison_api1.Langue", on_delete=models.CASCADE,null=True) 

    def __str__(self) -> str:
        return self.titre_classe 

#le model pour la classe verbe

class Verbe(models.Model):
    nom_verbe=models.CharField(max_length=50)
    Niveau=models.ForeignKey("conjugaison_api1.Niveau", on_delete=models.CASCADE) 
    Classe_Verbe=models.ForeignKey("conjugaison_api1.Classe_Verbe", on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.nom_verbe     


#le model pour la classe Avoir regle

class Avoir_regle(models.Model):
    regle=models.CharField(max_length=50)
    Temps_Verbaux=models.ForeignKey("conjugaison_api1.Temps_Verbaux", on_delete=models.CASCADE) 
    Langue=models.ForeignKey("conjugaison_api1.Langue", on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return self.regle     



#le model pour la Ere_conjuguer

class Etre_conjuguer(models.Model):
    Verbe=models.ForeignKey("conjugaison_api1.Verbe", on_delete=models.CASCADE,null=True)
    Langue=models.ForeignKey("conjugaison_api1.Langue", on_delete=models.CASCADE,null=True)
    Temps_Verbaux=models.ForeignKey("conjugaison_api1.Temps_Verbaux", on_delete=models.CASCADE,null=True) 
    person1=models.CharField(max_length=25)
    person2=models.CharField(max_length=25)
    person3=models.CharField(max_length=25)
    person4=models.CharField(max_length=25)
    person5=models.CharField(max_length=25)
    person6=models.CharField(max_length=25)

    audio=models.FileField(upload_to='Documents/',max_length=100, blank=True)

    def __str__(self) -> str:
        return f'{self.Verbe} + {self.Temps_Verbaux}'
    
class Etre_conjuguerlAdmin(admin.ModelAdmin):
    list_display=('id','Verbe','Langue','Temps_Verbaux','person1','person2','person3','person4','person5','person6','audio')
    list_filter=('Verbe',)
    search_fields=['Verbe',]    


class langueAdmin(admin.ModelAdmin):
    list_display=('id','nom_langue','regle_conjugaison',)
    list_filter=('nom_langue',)
    search_fields=['nom_langue',]