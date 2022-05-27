from django.shortcuts import render
from .models import tweet
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.



def profile(request):
    return render(request,'accounts/profile.html')
class TweetListView(LoginRequiredMixin,ListView):
    model=tweet
    template_name='home.html'
    ordering=['-datetime']

class TweetCreateView(LoginRequiredMixin,CreateView):
    model=tweet
    template_name='create.html'
    fields='__all__'
    success_url='/'

    def form_valid(self,form):
        form.instance.uname=self.request.user
        return super().form_valid(form)

class TweetUpdateView(UserPassesTestMixin,UpdateView,LoginRequiredMixin):
    model=tweet
    template_name='update.html'
    fields=['text']
    success_url='/'

    def form_valid(self,form):
        form.instance.uname=self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet=self.get_object()
        if(self.request.user==tweet.uname):
            return True
        return False

class TweetDeleteView(UserPassesTestMixin,DeleteView,LoginRequiredMixin):
    model=tweet
    template_name='delete.html'
    success_url='/'

    def form_valid(self,form):
        form.instance.uname=self.request.user
        return super().form_valid(form)

    def test_func(self):
        tweet=self.get_object()
        if(self.request.user==tweet.uname):
            return True
        return False
