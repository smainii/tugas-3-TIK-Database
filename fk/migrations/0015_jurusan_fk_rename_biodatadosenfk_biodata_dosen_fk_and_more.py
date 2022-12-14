# Generated by Django 4.1.1 on 2022-10-11 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fk', '0014_nim_rename_nama_matkul_perkuliahanfk_nama_ruangan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jurusan_fk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('tanggal_berdiri', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('telepon', models.CharField(max_length=100)),
                ('alamat', models.TextField(null=True)),
                ('kode_jurusan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fk.jurusan')),
            ],
        ),
        migrations.RenameModel(
            old_name='Biodatadosenfk',
            new_name='Biodata_dosen_fk',
        ),
        migrations.RenameModel(
            old_name='Biodatamahasiswafk',
            new_name='Biodata_mahasiswa_fk',
        ),
        migrations.RenameModel(
            old_name='Biodatatendikfk',
            new_name='Biodata_tendik_fk',
        ),
        migrations.RenameModel(
            old_name='Jurusanfk',
            new_name='Fakultas_fk',
        ),
        migrations.RenameModel(
            old_name='MatKulfk',
            new_name='MatKul_fk',
        ),
        migrations.RenameModel(
            old_name='Perkuliahanfk',
            new_name='Perkuliahan_fk',
        ),
        migrations.RenameModel(
            old_name='Userdosenfk',
            new_name='User_dosen_fk',
        ),
        migrations.RenameModel(
            old_name='Usertendikfk',
            new_name='User_mahasiswa_fk',
        ),
        migrations.RenameModel(
            old_name='Usermahasiswafk',
            new_name='User_tendik_fk',
        ),
        migrations.RemoveField(
            model_name='fakultas_fk',
            name='kode_jurusan',
        ),
        migrations.RemoveField(
            model_name='user_mahasiswa_fk',
            name='nip_id',
        ),
        migrations.RemoveField(
            model_name='user_tendik_fk',
            name='nim_id',
        ),
        migrations.AddField(
            model_name='fakultas_fk',
            name='kode_fakul',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fk.fakultas'),
        ),
        migrations.AddField(
            model_name='user_mahasiswa_fk',
            name='nim_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fk.nim'),
        ),
        migrations.AddField(
            model_name='user_tendik_fk',
            name='nip_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fk.nip'),
        ),
        migrations.DeleteModel(
            name='Fakultasfk',
        ),
    ]
