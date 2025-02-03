from django.shortcuts import render

def index(request):
    return render(request, 'buku/index.html')

def daftar_buku(request):
    return render(request, 'buku/daftar_buku.html')

def peminjaman_buku(request):
    return render(request, 'buku/peminjaman_buku.html')
