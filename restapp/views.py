from django.http import JsonResponse

# Create your views here.

def index(request):
    context = {
        "post": "posts"
    }
    return JsonResponse(context)