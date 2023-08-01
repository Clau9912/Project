from django.shortcuts import render
from django.http import HttpResponse

from django.conf import settings
from django.core.files.storage import FileSystemStorage




# Create your views here.s
def file(request) :
    return render(request, "FileUpload/home.html")


def categorias(request) :
    count = 0
    if request.method == "POST" and request.FILES["mfile"]:
        mfile = request.FILES["mfile"]
        fs = FileSystemStorage()
        fnn = fs.save(mfile.name, mfile)
        upload_file_url = fs.url(mfile)
        value1 = request.POST["mb"]
        value2 = request.POST["category"]
        count += 1
        return render(request, "FileUpload/categorias.html",
                      {"upload_file_url" : upload_file_url, "value1" : value1, "value2" : value2, "cont" : count})
    return render(request, "FileUpload/home.html")


