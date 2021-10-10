from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
from .forms import CommentForm


class ShowPostView(ListView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
    ordering = ['-date']
    paginate_by = 1

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


# def commentadd(request):
#
#     if request.method == 'POST':
#         back = CommentForm(request.POST)
#         if back.is_valid():
#             back.save()
#     back = CommentForm
#     data = {
#             'back': back,
#         }
#
#     return render(request, 'blog/post_detail.html', data)


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


class UpdatePostView( LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/create_post.html'

    fields = ['title', 'text']

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePostView( DeleteView, UserPassesTestMixin, LoginRequiredMixin ):
    model = Post
    success_url = '/'
    template_name = 'blog/delete_post.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserAllPostView( ListView ):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'post'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404( User, username=self.kwargs.get( 'username' ) )
        return Post.objects.filter( author=user ).order_by( '-date' )

    def get_context_data(self, **kwards):
        ctx = super( UserAllPostView, self ).get_context_data( **kwards )
        ctx['title'] = f"Статьи от пользователя {self.kwargs.get( 'username' )}"
        return ctx
