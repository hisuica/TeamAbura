from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import posts

def index(request):
    test_message = 'Test message'
    context = {'test_message': test_message}
    return render(request, 'write/write.html', context)

def posting(request, id):
    post = get_object_or_404(posts, pk=id)
    return render(request, 'write/posting.html', {'post': post})

def save(request, id):
    post = get_object_or_404(posts, pk=id)
    try:
        post.post_author = request.POST['author']
        post.category_ID2 = request.POST['categoryid2']
        post.post_password = request.POST['password']
        post.post_title = request.POST['title']
        post.post_content = request.POST['content']
    except (KeyError, Posts.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'write/posting.html', {
            'post': post,
            'error_message': "포스트가 존재하지 않음",
        })
    else:
        post.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('write:posting', args=(post.ID,)))