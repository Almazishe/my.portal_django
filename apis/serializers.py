from rest_framework import serializers
from myDB.models import (Storage,
                        StorageCat, 
                        StorageResp,
                        StorageState,
                        StorageSubcat,
                        Users
                        )

class AllStorageSerializer(serializers.ModelSerializer):
	class Meta:
	    model = Storage
	    fields = '__all__'


class AllCategorySerializer(serializers.ModelSerializer):
	class Meta:
	    model = StorageCat
	    fields = '__all__'


class AllSubCategorySerializer(serializers.ModelSerializer):
	class Meta:
	    model = StorageSubcat
	    fields = '__all__'

class AllRespSerializer(serializers.ModelSerializer):
	class Meta:
	    model = StorageResp
	    fields = '__all__'

class AllStateSerializer(serializers.ModelSerializer):
	class Meta:
	    model = StorageState
	    fields = '__all__'


class AllUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = ('id', 'firstname', 'secondname',)


class id_name_UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Users
    fields = ('id', 'name',)

