from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.


def homepage(request):
    # template = loader.get_template("homepage.html")
    # context = {}
    #
    # return HttpResponse(template.render(context, request))
    return render(
        request,
        "homepage.html",
        {"dane": "Ala ma kota",
         "a_list": [1,2,3,4,5,6]
        },

    )


def greetings(request):
    return HttpResponse("Hello")
