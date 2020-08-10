from rest_framework import serializers
from myDB.models import (Storage,
                        StorageCat, 
                        StorageResp,
                        StorageState,
                        StorageSubcat
                        )

class StorageSerializer(serializers.ModelSerializer):
	class Meta:
	    model = Storage
	    fields = ('id', 'name')

class StorageDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model = Storage
    fields = "__all__"
class CatListSerializer(serializers.ModelSerializer):
  class Meta:
    model = StorageCat
    fields = "__all__"
class SubCatListSerializer(serializers.ModelSerializer):
  class Meta:
    model = StorageSubcat
    fields = "__all__"

class RespListSerializer(serializers.ModelSerializer):
  class Meta:
    model = StorageResp
    fields = "__all__"

class StateListSerializer(serializers.ModelSerializer):
  class Meta:
    model = StorageState
    fields = "__all__"



