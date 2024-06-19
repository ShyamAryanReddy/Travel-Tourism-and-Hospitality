from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models


# Create your views here.

def home(request):
    return render(request, 'home.html')


def courses(request):
    return render(request, 'courses.html')


def bookings(request):
    dests = models.Destination.objects.all()
    return render(request, 'bookings.html', {'dests': dests})


def profile(request):
    current_user = request.user
    username = current_user.username
    userDestinations = models.UserDestinations.objects.filter(username=username).values()
    return render(request, 'profile.html', {'userDestinations': userDestinations})


def course(request, coursetype):
    if coursetype == "Travel":
        courses = models.Travel_courses.objects.all()
    elif coursetype == "Tourism":
        courses = models.Tourism_courses.objects.all()
    elif coursetype == "Hospitality":
        courses = models.Hospitality_courses.objects.all()
    return render(request, 'course.html', {'courses': courses, 'coursetype': coursetype})


def hotels(request):
    city = request.GET.get('data')
    txt = city.split()
    dest = txt[0]
    cprice = txt[1]
    hotels = models.Hotel.objects.all()
    c = models.Destination.objects.get(name=dest)
    c.clicks = c.clicks + 1
    c.save()
    return render(request, 'hotel.html', {'dest': dest, 'cprice': cprice, 'hotels': hotels})


def addUserDestination(request):
    data = request.GET.get('data')
    if data != None:
        txt = data.split()
        current_user = request.user
        username = current_user.username
        city = txt[0]
        cprice = int(txt[1])
        hotel = txt[2]
        hprice = int(txt[3])
        price = cprice + hprice
        userDestination = models.UserDestinations(username=username, city=city, hotel=hotel, price=price, date=datetime.now())
        userDestination.save()
        messages.success(request, 'Destination saved successfully')
        return redirect('profile')
    else:
        return redirect('bookings')


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels = models.Destination.objects.values_list('name', flat=True)
        chartLabel = "City statics"
        chartdata = models.Destination.objects.values_list('clicks', flat=True)
        data = {
            "labels": labels,
            "chartLabel": chartLabel,
            "chartdata": chartdata,
        }
        return Response(data)
