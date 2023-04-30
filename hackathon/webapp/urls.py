from django.urls import path
from .views import home, admin_register, admin, book, pre_book, book_details, stand_women, stand, w_pre_book, women_book, women
urlpatterns = [
path('', home.as_view(), name='home'),
path('admin_register/', admin_register.as_view(), name='admin_register'),
path('admin/', admin.as_view(), name='admin'),
path('book/', book.as_view(), name='book'),
#path('login/', login.as_view(), name='login'),
path('pre_book/', pre_book.as_view(), name='pre_book'),
#path('register/', register.as_view(), name='register'),
path('stand_women/', stand_women.as_view(), name='stand_women'),
path('stand/', stand.as_view(), name='stand'),
path('w_pre_book/', w_pre_book.as_view(), name='w_pre_book'),
path('women_book/', women_book.as_view(), name='women_book'),
path('women/', women.as_view(), name='women'),
path('book_details/', book_details.as_view(), name="book_details"),
]
