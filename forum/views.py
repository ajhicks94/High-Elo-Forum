from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils import timezone

from .models import Category, Forum, Thread, Post
from .forms import NameForm

#need to show the categories and their subforums
class CategoryView(generic.ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category_list'

    def get_queryset(self):
        return Forum.objects.all().order_by('position')

#We've clicked on a forum and need to see its sub-forums if it has any,
#and its threads if it does not.
class ForumView(generic.ListView):
    template_name = 'forum.html'
    context_object_name = 'forum_list'


class TopicIndexView(generic.ListView):
    template_name = 'topic_index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.filter(modified_on__lte=timezone.now()).order_by('-modified_on')

class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail.html'

#    def get_context_data(self, **kwargs):
#        context = super(DetailView, self).get_context_data(**kwargs)
#
#        return context

#test function for forms
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

# Create your views here.
