from django.views.generic import ListView, DetailView
from django.db.models import Max
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from .models import Blog


# Create your views here.
class PostListView(ListView):
    template_name   = 'blog/list.html'

    def get_queryset(self, *args, **kwargs):
        request      = self.request
        posts        = Blog.objects.all().annotate(lr=Max('date_created'))\
                                                    .order_by('-lr')

        # Set pagination
        paginator = Paginator(posts, 2)
        page= request.GET.get('page') # get current page
        try:
            items = paginator.page(page)
        except PageNotAnInteger:
            items = paginator.page(1) # First Page
        except EmptyPage:
            items = paginator.page(paginator.num_pages) # Last page

        index = items.number - 1
        max_index = len(paginator.page_range)
        start_index = index - 5 if index >= 5 else 0
        end_index = index + 5 if index <= max_index else max_index
        page_range = paginator.page_range[start_index:end_index]

        instance = {
            'posts': posts,
            'items': items,
            'page_range': page_range,
        }
        return instance

class PostDetailView(DetailView):
    template_name   = 'blog/detail.html'

    def get_queryset(self, *args, **kwargs):
        request     = self.request
        slug        = self.kwargs.get('slug')
        queryset    = Blog.objects.filter(slug=slug)
        return queryset
