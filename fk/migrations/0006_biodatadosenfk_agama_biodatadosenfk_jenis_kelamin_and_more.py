# Generated by Django 4.1.1 on 2022-10-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fk', '0005_rename_nip_biodatadosenfk_nip_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodatadosenfk',
            name='agama',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatadosenfk',
            name='jenis_kelamin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatamahasiswafk',
            name='agama',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatamahasiswafk',
            name='jenis_kelamin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatatendikfk',
            name='agama',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatatendikfk',
            name='jenis_kelamin',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
