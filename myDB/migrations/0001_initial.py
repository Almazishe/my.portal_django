# Generated by Django 3.1 on 2020-08-05 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sap', models.CharField(blank=True, max_length=20, null=True)),
                ('sap_old', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(max_length=100)),
                ('cat_id', models.IntegerField(blank=True, null=True)),
                ('subcat_id', models.IntegerField(blank=True, null=True)),
                ('state_id', models.IntegerField(blank=True, null=True)),
                ('owner_id', models.IntegerField(blank=True, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=200, null=True)),
                ('resp_id', models.IntegerField(blank=True, null=True)),
                ('date_open', models.DateTimeField(blank=True, null=True)),
                ('date_assign', models.DateTimeField(blank=True, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('address_id', models.IntegerField(blank=True, null=True)),
                ('floor', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'storage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StorageCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'storage_cat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StorageResp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('secondname', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'storage_resp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StorageState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'storage_state',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StorageSubcat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cat_id', models.IntegerField()),
                ('subcat_info', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'storage_subcat',
                'managed': False,
            },
        ),
    ]