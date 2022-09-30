# Generated by Django 4.1.1 on 2022-09-30 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feb', '0003_biodatamahasiswafeb_alamat_and_more'),
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
            model_name='biodatadosenfeb',
            name='nip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feb.nip'),
        ),
        migrations.AlterField(
            model_name='biodatatendikfeb',
            name='nip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feb.nip'),
        ),
    ]