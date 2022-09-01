from django.shortcuts import render
from django_tables2 import RequestConfig
from web.table import Table
from web.query import get_query


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
    queryset = [get_query()]
    table = Table(queryset)
    RequestConfig(request).configure(table)
    context["table"] = table
    return render(request, "web/index.html", context)
