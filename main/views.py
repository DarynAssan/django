from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tagam, Un, Negizgi, Susyn, Tatty, Salat, Commentary, Tapsyrys
from django.views import View
from .forms import Con, Tapy


def index(request):
    tagam = Tagam.objects.all()
    return render(request, 'main/index.html', {'Tagam_list': tagam})


def index9(request):
    commentary = Commentary.objects.all()
    return render(request, 'main/index9.html', {'Commentary_list': commentary})


def index1(request):
    un = Un.objects.all()
    return render(request, 'main/index1.html',  {'Un_list': un})


def index2(request):
    negizgi = Negizgi.objects.all()
    return render(request, 'main/index2.html',  {'Negizgi_list': negizgi})


def index3(request):
    susyn = Susyn.objects.all()
    return render(request, 'main/index3.html',  {'Susyn_list': susyn})


def index4(request):
    tatty = Tatty.objects.all()
    return render(request, 'main/index4.html',  {'Tatty_list': tatty})


def index5(request):
    salat = Salat.objects.all()
    return render(request, 'main/index5.html',  {'Salat_list': salat})


def index6(request):
    tapsyrys = Tapsyrys.objects.all()
    return render(request, 'main/index6.html', {'Tapsyrys_list': tapsyrys} )


def index7(request):
    return render(request, 'main/index7.html')


def index8(request):
    return render(request, 'main/index8.html')


class Com(View):
    def post(self, request):
        form = Con(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/9')


class Tap(View):
    def post(self, request):
        form = Tapy(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/6')
