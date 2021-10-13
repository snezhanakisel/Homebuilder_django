from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.
from django.views.generic.edit import CreateView



class ShowPostView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwards):
        ctx = super(ShowPostView, self).get_context_data(**kwards)
        ctx['title'] = 'Главная страница блога'
        return ctx


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwards):
        ctx = super(PostDetailView, self).get_context_data(**kwards)
        ctx['title'] = Post.objects.get(pk=self.kwargs['pk'])
        return ctx


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'

    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(CreatePostView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/create_post.html'

    fields = ['title', 'text']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwards):
        ctx = super(UpdatePostView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx


class DeletePostView(DeleteView, UserPassesTestMixin, LoginRequiredMixin):
    model = Post
    success_url = '/'
    template_name = 'blog/delete_post.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserAllPostView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'post'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username') )
        return Post.objects.filter(author=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserAllPostView, self).get_context_data(**kwards)
        ctx['title'] = f"Статьи от пользователя {self.kwargs.get( 'username' )}"
        return ctx


class PostCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login.
    """
    model = Comment
    template_name = 'blog/post_commentform.html'
    fields = ['message', ]
    context_object_name = "comment"

    def get_context_data(self, **kwargs):
        """
        Add associated blog to form template so can display its title in HTML.
        """
        # Call the base implementation first to get a context
        kwargs['comment'] = self.object.blogcomment_set.all()
        context = super(PostCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Add author and associated blog to form data before setting it as valid (so it is saved to model)
        """
        # Add logged-in user as author of comment
        form.instance.author = self.request.user
        # Associate comment with blog based on passed id
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        # Call super-class form validation behaviour
        return super(PostCommentCreate, self).form_valid(form)

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        return reverse('blog_post', kwargs={'pk': self.kwargs['pk'], })