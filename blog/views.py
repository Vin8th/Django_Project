from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,CreateView, UpdateView , DeleteView #classbased views	
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin	
from django.contrib.auth.models import User					 
from django.http import HttpResponse
from .models import Post #function based views

# Create your views here.

# posts = [
# 	{
# 		'author':'Vineeth B',
# 		'title':'Blog Post 1',
# 		'content':'Content post 1',
# 		'date_posted':'April'
# 	},
# 	{
# 		'author':'Corey MS',
# 		'title':'Blog Post 2',
# 		'content':'Content post 2',
# 		'date_posted':'May'
# 	}
# ]

def home(request):
	context = {
		'posts' : Post.objects.all()
		# 'title':'Vineeth'
	}

	return render(request,'blog/home.html',context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] # the - sign changes to latest to oldest
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_post.html'
	context_object_name = 'posts'
	paginate_by = 5

	def get_queryset(self):	#This used to overide to get only one particular user
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
	model = Post
	fields = ['title','content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):		#only authour of the post can update his post not others
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post

	def test_func(self):		#only authour of the post can update his post not others
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

	success_url = '/'

def about(request):
	# return HttpResponse('<h1>Blog About</h1>')
	return render(request,'blog/about.html',{'title':'about'})

	
