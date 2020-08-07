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

def check_field(val):
  try:
    val = int(val)
    return True
  except ValueError:
    return False


def storage_view(request, pk=None):
  if request.method == 'POST':
    pst = request.POST
    name = pst.get('name')
    sap = pst.get('sap')
    sap_old = pst.get('sap_old')
    cat_id = pst.get('cat_id')
    subcat_id = pst.get('subcat_id')
    state_id = pst.get('state_id')
    owner_id = pst.get('owner_id')
    owner_name = pst.get('owner_name')
    resp_id = pst.get('resp_id')
    model = pst.get('model')
    serial_number = pst.get('serial_number')
    manufacturer = pst.get('manufacturer')
    description = pst.get('description')
    address_id = pst.get('address_id')
    floor = pst.get('floor')


    obj = Storage.objects.get(pk=pk)
    obj.name = name
    obj.sap = sap
    obj.sap_old = sap_old
    if obj.cat_id != int(cat_id):
      obj.subcat_id = 0
    else:
      obj.subcat_id = subcat_id
    obj.cat_id = cat_id
    obj.state_id = state_id
    if not check_field(owner_id):
      obj.owner_id = 0
    else:
      obj.owner_id = owner_id
    obj.owner_name = owner_name
    obj.resp_id = resp_id
    obj.model = model
    obj.serial_number = serial_number
    obj.manufacturer = manufacturer
    obj.description = description
    if not check_field(address_id):
      obj.address_id = 0
    else:
      obj.address_id = address_id

    if check_field(floor):
      obj.floor = floor
    else:
      obj.floor = 0
    obj.save()

    
  storages = Storage.objects.all()
  cats = StorageCat.objects.all()
  subcats = StorageSubcat.objects.all()
  resps = StorageResp.objects.all()
  states = StorageState.objects.all()
  context = {
    'storages': storages,
    'cats': cats,
    'subcats': subcats,
    'resps': resps,
    'states': states
  }
  if pk:
    obj = Storage.objects.get(pk=pk)
    context['obj'] = obj




  
  return render(request, 'detail.html', context)


class StorageUpdateView(UpdateView):
  model = Storage
  form_class = StorageForm
  template_name = 'detail.html'
  success_url = 'home'
  def get_success_url(self):
    return reverse('home')
  # def get_object(self):
  #   return self.request.user

