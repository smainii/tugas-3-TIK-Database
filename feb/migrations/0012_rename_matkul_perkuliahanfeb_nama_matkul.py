# Generated by Django 4.1.1 on 2022-10-08 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feb', '0011_rename_perkuliahanfaperta_perkuliahanfeb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perkuliahanfeb',
            old_name='matkul',
            new_name='nama_matkul',
        ),
    ]