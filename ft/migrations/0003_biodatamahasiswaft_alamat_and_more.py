# Generated by Django 4.1.1 on 2022-09-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0002_alter_biodatadosenft_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodatamahasiswaft',
            name='alamat',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='biodatadosenft',
            name='alamat',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='biodatatendikft',
            name='alamat',
            field=models.TextField(null=True),
        ),
    ]