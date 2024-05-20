from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
path('', views.index, name='index'),
path('home/', views.home, name='home'),
path('about/', views.about, name='about'),
    

path('addbabies/', views.AddBabies, name='addbabies'),
path('display_babies/', views.display_babies, name='display_babies'),
path('delete/<int:BabyReg_id>/',views.delete_baby, name='delete_baby'),
path('edit/<int:id>/', views.edit, name='edit'),

    #baby attendance
path('baby_attendance/', views.baby_attendance, name='baby_attendance'),
path('present_babies/', views.present_babies, name='present_babies'),



    #sitter attendance
path('sitter_attendance/', views.sitter_attendance, name='sitter_attendance'),
path('present_sitters/', views.present_sitters, name='present_sitters'),
path('addsitters/', views.addsitters, name='addsitters'),
path('allsitters/', views.allsitters, name='allsitters'),
path('delete/<int:BabyReg_id>/',views.delete_baby, name='delete_baby'),
path('edit_sitter/<int:id>/', views.edit_sitter, name='edit_sitter'),

    #login urls
path('login/', views.loginpage, name='login'),
path('register/', views.registerpage, name='register'),
path('logout/', views.logoutUser, name='logout'),

    #doll paths
path('doll/', views.doll, name='doll'),
path('add_to_stock/<int:id>', views.add_to_stock, name='add_to_stock'),
path('all_sales/', views.receipt, name='receipt'),
path('issue_item/<int:id>/', views.issue_item, name='issue_item'),
path('receipt_detail/<int:id>/', views.receipt_detail, name='receipt_detail'),
path('edit_doll/<int:id>/', views.edit_doll, name='edit_doll'),
#payment paths
path('addpayment/', views.addpayment, name='addpayment'),
path('paymentlist/', views.paymentlist, name='paymentlist'),
path('edit_payment/<int:id>/', views.edit_payment, name='edit_payment'),

path('trial/', views.trial, name='trial'),
path('baby_checkin/', views.baby_checkin, name='baby_checkin'),
path('sitter_checkin/', views.sitter_checkin, name='sitter_checkin'),
path('baby_checkout/', views.baby_checkout, name='baby_checkout'),
path('sitter_checkout/', views.sitter_checkout, name='sitter_checkout'),

]