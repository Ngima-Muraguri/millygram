from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path, re_path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django_registration.backends.one_step.views import RegistrationView
# from django.core.urlresolvers import reverse_lazy


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path(r'home/', views.home, name='home'),
    path(r'search/', views.search, name='search'),
    path(r'image/<int:image_id>', views.single_image, name='image'),
    path(r'post/', views.new_post, name='post'),
    path(r'profile/', views.profile, name='profile'),
    path(r'editprofile/', views.edit_profile, name='editprofile'),
    path(r'comment/', views.comment, name='comment'),

    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('accounts/register/',
        RegistrationView.as_view(success_url=reverse_lazy('home')),
        name='django_registration_register'),

    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'), 
    re_path(r'^login/$', LoginView.as_view(), {"next_page": '/'}),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)