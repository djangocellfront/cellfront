from django.shortcuts import render


def handler404(request, *args, **argv):
    context = {}
    response = render(request, "web/404.html", context)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    context = {}
    response = render(request, "web/500.html", context)
    response.status_code = 500
    return response


def index(request):
    context = {}
    return render(request, "web/index.html", context)
