from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import book, Pre_Book

class home(TemplateView):
    template_name = 'home.html'

class admin_register(TemplateView):
    template_name = 'admin_register.html'

class admin(TemplateView):
    template_name = 'admin.html'

class book(TemplateView):
    model = book
    template_name = 'book.html'
    
class book_details(ListView):
    model = book
    template_name = 'book_details.html'
    context_object_name = 'all_posts_list'

class login(TemplateView):
    template_name = 'login.html'

class pre_book(ListView):
    model = Pre_Book
    template_name = 'pre_book.html'

"""class register(TemplateView):
    template_name = 'register.html'"""

class stand_women(TemplateView):
    template_name = 'stand_women.html'

class stand(TemplateView):
    template_name = 'stand.html'
class w_pre_book(TemplateView):
    template_name = 'w_pre_book.html'

class women_book(TemplateView):
    template_name = 'women_book.html'

class women(TemplateView):
    template_name = 'women.html'