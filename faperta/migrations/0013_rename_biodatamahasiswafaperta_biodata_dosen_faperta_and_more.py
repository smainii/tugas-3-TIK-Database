# Generated by Django 4.1.1 on 2022-10-11 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0012_nim_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Biodatamahasiswafaperta',
            new_name='Biodata_dosen_faperta',
        ),
        migrations.RenameModel(
            old_name='Biodatadosenfaperta',
            new_name='Biodata_mahasiswa_faperta',
        ),
        migrations.RenameModel(
            old_name='Biodatatendikfaperta',
            new_name='Biodata_tendik_faperta',
        ),
        migrations.RenameModel(
            old_name='Fakultasfaperta',
            new_name='Fakultas_faperta',
        ),
        migrations.RenameModel(
            old_name='Jurusanfaperta',
            new_name='Jurusan_faperta',
        ),
        migrations.RenameModel(
            old_name='MatKulfaperta',
            new_name='MatKul_faperta',
        ),
        migrations.RenameModel(
            old_name='Perkuliahanfaperta',
            new_name='Perkuliahan_faperta',
        ),
        migrations.RenameModel(
            old_name='Usertendikfaperta',
            new_name='User_dosen_faperta',
        ),
        migrations.RenameModel(
            old_name='Usermahasiswafaperta',
            new_name='User_mahasiswa_faperta',
        ),
        migrations.RenameModel(
            old_name='Userdosenfaperta',
            new_name='User_tendik_faperta',
        ),
        migrations.RemoveField(
            model_name='biodata_dosen_faperta',
            name='nim',
        ),
        migrations.RemoveField(
            model_name='biodata_mahasiswa_faperta',
            name='nip_id',
        ),
        migrations.AddField(
            model_name='biodata_dosen_faperta',
            name='nip_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faperta.nip'),
        ),
        migrations.AddField(
            model_name='biodata_mahasiswa_faperta',
            name='nim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faperta.nim'),
        ),
    ]