# Generated by Django 4.1.1 on 2022-10-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0007_jurusan_jurusanft'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodatadosenft',
            name='telepon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodatamahasiswaft',
            name='telepon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodatatendikft',
            name='telepon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
