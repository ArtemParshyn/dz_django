from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api.serializers import UserSerializer# GoodSerializer, StorageSerializer
from api.models import ApiUser, Good, Storage

"""@csrf_exempt
def UserModelViewSet(request):
    
    List all code snippets, or create a new snippet.
    
    if request.method == 'GET':
        user = ApiUser.objects.all()
        serializer = UserSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
"""
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', "path", "get"]
    serializer_class = UserSerializer


"""
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post', "path", "get"]
    serializer_class = UserSerializer



class GoodViewSet(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer

class StorageSendToView(viewsets.ModelViewSet):
    def get_queryset(self, request):
        pk = self.kwargs.get('pk')
        try:
            storage = Storage.objects.get(pk=pk)
        except Storage.DoesNotExist:
            return HttpResponse(status=404)
        if request.method == 'POST':
            return storage
        # Логика, использующая значение pk
        # Например, возвращение фильтрованного queryset по значению pk
    # return JsonResponse(serializer.errors, status=400)

"""
