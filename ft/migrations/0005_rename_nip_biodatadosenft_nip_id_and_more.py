# Generated by Django 4.1.1 on 2022-09-30 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0004_nip_alter_biodatadosenft_nip_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='biodatadosenft',
            old_name='nip',
            new_name='nip_id',
        ),
        migrations.RenameField(
            model_name='biodatatendikft',
            old_name='nip',
            new_name='nip_id',
        ),
    ]
