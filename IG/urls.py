from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views



urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('image/<int:image_id>', views.single_image, name='image'),
    path('post/', views.new_post, name='post'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.edit_profile, name='editprofile'),
    path('comment/', views.comment, name='comment'),
     

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)