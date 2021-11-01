from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


from .decorators import group_required
from pages.models import Books
@group_required('viewergrp')
def BooksView(request):
    # if request.user.groups.filter(name="viewergrp").exists():
        books = Books.objects.all()
        return render(request, "books.html", {"books":books})

    # else:
    #     return HttpResponse("Only for Viewer group specific members")
