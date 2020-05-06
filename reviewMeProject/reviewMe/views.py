from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView

class NameView(CreateView):
    def get(self, request):
        q = request.GET.get("q", "")
        return render(request, 'username.html', {'q': q})


class reviewView(View):
    def get(self, request):
        q = request.GET.get("q", "")
        return render(request, 'review.html', {'q' : q })
    



