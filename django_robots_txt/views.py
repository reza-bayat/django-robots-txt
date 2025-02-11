from django.http import HttpResponse

from .utils import generate_robots_content

def robots_txt(request):
    content = generate_robots_content()
    return HttpResponse(content, content_type='text/plain')