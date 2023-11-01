from django.urls import path
from .import views

urlpatterns = [
    path('', views.Index, name="home"),
    path('newsletter/', views.newsletter_info, name="newsletter"),
    path('faq/', views.questions, name="faq"),
    

]