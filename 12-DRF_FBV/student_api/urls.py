from django.urls import path
from .views import (home, student_list, student_create, student_detail, student_update, student_delete, student_list_create, student_detail_update_delete)

urlpatterns = [
    path('', home),
    path('student_list/', student_list),  # listele
    path('student_create/', student_create),  # yeni kayit
    path('student_detail/<int:pk>', student_detail),  # tek kayit goruntuleme
    path('student_update/<int:pk>', student_update),  # tek kayit guncelleme
    path('student_delete/<int:pk>', student_delete),  # tek kayit silme
    # Fonksiyonların birleşmiş halleri:
    path('student_list_create/', student_list_create),
    path('student_detail_update_delete/<int:pk>', student_detail_update_delete),
    ]