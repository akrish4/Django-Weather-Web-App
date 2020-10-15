from django.contrib import admin
from django.urls import path,include
from app import views
from django.contrib.auth import views as auth_views


urlpatterns = [
  path('',views.index,name='index'),
  path('contact',views.contact,name='contact'),
  path('about',views.about,name='about'),
  path('handleBlog',views.handleBlog,name='handleBlog'),
  path('weather',views.weather,name='weather'),
  path('signUp',views.signUp,name='signUp'),
  path('login',views.handlelogin,name='handlelogin'),
  path('logout',views.handlelogout,name='handlelogout'),
  path('search',views.search,name='search'),
  #path('change-password/', auth_views.PasswordChangeView.as_view()),
  #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
     #   name='password_change_complete'),

 # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'),name='password_change'),
 # path('password-reset/',
  #       auth_views.PasswordResetView.as_view(
  #           template_name='registration/password_reset.html'
  #       ),
    #     name='password_reset'),
 # path('password-reset/done/',
    #     auth_views.PasswordResetDoneView.as_view(
     #        template_name='registration/password_reset_done.html'
      #   ),
       #  name='password_reset_done'),
  #path('password-reset-confirm/<uidb64>/<token>/',
   #      auth_views.PasswordResetConfirmView.as_view(
   #          template_name='registration/password_reset_confirm.html'
   #      ),
   #      name='password_reset_confirm'),
  #path('password-reset-complete/',
   #      auth_views.PasswordResetCompleteView.as_view(
    #         template_name='registration/password_reset_complete.html'
     #    ),
      #   name='password_reset_complete'),
  #path('password_change/', auth_views.PasswordChangeView.as_view()),
]

