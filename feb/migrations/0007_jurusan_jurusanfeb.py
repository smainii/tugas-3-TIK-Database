# Generated by Django 4.1.1 on 2022-10-08 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feb', '0006_biodatadosenfeb_agama_biodatadosenfeb_jenis_kelamin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jurusanfeb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('tanggal_berdiri', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('telepon', models.CharField(max_length=100)),
                ('alamat', models.TextField(null=True)),
                ('kode_jurusan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feb.jurusan')),
            ],
        ),
    ]
