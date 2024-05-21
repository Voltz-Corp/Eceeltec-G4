from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')
class ForbiddenView(View):
    def get(self, request):
        return render(request, 'forbidden-page.html')
    def post(self, request):
        print("role")