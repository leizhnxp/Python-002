from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from .models import ShortComment


def index(request):
    return HttpResponse("Hello there Django routes !")


def homework(request):
    #
    short_comments = ShortComment.objects.filter(stars__gte=1)[2:5:2]
    return render(request, 'index.html', locals())
