from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView


from myDB.models import Storage, StorageCat, StorageResp, StorageState, StorageSubcat



def home(request):
  return render(request, 'home.html')


def storage_view(request, pk=None):
  obj = Storage.objects.get(pk=pk)
  cats = StorageCat.objects.all()
  states = StorageState.objects.all()
  resps = StorageResp.objects.all()
  subcats = StorageSubcat.objects.filter(cat_id=obj.cat_id) 
  

  context = {
    'obj': obj,
    'cats': cats,
    'states': states,
    'resps': resps,
    'subcats': subcats
  }
  return render(request, 'detail.html', context)





