from django.shortcuts import render

# Create your views here.
def prodi5(request):
    judul = ["S1 Pendidikan Kedokteran", "S1 Gizi", "S1 Ilmu Keolahragaan", "D3 Keperawatan"]
    
    konteks = {
        'title': judul
    }
    return render(request, 'indexfk.html', konteks)
