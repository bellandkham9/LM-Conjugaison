from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Verbe)
admin.site.register(Classe_Verbe)
admin.site.register(Temps_Verbaux)
admin.site.register(Langue,langueAdmin)
admin.site.register(Niveau)
admin.site.register(Etre_conjuguer,Etre_conjuguerlAdmin)
admin.site.register(Avoir_regle)
