# Generated by Django 4.1.1 on 2022-10-08 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ft', '0009_matkul_matkulft'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perkuliahanfaperta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matkul', models.CharField(max_length=100)),
                ('jurusan', models.CharField(max_length=50)),
                ('dosen', models.CharField(max_length=100)),
                ('kode_ruangan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ft.kelas')),
            ],
        ),
    ]
