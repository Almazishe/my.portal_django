import json

from django.shortcuts import render, get_list_or_404
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveUpdateAPIView
                                    )
from rest_framework.viewsets import ModelViewSet

from myDB.models import (Storage,
                        StorageCat, 
                        StorageResp, 
                        StorageState, 
                        StorageSubcat,
                        Users
                        )
from .serializers import (
                          AllStorageSerializer,
                          AllCategorySerializer,
                          AllSubCategorySerializer,
                          AllRespSerializer,
                          AllStateSerializer,
                          AllUserSerializer
                          )
# Create your views here.
class StorageViewSet(ModelViewSet):
  queryset = Storage.objects.all()
  serializer_class = AllStorageSerializer

  def get_queryset(self):
    query = Storage.objects.all()
    search = self.request.query_params.get('search', None)
    if search: 
      query = query.filter(sap__contains=search)
    return query

  def update(self, request, pk):
    storage = self.get_object()
    d = dict(request.data)
    res = {
      'name':storage.name,
      d['type'][0]: d['value'][0]
    }
    print(res)
    serializer = AllStorageSerializer(storage, data=res)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    print(serializer.errors)

    return Response(serializer.errors)

class CategoryViewSet(ModelViewSet):
  queryset = StorageCat.objects.all()
  serializer_class = AllCategorySerializer


class SubCategoryViewSet(ModelViewSet):
  queryset = StorageSubcat.objects.all()
  serializer_class = AllSubCategorySerializer

  def get_queryset(self):
    qs = StorageSubcat.objects.all()
    cat_id = self.request.query_params.get('cat_id', None)

    if cat_id:
      qs = qs.filter(cat_id=cat_id)
    

    return qs

class StateViewSet(ModelViewSet):
  queryset = StorageState.objects.all()
  serializer_class = AllStateSerializer

class RespViewSet(ModelViewSet):
  queryset = StorageResp.objects.all()
  serializer_class = AllRespSerializer

class UserViewSet(ModelViewSet):
  queryset = Users.objects.all()
  serializer_class = AllUserSerializer