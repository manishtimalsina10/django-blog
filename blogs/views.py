from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Blog, Category


def posts_by_category(request, category_id):

  #Fetch the posts that belongs to the category with the id category_id
  posts = Blog.objects.filter(status='Published', category=category_id)
  # Use try/except when we want to do some custom action if the category doesnot exist
  try:
    category = Category.objects.get(pk=category_id)
  except:
    #Redirect user to home page
    return redirect('home')
  
  #Use get_object_or_404 when we want to show 404 error page if the category doesnot exist
  #category = get_object_or_404(Category, pk=category_id)

  context = {
    'posts' : posts,
    'category': category,
  }
  return render(request, 'posts_by_category.html',context)
