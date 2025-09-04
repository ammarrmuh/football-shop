from django.shortcuts import render

def show_main(request):
    context = {
        'Nama_Aplikasi' : 'Football Shop',
        'nama': 'Ammar muhammad Rafif',
        'kelas': 'PBP C'
    }

    return render(request, "main.html", context)
