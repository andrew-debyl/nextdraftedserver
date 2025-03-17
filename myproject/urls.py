from django.contrib import admin
from django.urls import path
from . import views
from .views import ProfileUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', view=views.login_user, name='login'),
    path('signup', view=views.signup_user, name='signup'),
    path('logout', view=views.logout_request, name='logout'),
    path('create_role', view=views.create_role, name='createrole'),
    path('profile/<str:username>', view=views.get_profile, name='get_profile'),
    path('profile/<str:username>/update', ProfileUpdateView.as_view(), name='update_profile'),
    path('portfolios/<str:username>', view=views.get_portfolios, name='get_portfolios'),
    path('portfolios/<str:username>/<str:portfolioId>', view=views.get_portfolio, name='get_portfolio')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)