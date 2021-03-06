# Generated by Django 2.2.20 on 2021-04-09 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='upload_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=250)),
                ('date', models.IntegerField(max_length=100)),
                ('file_field', models.DateField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=100)),
                ('number_of_elements', models.IntegerField(max_length=100)),
                ('price', models.IntegerField(max_length=100)),
                ('Upload_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manage_inventory.upload_file')),
            ],
        ),
    ]
