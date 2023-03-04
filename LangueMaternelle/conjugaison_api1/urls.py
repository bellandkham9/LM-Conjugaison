from django.urls import path, include
from .views import *
from .import views

urlpatterns = [
    path('verbe', VerbeListApiView.as_view()),
    path('verbe/<int:verbe_id>/', VerbeDetailApiView.as_view()),

    path('conjuguer/<int:val>/', VerbeConjuguéListApiView.as_view()),
    path('conjuguerD/<int:verbeConjug_id>/<str:temps_verbe>/<str:verbe>/', VerbeConjuguéDetailApiView.as_view()),

    path('Classe_verbe', ClassVerbeListApiView.as_view()),
    path('Classe_verbe/<int:ClassVerbe_id>/', ClassVerbeDetailApiView.as_view()),

    path('Langue', LangueListApiView.as_view()),
    path('Langue/<int:langue_id>/', LangueDetailApiView.as_view()),

    path('Temps verbaux', TempsListApiView.as_view()),
    path('Temps verbaux/<int:temps_id>/', TempsDetailApiView.as_view()),

    path('Niveau', NiveauListApiView.as_view()),
    path('Niveau/<int:niveau_id>/', NiveauDetailApiView.as_view()),

    path('Regle', AvoirRegleListApiView.as_view()),
    path('Regle/<int:regle_id>/', AvoirRegleDetailApiView.as_view()),

    path('VoirConjugaison/', views.myConjugaison),
    path('ajouterConjugaison/', views.registerConjug)
]