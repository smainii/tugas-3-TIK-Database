# Generated by Django 4.1.1 on 2022-10-08 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0005_rename_nip_biodatadosenft_nip_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodatadosenft',
            name='agama',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatadosenft',
            name='jenis_kelamin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatamahasiswaft',
            name='agama',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatamahasiswaft',
            name='jenis_kelamin',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatatendikft',
            name='agama',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='biodatatendikft',
            name='jenis_kelamin',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
