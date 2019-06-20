from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from interviews import views as interviewsViews
from jobs import views as jobsViews
from candidates import views as candidatesViews
from recruiters import views as recruitersViews
from dashboards import views as dashboardViews
from django.contrib.auth.models import User

urlpatterns = [
    path('', dashboardViews.dashboards, name='dashboards'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('jobs/', jobsViews.view_jobs, name='jobs'),
    path('jobs/<str:job_id>/', jobsViews.view_job_details, name='job_details'),
    path('candidates/apply/', candidatesViews.apply, name='candidate_apply'),
    path('candidates/apply/success/', candidatesViews.apply_success, name='candidate_apply_success'),    
    path('recruiters/', recruitersViews.view_recruiters, name='recruiters'), 
    path('available/<str:bu_id>/', interviewsViews.available, name='available'),
    path('availability/<str:bu_id/', interviewsViews.availability, name='availability'),
    path('interviews/', interviewsViews.interview_requests, name='interviews')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)