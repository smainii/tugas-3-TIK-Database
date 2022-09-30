from django.shortcuts import render

# Create your views here.
def prodi8(request):
    judul = ["Doktor Pendidikan", "Doktor Ilmu Akuntansi", "Doktor Ilmu Pertanian", "Pendidikan Bahasa Indonesia", "Magister Ilmu Hukum", "Magister Ilmu Pertanian", "Magister Administrasi Publik", "Magister Akuntansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Teknologi Pendidikan", "Magister Pendidikan Dasar", "Magister Ekonomi"]
    
    konteks = {
        'title': judul
    }
    return render(request, 'indexpasca.html', konteks)
