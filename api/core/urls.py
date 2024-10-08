from django.urls import path
from .views import CutCreateView
from .views_func import create_person, create_cut, person_list, cut_list, cut_detail, person_detail

views_func_urlpatterns = [
    path('person_list/', person_list, name='person_list'),
    path('create_person/', create_person, name='create_person'),
    path('create_cut/', create_cut, name='create_cut'),
    path('cut_list/', cut_list, name='cut_list'),
    path('cut/<str:cut_code>/', cut_detail, name='cut_detail'),
    path('person/<int:pk>/', person_detail, name='person_detail'),
]

urlpatterns = [
    path('cut-create-drf/', CutCreateView.as_view(), name='cut-create-drf'),
    
] + views_func_urlpatterns

