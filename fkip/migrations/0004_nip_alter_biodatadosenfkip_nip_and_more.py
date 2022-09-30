# Generated by Django 4.1.1 on 2022-09-30 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fkip', '0003_biodatamahasiswafkip_alamat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('keterangan', models.TextField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='biodatadosenfkip',
            name='nip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fkip.nip'),
        ),
        migrations.AlterField(
            model_name='biodatatendikfkip',
            name='nip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fkip.nip'),
        ),
    ]