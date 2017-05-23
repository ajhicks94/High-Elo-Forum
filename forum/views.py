from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import Category, Forum, Thread, Post
from .forms import ThreadForm, CreateUserForm

#TODO: CLEAN UP OVER-IMPORTED LIBRARIES/ITEMS 

#need to show the categories and their subforums
class CategoryIndex(generic.ListView):
    model = Forum
    template_name = 'category.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Category.objects.prefetch_related("forums").all()

#We've clicked on a forum and need to see its sub-forums if it has any,
#and its threads if it does not.
class ThreadList(generic.ListView):
    template_name = 'forum.html'
    context_object_name = 'thread_list'

    def get_context_data(self, **kwargs):
        context = super(ThreadList, self).get_context_data(**kwargs)
        forum = get_object_or_404(Forum, id=self.kwargs['pk'])
        context['forum'] = forum
        return context

    def get_queryset(self):
        return Thread.objects.filter(forum=self.kwargs['pk'])

class PostList(generic.ListView):
    template_name = 'thread.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        thread = get_object_or_404(Thread, id=self.kwargs['pk'])
        context['thread'] = thread
        return context

    def get_queryset(self):
        return Post.objects.filter(thread=self.kwargs['pk'])

class CreateUser(generic.FormView):
    form_class = CreateUserForm
    template_name = 'create_user.html'
    
    success_url = reverse_lazy('forum:category')

    def form_valid(self, form):
        data = form.cleaned_data
        new_user = User.objects.create_user(username=data['username'], password=data['password'], email=data['email'])
        return super(CreateUser, self).form_valid(form)

class AddThread(generic.FormView):
    form_class = ThreadForm
    success_url = '/forum/'
    template_name = 'add_thread.html'

    #Filter options and set default for the field
    def get_form(self):
        form = super(AddThread, self).get_form()
        form.fields['forum'].queryset = Forum.objects.filter(pk=self.kwargs['pk'])
        form.initial['forum'] = get_object_or_404(Forum, pk=self.kwargs['pk'])
        return form

    #Creates a new thread with appropriate attributes
    def form_valid(self, form):
        data = form.cleaned_data
        if not self.request.user.is_authenticated():
            #TODO: Show user that they must be logged in first
            return super(AddThread, self).form_valid(form)

        new_thread = Thread(title=data['title'], body=data['body'], forum=data['forum'], 
                            author=get_object_or_404(User, id=self.request.user.id))
        new_thread.save()
        self.success_url = '/forum/thread/' + str(new_thread.id) + '-' + new_thread.slug
        return super(AddThread, self).form_valid(form)
