from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView


from myDB.models import Storage, StorageCat, StorageResp, StorageState, StorageSubcat
from .forms import StorageForm



def home(request):
  return render(request, 'home.html')


def storage_view(request, pk=None):
  return render(request, 'detail.html', {'pk':pk})





