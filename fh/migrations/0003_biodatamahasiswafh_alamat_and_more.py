# Generated by Django 4.1.1 on 2022-09-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fh', '0002_alter_biodatadosenfh_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodatamahasiswafh',
            name='alamat',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='biodatadosenfh',
            name='alamat',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='biodatatendikfh',
            name='alamat',
            field=models.TextField(null=True),
        ),
    ]
