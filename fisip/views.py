from django.shortcuts import render

# Create your views here.
def prodi4(request):
    judul = ["Administrasi Publik", "Ilmu Komunikasi", "Ilmu Pemerintah"]

    konteks = {
        'title': judul
    }
    return render(request, 'indexfisip.html', konteks)
