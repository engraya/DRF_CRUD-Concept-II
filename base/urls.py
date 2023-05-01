from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('programmingLanguageList/', views.ProgrammingLanguageList.as_view()),
    path('programmingLanguageCreate/', views.ProgrammingLanguageCreate.as_view()),
    path('programmingLanguageDetail/<int:pk>/', views.ProgrammingLanguageDetail.as_view()),
    path('programmingLanguageUpdate/<int:pk>/', views.ProgrammingLanguageUpdate.as_view()),
    path('programmingLanguageDelete/<int:pk>/', views.ProgrammingLanguageDelete.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)