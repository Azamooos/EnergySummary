from django.urls import path

from . import views

urlpatterns = [
    path('TotalSummary', views.totalSummary, name='TotalSummary'),
    path('YearlySummary', views.yearlySummary, name='YearlySummary'),
    path('WeeklySummary', views.weeklySummary, name='WeeklySummary'),
    path('LiveSummary', views.liveSummary, name='LiveSummary')
]