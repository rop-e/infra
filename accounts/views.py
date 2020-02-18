from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('página inicial de contas de usuários')

def index_t(request):
    return render(request, 'index.html')