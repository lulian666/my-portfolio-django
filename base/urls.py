from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('project/<str:pk>', views.project_page, name='project'),
    path('add-project', views.add_project, name='add-project'),
    path('edit-project/<str:pk>', views.edit_project, name='edit-project'),
    path('inbox', views.inbox, name='inbox'),
    path('message/<str:pk>', views.message_detail, name='message'),
    path('add-skill', views.add_skill, name='add-skill'),
    path('add-endorsement', views.add_endorsement, name='add-endorsement'),
    path('donation', views.donation_page, name='donation'),
    path('chart', views.chart_page, name='chart'),
]
