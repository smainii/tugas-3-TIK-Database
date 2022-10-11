# Generated by Django 4.1.1 on 2022-10-11 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fk', '0012_rename_matkul_perkuliahanfk_nama_matkul'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fakultasfk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('tanggal_berdiri', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('telepon', models.CharField(max_length=100)),
                ('alamat', models.TextField(null=True)),
                ('kode_fakul', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fk.fakultas')),
            ],
        ),
    ]
