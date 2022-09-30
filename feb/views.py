from turtle import title
from django.shortcuts import render

# Create your views here.
def prodi2(request):
    judul = ["S1 Akuntansi", "S1 Ilmu Ekonomi Pembangunan", "S1 Manajemen", "S1 Ekonomi Syariah", "D3 Keuangan Perbankan", "D3 Akuntansi", "D3 Perpajakan", "D3 Pemasaran"]
    
    konteks = {
        'title': judul
    }
    return render(request, 'feb/index.html', konteks)