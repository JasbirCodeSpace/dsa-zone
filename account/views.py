from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views.generic import CreateView
from account.forms import StudentSignUpForm, CuratorSignUpForm
from account.models import User


class StudentCreateView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'account/registration/student.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'student'
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student_signup')

class CuratorCreateView(CreateView):
    model = User
    form_class = CuratorSignUpForm
    template_name = 'account/registration/curator.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_type'] = 'curator'
        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('curator_signup')
    

