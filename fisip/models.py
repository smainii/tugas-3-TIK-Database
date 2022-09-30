from django.db import models

# Create your models here.
class Biodatadosenfisip(models.Model):
    nip = models.IntegerField()
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    photo = models.ImageField()
    email = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=50)
    alamat = models.TextField(null=True)

    def __str__(self):
        return self.nama

class Biodatatendikfisip(models.Model):
    nip = models.IntegerField()
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    photo = models.ImageField()
    email = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    alamat = models.TextField(null=True)

    def __str__(self):
        return self.nama

class Biodatamahasiswafisip(models.Model):
    nim = models.IntegerField()
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    photo = models.ImageField()
    email = models.CharField(max_length=100)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=50)
    alamat = models.TextField(null=True)

    def __str__(self):
        return self.nama