# Generated by Django 4.1.1 on 2022-10-08 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fkip', '0007_jurusan_jurusanfkip'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodatadosenfkip',
            name='telepon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodatamahasiswafkip',
            name='telepon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodatatendikfkip',
            name='telepon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
