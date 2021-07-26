from django.conf.urls import url,include
from django.contrib import admin
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('home.urls')),
    url(r'^accounts/register/',RegistrationView.as_view(success_url='/accounts/login/'),name='django_registration_register'),
    url(r'^accounts/', include('django_registration.backends.one_step.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]