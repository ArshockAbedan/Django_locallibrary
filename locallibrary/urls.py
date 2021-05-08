"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# Use include() to add paths from the catalog application
from django.urls import include
# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('catalog/', include('catalog.urls')),
                  path('', RedirectView.as_view(url='catalog/')),
                  # Add Django site authentication urls (for login, logout, password management)
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('accounts/', RedirectView.as_view(url='login/'), name='login'),
                  path('accounts/', RedirectView.as_view(url='logout/'), name='logout'),
                  path('accounts/', RedirectView.as_view(url='password_change/'), name='password_change'),
                  path('accounts/', RedirectView.as_view(url='password_change/done/'), name='password_change_done'),
                  path('accounts/', RedirectView.as_view(url='password_reset/'), name='password_reset'),
                  path('accounts/', RedirectView.as_view(url='password_reset/done/'), name='password_reset_done'),
                  path('accounts/', RedirectView.as_view(url='reset/<uidb64>/<token>/'), name='password_reset_confirm'),
                  path('accounts/', RedirectView.as_view(url='reset/done/'), name='password_reset_complete'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# path('accounts/ logout/ [name='logout']
# path('accounts/ password_change/ [name='password_change']
# path('accounts/ password_change/done/ [name='password_change_done']
# path('accounts/ password_reset/ [name='password_reset']
# path('accounts/ password_reset/done/ [name='password_reset_done']
# path('accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# path('accounts/ reset/done/ [name='password_reset_complete']

