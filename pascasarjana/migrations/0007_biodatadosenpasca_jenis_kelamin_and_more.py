# Generated by Django 4.1.1 on 2022-10-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pascasarjana', '0006_biodatadosenpasca_agama_biodatamahasiswapasca_agama_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodatadosenpasca',
            name='jenis_kelamin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatamahasiswapasca',
            name='jenis_kelamin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatatendikpasca',
            name='jenis_kelamin',
            field=models.CharField(max_length=20, null=True),
        ),
    ]