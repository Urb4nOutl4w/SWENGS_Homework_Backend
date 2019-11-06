from django.urls import path
from swengs.songs import views

urlpatterns = [
    path('song/', views.song_list),
    path('song/<int:song_id>', views.song_update),
]