from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import UpdateView


from myDB.models import Storage, StorageCat, StorageResp, StorageState, StorageSubcat
from .forms import StorageForm


def home(request):
  storages = Storage.objects.all()
  context = {
    'objects': storages,
  }

  return render(request, 'home.html', context)


class StorageUpdateView(UpdateView):
  model = Storage
  form_class = StorageForm
  template_name = 'detail.html'
  success_url = 'home'
  def get_success_url(self):
    return reverse('home')
  # def get_object(self):
  #   return self.request.user

