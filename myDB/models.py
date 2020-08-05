from django.db import models

class Storage(models.Model):
    sap = models.CharField(max_length=20, blank=True, null=True)
    sap_old = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=100)
    cat_id = models.IntegerField(blank=True, null=True)
    subcat_id = models.IntegerField(blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    owner_id = models.IntegerField(blank=True, null=True)
    owner_name = models.CharField(max_length=200, blank=True, null=True)
    resp_id = models.IntegerField(blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    date_assign = models.DateTimeField(blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    address_id = models.IntegerField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage'


class StorageCat(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'storage_cat'


class StorageResp(models.Model):
    user_id = models.IntegerField()
    firstname = models.CharField(max_length=100, blank=True, null=True)
    secondname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_resp'


class StorageState(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'storage_state'


class StorageSubcat(models.Model):
    name = models.CharField(max_length=50)
    cat_id = models.IntegerField()
    subcat_info = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'storage_subcat'