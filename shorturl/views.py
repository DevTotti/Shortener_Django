from django.shortcuts import render,redirect
from .models import Mainurl
from .form import UrlForm
from django.http import HttpResponse, HttpResponseNotFound
from .shorten import shorten_url

# Create your views here.
def homepage( request, *args, **kwargs):
    request_host = request.get_host()

    if request.method == 'GET':
        form = UrlForm()
        url_data = {
        "encoded": "",
        "original_url": ""
        }
        context = {
            "form":form,
            "url":url_data
        }


    elif request.method == 'POST':
        form = UrlForm()
        formdata = request.POST
        original_url = formdata["original_url"]

        url_data = shorten_url(request_host, original_url)

        newUrl_ = Mainurl(**url_data)

        newUrl_.save()

        full_encoded = "http://"+str(request_host) + '/'+url_data["encoded"]

        url_data["encoded"] = full_encoded

        context = {
            "form":form,
            "url":url_data
        }


    return render(request, 'index.html', context)



def accessPage(request, short_url):
    if request.method == 'GET':
        try:
            url_data = Mainurl.objects.filter(encoded=str(short_url)).values('original_url')
            original_url = url_data[0]['original_url']
            
            return redirect(original_url)

        except Exception as error:
            print(error)
            return HttpResponse(status=400)
    
    else:
        return render(request, 'index.html',{})

        
