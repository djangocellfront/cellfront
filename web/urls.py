from django.urls import path
from web import views

urlpatterns = [
    path("", views.index, name="index"),
    path("upgrade-chart/", views.upgrade_chart, name="upgrade-chart"),
]
