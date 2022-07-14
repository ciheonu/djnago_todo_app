from django.conf import settings
from django.conf.urls.static import static
from accounts import views as user_views
from profiles import views as profile_views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Todo Admin'
admin.site.site_title = 'Todo Admin'
admin.site.index_title = 'Todo Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoapp.urls')),
    path('profile/', profile_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)