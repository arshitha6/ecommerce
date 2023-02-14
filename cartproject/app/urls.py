from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from app import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
app_name='app'
urlpatterns = [
    path('',views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='app:login'),name='logout'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
