from django.contrib import admin
from django.urls import path
from buku.views import index, daftar_buku, peminjaman_buku  # Import the new views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # URL pattern for index
    path('daftar_buku/', daftar_buku, name='daftar_buku'),  # URL pattern for daftar_buku
    path('peminjaman_buku/', peminjaman_buku, name='peminjaman_buku'),  # URL pattern for peminjaman_buku
]
