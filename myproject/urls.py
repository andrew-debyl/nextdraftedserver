from django.contrib import admin
from django.urls import path
from . import views
from .views import ProfileUpdateView, PortfolioUpdateView, PortfolioItemPostView, PortfolioItemUpdateView
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
    path('portfolios/<str:username>/<str:portfolioId>', view=views.get_portfolio, name='get_portfolio'),
    path('portfolios/<str:username>/<str:portfolioId>/update', PortfolioUpdateView.as_view(), name='update_portfolio'),
    path('portfolios/<str:username>/<str:portfolioId>/items', PortfolioItemPostView.as_view(), name='portfolio_itemlist_put'),
    path('portfolios/<str:username>/<str:portfolioId>/items/<str:item_id>', PortfolioItemUpdateView.as_view(), name='portfolio_itemlist_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)