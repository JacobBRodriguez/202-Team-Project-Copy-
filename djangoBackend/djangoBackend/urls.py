"""djangoBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import Team_5.views as views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index_view),
    path('index.html', views.index_view),
    path('login.html', views.login_view),
    path('services.html', views.services_view),
    path('searching.html', views.searching_view),
    path('posting.html', views.posting_view),
    path('approve_listing.html', views.approve_listing_view),
    path('offers.html', views.offers_view),
    path('remove_user.html', views.remove_user_view),
    path('send_offer.html', views.send_offer_view, name="send_offer"),
    path('sign-up.html', views.sign_up_view),
    path('logout', views.logout_view),
    path('determine_route_index', views.determine_route_index_view),
    path('query', views.search_view),
    path('favorites.html', views.favorite_list),
    path('<str:listing_id>', views.single_view, name="single"),
    path('favorite/<str:listing_id>', views.favorite_post, name="favorite_post"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


