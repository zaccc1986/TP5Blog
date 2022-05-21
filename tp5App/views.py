from django.shortcuts import render

def post_list(request):
    return render(request, 'tp5App/post_list.html', {})