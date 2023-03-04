from django.db.models import fields
from rest_framework import serializers
from .models import *
 
class LangueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Langue
        fields = ('id','nom_langue','regle_conjugaison')

class Temps_VerbauxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temps_Verbaux
        fields = ('id','nom_temps')        

class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = ('id','titre_niveau')   

class Classe_VerbeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe_Verbe
        fields = ('id','titre_classe','Langue')   


class VerbeSerializer(serializers.ModelSerializer):
         class Meta:
              model = Verbe
              fields = ('id','nom_verbe','Niveau','Classe_Verbe',)


class Avoir_regleSerializer(serializers.ModelSerializer):
        class Meta:
             model = Avoir_regle
             fields = ('regle','Temps_Verbaux','Langue') 


class Etre_conjuguerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etre_conjuguer
        fields = ('id','Verbe','Langue','Temps_Verbaux','person1','person2','person3','person4','person5','person6','audio')                                     