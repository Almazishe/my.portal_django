from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView


from myDB.models import Storage



def home(request):
  storages = Storage.objects.all()
  context = {
    'objects': storages,
  }

  return render(request, 'home.html', context)


def detail_view(request, pk=None):
  if pk:
    obj = Storage.objects.get(pk=pk)
    
