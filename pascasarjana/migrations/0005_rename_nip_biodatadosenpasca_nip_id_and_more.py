# Generated by Django 4.1.1 on 2022-09-30 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pascasarjana', '0004_nip_alter_biodatadosenpasca_nip_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biodatadosenpasca',
            old_name='nip',
            new_name='nip_id',
        ),
        migrations.RenameField(
            model_name='biodatatendikpasca',
            old_name='nip',
            new_name='nip_id',
        ),
    ]
