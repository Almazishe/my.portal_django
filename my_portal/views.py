from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView


from myDB.models import Storage, StorageCat, StorageResp, StorageState, StorageSubcat, Users



def home(request):
  return render(request, 'home.html')


def storage_view(request, pk=None):
  obj = Storage.objects.get(pk=pk)
  cats = StorageCat.objects.all().order_by('name')
  states = StorageState.objects.all().order_by('name')
  resps = StorageResp.objects.all().order_by('secondname')
  subcats = StorageSubcat.objects.filter(cat_id=obj.cat_id) 
  users = Users.objects.all().order_by('secondname')
  

  context = {
    'obj': obj,
    'cats': cats,
    'states': states,
    'resps': resps,
    'subcats': subcats,
    'users': users,
  }
  return render(request, 'detail.html', context)





