# Generated by Django 4.1.1 on 2022-09-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisip', '0002_alter_biodatadosenfisip_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodatamahasiswafisip',
            name='alamat',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='biodatadosenfisip',
            name='alamat',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='biodatatendikfisip',
            name='alamat',
            field=models.TextField(null=True),
        ),
    ]
