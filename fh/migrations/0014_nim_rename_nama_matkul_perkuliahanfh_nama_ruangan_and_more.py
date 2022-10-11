# Generated by Django 4.1.1 on 2022-10-11 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fh', '0013_fakultas_fakultasfh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.TextField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='perkuliahanfh',
            old_name='nama_matkul',
            new_name='nama_ruangan',
        ),
        migrations.CreateModel(
            name='Usertendikfh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('nip_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fh.nip')),
            ],
        ),
        migrations.CreateModel(
            name='Usermahasiswafh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('nim_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fh.nim')),
            ],
        ),
        migrations.CreateModel(
            name='Userdosenfh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('nip_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fh.nip')),
            ],
        ),
        migrations.AlterField(
            model_name='biodatamahasiswafh',
            name='nim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fh.nim'),
        ),
    ]
