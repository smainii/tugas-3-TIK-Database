# Generated by Django 4.1.1 on 2022-09-30 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fkip', '0004_nip_alter_biodatadosenfkip_nip_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biodatadosenfkip',
            old_name='nip',
            new_name='nip_id',
        ),
        migrations.RenameField(
            model_name='biodatatendikfkip',
            old_name='nip',
            new_name='nip_id',
        ),
    ]
