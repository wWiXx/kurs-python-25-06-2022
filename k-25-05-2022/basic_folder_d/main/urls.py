from django.urls import path

from main.views import homepage, greetings

urlpatterns = [
    path("", homepage, name="homepage"),
    path("greetings/", greetings),
]
