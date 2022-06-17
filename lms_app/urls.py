

from django.urls import path
from lms_app.views import apply_leave, Inactive_permission, Inactive_role, active, active_permission, active_role, apply_leave, approve, create_leave_type, home, leave, list_view_Role, list_view_leave, login, signup_view, sinup, unapprove, update_appyleave, update_leave_type, updateuser, create_permission, create_role, update_Permssion, update_role, user_change_password, signout, Inactive, updateuser_reporting_manager

from django.contrib.auth import views


urlpatterns = [
    path('', home, name='home'),

    path('login/', login, name='login'),
    path('updateuser/', updateuser, name='updateuser'),
    path('update/<int:id>/', updateuser_reporting_manager,
         name='updateuser_reporting_manager'),
    path('changepassword/', user_change_password, name='changepassword'),
    #     path('createrole/', create_role, name='createrole'),

    path('sinup/', sinup, name='sinup'),
    path('signup_view/', signup_view, name='signup_view'),
    path('logout/', signout, name='signout'),
    path('active/<int:id>/',
         active, name='active'),
    path('Inactive/<int:id>/',
         Inactive, name='active'),

    # forget password
    path('reset_password/', views.PasswordResetView.as_view(
        template_name="password_reset/reset_password.html"), name='reset_password'),
    path('reset_password_sent/', views.PasswordResetDoneView.as_view(
        template_name="password_reset/password_reset_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', views.PasswordResetConfirmView.as_view(
        template_name="password_reset/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', views.PasswordResetCompleteView.as_view(
        template_name="password_reset/password_reset_done.html"), name='password_reset_complete'),

    path('create_permission/', create_permission, name='create_permission'),
    path('update_permission/<int:id>/',
         update_Permssion, name='update_permission'),
    path('active_permission/<int:id>/',
         active_permission, name='active_permission'),
    path('Inactive_permission/<int:id>/',
         Inactive_permission, name='inactive_permission'),


    path('list_view_role/', list_view_Role, name='list_view_Role'),
    path('create_role/', create_role, name='create_role'),
    path('update_role/<int:id>/', update_role, name='update_role'),
    path('active_role/<int:id>/',
         active_role, name='active_role'),
    path('Inactive_role/<int:id>/',
         Inactive_role, name='inactive_role'),


    path('list_view_leave/', list_view_leave, name='list_view_leave'),

    path('create_leave_type/', create_leave_type, name='create_leave_type'),
    path('update_leave_type/<int:id>/',
         update_leave_type, name='update_leave_type'),
    #     path('list_view_leave/update_leave_type/<int:id>/',
    #          update_leave_type, name='update_leave_type'),


    path('leave/', leave, name='leave'),
    path('apply_leave/', apply_leave, name='apply_leave'),
    path('update_appyleave/<int:id>/', update_appyleave, name='update_appyleave'),

    path('approve/<int:id>/',
         approve, name='approve'),
    path('unapprove/<int:id>/',
         unapprove, name='unapprove'),


]
