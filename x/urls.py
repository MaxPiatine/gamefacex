from django.urls import path
from x import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('alfy', views.alfy, name='alfy'),
    path('folkhen', views.folkhen, name='folkhen'),
    path('kingboozer', views.kingboozer, name='kingboozer'),
    path('kingland', views.kingland, name='kingland'),
    path('mudbuddy', views.mudbuddy, name='mudbuddy'),
    path('work', views.work_page, name='work_page'),
    path('services', views.service_page, name='service_page'),
    path('quote', views.quote, name='quote'),
    path('insights', views.insights_page, name='insights_page'),
    path('partner', views.partner_page, name='partner_page'),
    path('partner-sent', views.partner_sign_up, name='partner-sent'),
    path('gfx-story', views.gfx_story_page, name='gfx_story_page'),
    path('quote-sent', views.sending_quote, name='sent-quote')
]