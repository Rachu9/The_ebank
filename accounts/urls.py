# # # from django.urls import path
# # # from . import views

# # # urlpatterns = [
# # #     path('', views.home, name='home'),
# # #     path('dashboard/', views.dashboard, name='dashboard'),
# # #     path('transfer/', views.transfer_funds, name='transfer_funds'),
# # #     path('pay-bill/', views.pay_bill, name='pay_bill'),
# # #     path('logout/', views.logout, name='logout'),
    
# # # ]

# # from django.contrib import admin
# # from django.urls import path
# # from django.contrib.auth.views import LoginView, LogoutView
# # from django.contrib.auth import views as auth_views

# # from . import views  # Import your views

# # urlpatterns = [
# #     path('admin/', admin.site.urls),
# #     path('', views.home, name='home'),  # Assuming you have a home view
# #     path('dashboard/', views.dashboard, name='dashboard'),
# #     path('transfer/', views.transfer_funds, name='transfer_funds'),
# #     path('pay-bill/', views.pay_bill, name='pay_bill'),
# #     # path('logout/', LogoutView.as_view(), name='logout'),  # Log out view
# #     # path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login view
# #     path('login/', auth_views.LoginView.as_view(), name='login'),
# #     path('signup/', views.signup, name='signup'),
# # ]

# from django.contrib import admin
# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views  # Import your views
# from .views import transaction_history,user_list

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),  # Home page
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('transfer/', views.transfer_funds, name='transfer_funds'),
#     path('pay-bill/', views.pay_bill, name='pay_bill'),
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('signup/', views.signup, name='signup'),
#     path('transaction_history/', transaction_history, name='transaction_history'), 
#     path('users/', user_list, name='user_list'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Log out view
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transfer-funds/', views.transfer_funds, name='transfer_funds'),
    path('pay-bill/', views.pay_bill, name='pay_bill'),
    path('transaction-history/', views.transaction_history, name='transaction_history'),
    path('bill_payment_history/', views.bill_payment_history, name='bill_payment_history'),
    path('user-list/', views.user_list, name='user_list'),
    path('logout/', views.logout, name='logout'),
]
