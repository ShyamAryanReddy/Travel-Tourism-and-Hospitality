from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses', views.courses, name='courses'),
    path('bookings', views.bookings, name='bookings'),
    path('hotels', views.hotels, name='hotels'),
    path('profile', views.profile, name='profile'),
    path('courses/<coursetype>', views.course, name='course'),
    path('addUserDestination', views.addUserDestination, name='addUserDestination'),
    path('charthome', views.HomeView.as_view()),
    path('charthome/api', views.ChartData.as_view()),
]