import json

from django.shortcuts import render, get_list_or_404
from rest_framework.response import Response
from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveUpdateAPIView
                                    )
from myDB.models import (Storage,
                        StorageCat, 
                        StorageResp, 
                        StorageState, 
                        StorageSubcat
                        )
from .serializers import (StorageSerializer, 
                          StorageDetailSerializer,
                          StateListSerializer,
                          RespListSerializer,
                          SubCatListSerializer,
                          CatListSerializer
                          )
# Create your views here.

class RespListAPI(ListAPIView):
  serializer_class = RespListSerializer
  queryset = StorageResp.objects.all()


class StateListAPI(ListAPIView):
  serializer_class = StateListSerializer
  queryset = StorageState.objects.all()



class SubCatListAPI(ListAPIView):
  serializer_class = SubCatListSerializer

  def get_queryset(self):
    qs = StorageSubcat.objects.all()
    cat_id = self.request.query_params.get('cat_id', None)

    if cat_id:
      qs = qs.filter(cat_id=cat_id)
    

    return qs



class CatListAPI(ListAPIView):
  serializer_class = CatListSerializer
  queryset = StorageCat.objects.all()



class StorageList(ListAPIView):
  serializer_class = StorageSerializer

  def get_queryset(self):
    query = Storage.objects.all()
    search = self.request.query_params.get('search', None)
    if search: 
      query = query.filter(id__contains=search)
    return query
    
class StorageDetailAPI(RetrieveUpdateAPIView):
  serializer_class = StorageDetailSerializer
  queryset = Storage.objects.all()
  def put(self, request, pk):
    storage = self.get_object()
    d = dict(request.data)
    res = {
      'name':storage.name,
      d['type'][0]: d['value'][0]
    }
    print(res)
    serializer = StorageDetailSerializer(storage, data=res)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    print(serializer.errors)

    return Response(serializer.errors)