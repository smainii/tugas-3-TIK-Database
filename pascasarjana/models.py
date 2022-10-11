from django.db import models

# Create your models here.
class Fakultas(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField(null=True)

    def __str__(self):
        return self.nama

class Jurusan(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField(null=True)

    def __str__(self):
        return self.nama

class MatKul(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField(null=True)

    def __str__(self):
        return self.nama

class Kelas(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField(null=True)

    def __str__(self):
        return self.nama

class Nip(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField(null=True)

    def __str__(self):
        return self.nama

class Nim(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField(null=True)

    def __str__(self):
        return self.nama

class Fakultas_pasca(models.Model):
    kode_fakul = models.ForeignKey(Fakultas, on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=100)
    tanggal_berdiri = models.DateField()
    email = models.CharField(max_length=100)
    telepon = models.CharField(max_length=100)
    alamat = models.TextField(null=True)

    def __str__(self):
        return self.nama

class Jurusan_pasca(models.Model):
    kode_jurusan = models.ForeignKey(Jurusan, on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=100)
    tanggal_berdiri = models.DateField()
    email = models.CharField(max_length=100)
    telepon = models.CharField(max_length=100)
    alamat = models.TextField(null=True)

    def __str__(self):
        return self.nama

class MatKul_pasca(models.Model):
    kode_MatKul = models.ForeignKey(MatKul, on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

class Perkuliahan_pasca(models.Model):
    kode_ruangan = models.ForeignKey(Kelas, on_delete=models.CASCADE, null=True)
    nama_ruangan = models.CharField(max_length=100)
    jurusan = models.CharField(max_length=50)
    dosen = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_ruangan

class Biodata_dosen_pasca(models.Model):
    nip_id = models.ForeignKey(Nip, on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=20, null=True)
    agama = models.CharField(max_length=20, null=True)
    photo = models.ImageField()
    email = models.CharField(max_length=100)
    telepon = models.CharField(max_length=100, null=True)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=50)
    alamat = models.TextField(null=True)

    def __str__(self):
        return self.nama

class User_dosen_pasca(models.Model):
    nip_id = models.ForeignKey(Nip, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

class Biodata_tendik_pasca(models.Model):
    nip_id = models.ForeignKey(Nip, on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=20, null=True)
    agama = models.CharField(max_length=20, null=True)
    photo = models.ImageField()
    email = models.CharField(max_length=100)
    telepon = models.CharField(max_length=100, null=True)
    unit = models.CharField(max_length=100)
    alamat = models.TextField(null=True)

    def __str__(self):
        return self.nama

class User_tendik_pasca(models.Model):
    nip_id = models.ForeignKey(Nip, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username

class Biodata_mahasiswa_pasca(models.Model):
    nim = models.ForeignKey(Nim, on_delete=models.CASCADE, null=True)
    nama = models.CharField(max_length=100)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=20, null=True)
    agama = models.CharField(max_length=20, null=True)
    photo = models.ImageField()
    email = models.CharField(max_length=100)
    telepon = models.CharField(max_length=100, null=True)
    fakultas = models.CharField(max_length=100)
    prodi = models.CharField(max_length=50)
    alamat = models.TextField(null=True)
    agama = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.nama

class User_mahasiswa_pasca(models.Model):
    nim_id = models.ForeignKey(Nim, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username