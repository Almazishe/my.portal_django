from django import forms
from django.forms import Select as Sel

from myDB.models import Storage, StorageCat, StorageResp, StorageState, StorageSubcat





def get_cat_id():
  ids = [i[0] for i in StorageCat.objects.all().values_list('id')]
  names = [i[0] for i in StorageCat.objects.all().values_list('name')]

  {
    "id": "id",
    "name": "Mustang"
  }

  res = [(-1, 'Select')]
  for i in range(len(ids)):
    res.append(tuple([ids[i], names[i]]))
  res = tuple(res)
  return res

def get_subcat_id():
  ids = [i[0] for i in StorageSubcat.objects.all().values_list('id')]
  names = [i[0] for i in StorageSubcat.objects.all().values_list('name')]

  res = [(-1, 'Select')]
  for i in range(len(ids)):
    res.append(tuple([ids[i], names[i]]))
  res = tuple(res)
  return res

def get_state_id():
  ids = [i[0] for i in StorageState.objects.all().values_list('id')]
  names = [i[0] for i in StorageState.objects.all().values_list('name')]

  res = [(-1, 'Select')]
  for i in range(len(ids)):
    res.append(tuple([ids[i], names[i]]))
  res = tuple(res)
  return res

def get_resp_id():
  ids = [i[0] for i in StorageResp.objects.all().values_list('id')]
  firstnames = [i[0] for i in StorageResp.objects.all().values_list('firstname')]
  lastnames = [i[0] for i in StorageResp.objects.all().values_list('secondname')]
  res = [(-1, 'Select')]
  for i in range(len(ids)):
    res.append(tuple([ids[i], firstnames[i] + " " + lastnames[i]]))
  res = tuple(res)
  return res

class StorageForm(forms.ModelForm):
  id = forms.CharField(label="ID", required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'ID'}))
  sap = forms.CharField(label="SAP", required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'SAP'}))
  sap_old = forms.CharField(label="SAP-OLD", required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'SAP-OLD'}))
  name = forms.CharField(label="Name", required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Name'}))
  cat_id = forms.ChoiceField(label="CAT_ID",choices=get_cat_id(), required=False, widget=forms.Select(attrs = {'class': 'form-control', 'placeholder': 'Cat_ID'}))
  subcat_id = forms.ChoiceField(label="SUBCAT_ID",choices=get_subcat_id(), required=False, widget=forms.Select(attrs = {'class': 'form-control', 'placeholder': 'SUBCAT_ID'}))
  owner_id = forms.IntegerField(label="owner_id", required=False, widget=forms.NumberInput(attrs = {'class': 'form-control', 'placeholder': 'owner_id'}))
  owner_name = forms.CharField(label="Owner Name", required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Owner Name'}))
  resp_id = forms.ChoiceField(label="resp_ID",choices=get_resp_id(), required=False, widget=forms.Select(attrs = {'class': 'form-control', 'placeholder': 'resp_ID'}))
  date_open = forms.DateTimeField(label="date Open", required=False, widget=forms.DateTimeInput(attrs = {'class': 'form-control', 'placeholder': 'date_open'}))
  date_assign = forms.DateTimeField(label="date_assign", required=False, widget=forms.DateTimeInput(attrs = {'class': 'form-control', 'placeholder': 'date_assign'}))
  model = forms.CharField(label="model", required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Model'}))
  serial_number = forms.CharField(label="serial_number", required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'serial_number'}))
  manufacturer = forms.CharField(label="manufacturer", required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'manufacturer'}))
  description = forms.CharField(label="description", required=False, widget=forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'description'}))
  modified_date = forms.DateTimeField(label="modified_date", required=False, widget=forms.DateTimeInput(attrs = {'class': 'form-control', 'placeholder': 'modified_date'}))
  address_id = forms.IntegerField(label="address_id", required=False, widget=forms.NumberInput(attrs = {'class': 'form-control', 'placeholder': 'address_id'}))
  floor = forms.IntegerField(label="floor", required=False, widget=forms.NumberInput(attrs = {'class': 'form-control', 'placeholder': 'floor'}))
  state_id = forms.ChoiceField(label="STATE_ID",choices=get_state_id(), required=False, widget=forms.Select(attrs = {'class': 'form-control', 'placeholder': 'STATE'}))
  
  
  class Meta:
    model = Storage
    fields = ('id', 'name','sap', 'sap_old', 'cat_id', 'subcat_id', 'state_id', 'owner_id', 'owner_name', 'resp_id', 'date_open', 'date_assign', 'model', 'serial_number', 'manufacturer', 'description', 'modified_date', 'address_id', 'floor',)

