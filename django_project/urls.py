from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.urls import path, include
from django.conf import settings

# serving media files in DEBUG=FALSE mode, not appropriate for production
from django.views.static import serve
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),

    path('reset-password/', auth_views.PasswordResetView.as_view(
                                                                    template_name='users/reset_password.html',
                                                                    subject_template_name='users/password_reset_subject.txt',
                                                                    email_template_name='users/password_reset_email.html'
                                                                    #success_url='/login/',
                                                                    ), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'), # using a custom logout function
    path('', include('blog.urls')),
    path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), # serving media files in DEBUG=FALSE mode

]
