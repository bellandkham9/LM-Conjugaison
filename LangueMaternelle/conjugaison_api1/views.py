from django.shortcuts import get_object_or_404, render
import requests
from .forms import *
from .models import *
# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import *
from .serializers import *

class VerbeListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        verbes = Verbe.objects.filter()
        serializer = VerbeSerializer(verbes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'nom_verbe':request.data.get('nom_verbe'),
            'Niveau':request.data.get('Niveau'),
            'Classe_Verbe':request.data.get('Classe_Verbe')
        }
        serializer = VerbeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerbeDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, verbe_id):
        '''
        Helper method to get the object with given verbe_id
        '''
        try:
            return Verbe.objects.get(id=verbe_id)
        except Verbe.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, verbe_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(verbe_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = VerbeSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, verbe_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(verbe_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nom_verbe':request.data.get('nom_verbe'),
            'Niveau':request.data.get('Niveau'),
            'Classe_Verbe':request.data.get('Classe_Verbe')
        }
        serializer = VerbeSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, verbe_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(verbe_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )



#Pour la gestion de la conjugaison





class VerbeConjuguéListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, val, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        verbes = Etre_conjuguer.objects.filter(Langue=val)
        serializer = Etre_conjuguerSerializer(verbes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'Verbe':request.data.get('Verbe'),
            'Langue':request.data.get('Langue'),
            'Temps_Verbaux':request.data.get('Temps_Verbaux'),
            'person1':request.data.get('person1'),
            'person2':request.data.get('person2'),
            'person3':request.data.get('person3'),
            'person4':request.data.get('person4'),
            'person5':request.data.get('person5'),
            'person6':request.data.get('person6'), 
            'audio':request.FILES.get('audio'),

        }
        serializer = Etre_conjuguerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class VerbeConjuguéDetailApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, verbeConjug_id,temps_verbe,verbe):
        '''
        Helper method to get the object with given verbe_id
        '''
        try:
            return Etre_conjuguer.objects.get(Langue=verbeConjug_id,Temps_Verbaux=temps_verbe,Verbe=verbe)
        except Etre_conjuguer.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, verbeConjug_id, temps_verbe,verbe,*args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(verbeConjug_id,temps_verbe,verbe)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = Etre_conjuguerSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, verbeConjug_id, temps_verbe, verbe,*args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(verbeConjug_id,temps_verbe,verbe)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'Verbe':request.data.get('Verbe'),
            'Langue':request.data.get('Langue'),
            'Temps_Verbaux':request.data.get('Temps_Verbaux'),
            'person1':request.data.get('person1'),
            'person2':request.data.get('person2'),
            'person3':request.data.get('person3'),
            'person4':request.data.get('person4'),
            'person5':request.data.get('person5'),
            'person6':request.data.get('person6'),
            'audio':request.FILES.get('audio'),

        }
        serializer = Etre_conjuguerSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, verbeConjug_id,temps_verbe,verbe, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(verbeConjug_id,temps_verbe,verbe)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )        




#Pour les classes des verbes





class ClassVerbeListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        verbes = Classe_Verbe.objects.filter()
        serializer = Classe_VerbeSerializer(verbes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'titre_classe':request.data.get('titre_classe'),
            'Langue':request.data.get('Langue'),
        }
        serializer = Classe_VerbeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ClassVerbeDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, ClassVerbe_id):
        '''
        Helper method to get the object with given verbe_id
        '''
        try:
            return Classe_Verbe.objects.get(id=ClassVerbe_id)
        except Classe_Verbe.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, ClassVerbe_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(ClassVerbe_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = Classe_VerbeSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, ClassVerbe_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(ClassVerbe_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'titre_classe':request.data.get('titre_classe'),
            'Langue':request.data.get('Langue'),

        }
        serializer = Classe_VerbeSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, ClassVerbe_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(ClassVerbe_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )        





#Pour les classes des langues





class LangueListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        verbes = Langue.objects.filter()
        serializer = LangueSerializer(verbes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'nom_langue':request.data.get('nom_langue'),
            'regle_conjugaison':request.data.get('regle_conjugaison')
        }
        serializer = LangueSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LangueDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, langue_id):
        '''
        Helper method to get the object with given verbe_id
        '''
        try:
            return Langue.objects.get(id=langue_id)
        except Langue.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, langue_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(langue_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LangueSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, langue_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(langue_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nom_langue':request.data.get('nom_langue'),
            'regle_conjugaison':request.data.get('regle_conjugaison'),

        }
        serializer = LangueSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, langue_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(langue_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )




#Pour les temps verbaux





class TempsListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        verbes = Temps_Verbaux.objects.filter()
        serializer = Temps_VerbauxSerializer(verbes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
            'nom_temps':request.data.get('nom_temps')
        }
        serializer = Temps_VerbauxSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TempsDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, temps_id):
        '''
        Helper method to get the object with given verbe_id
        '''
        try:
            return Temps_Verbaux.objects.get(id=temps_id)
        except Temps_Verbaux.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, temps_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(temps_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = Temps_VerbauxSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, temps_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(temps_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'nom_temps':request.data.get('nom_temps')
        }
        serializer = Temps_VerbauxSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, temps_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(temps_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )          




#Pour les Niveau





class NiveauListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        verbes = Niveau.objects.filter()
        serializer = NiveauSerializer(verbes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
             'titre_niveau':request.data.get('titre_niveau')
        }
        serializer = NiveauSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class NiveauDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, niveau_id):
        '''
        Helper method to get the object with given verbe_id
        '''
        try:
            return Niveau.objects.get(id=niveau_id)
        except Niveau.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, niveau_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(niveau_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = NiveauSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, niveau_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(niveau_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'titre_niveau':request.data.get('titre_niveau')
        }
        serializer = NiveauSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, niveau_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(niveau_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )          




#Pour les AvoirRegle





class AvoirRegleListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        verbes = Avoir_regle.objects.filter()
        serializer = Avoir_regleSerializer(verbes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        data = {
             'regle':request.data.get('regle'),
             'Temps_Verbaux':request.data.get('Temps_Verbaux'),
             'Langue':request.data.get('Langue')
        }
        serializer = Avoir_regleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AvoirRegleDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, regle_id):
        '''
        Helper method to get the object with given verbe_id
        '''
        try:
            return Avoir_regle.objects.get(id=regle_id)
        except Avoir_regle.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, regle_id, *args, **kwargs):
        '''
        Retrieves the Todo with given todo_id
        '''
        todo_instance = self.get_object(regle_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = Avoir_regleSerializer(todo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, regle_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(regle_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'regle':request.data.get('regle'),
            'Temps_Verbaux':request.data.get('Temps_Verbaux'),
            'Langue':request.data.get('Langue')
        }
        serializer = Avoir_regleSerializer(instance = todo_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, regle_id, *args, **kwargs):
        '''
        Deletes the todo item with given todo_id if exists
        '''
        todo_instance = self.get_object(regle_id)
        if not todo_instance:
            return Response(
                {"res": "Object with todo id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        todo_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )          

from verbecc import Conjugator

def conjuguer(verbe,temps):
    cg = Conjugator(lang='fr')
    conjugation = cg.conjugate(verbe)
    conj = conjugation['moods']['indicatif'][temps]
    return conj


def myConjugaison(request):
    if request.method =='POST':
        form1=ConjugaisonForm(request.POST)
        if form1.is_valid():
            cd=form1.cleaned_data
            temps=cd["Temps_Verbaux"]
            verbe=cd["Verbe"]
            lang=cd["Langue"]
            id_verbe=get_object_or_404(Verbe,nom_verbe=verbe)
            id_verbe1=id_verbe.id

            id_temps=get_object_or_404(Temps_Verbaux,nom_temps=temps)
            id_temps1=id_temps.id

            id_lang=get_object_or_404(Langue,nom_langue=lang)
            id_lang1=id_lang.id

            print(id_verbe)


            result=conjuguer(f'{verbe}',f'{temps}')

            reponse=requests.get(f'http://127.0.0.1:8000/conjugaison/conjuguerD/{id_lang1}/{id_temps1}/{id_verbe1}/').json()
            return render(request, 'html/conjugaison.html', {'data':result, 'conjugL':reponse})  
    else:
        form1=ConjugaisonForm(request.POST)
    return render(request,'html/conjugaison.html', {'form1':form1})        
        


def registerConjug(request):
    if request.method=='POST':
        conj_form=RegisterConjugForm(request.POST)
        if conj_form.is_valid():
             new_user=conj_form.save(commit=False)
             new_user.save()
             return render(request,'html/registerDone.html', {'new_user':new_user})
    else:
        conj_form=RegisterConjugForm(request.POST)
    return render(request,'html/addConjugaison.html', {'conj_form':conj_form})