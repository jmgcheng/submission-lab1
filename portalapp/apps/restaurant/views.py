from django.shortcuts import render
from .models import Restaurant
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class RestaurantListView(ListView):
    model = Restaurant

    template_name = 'restaurant/list.html'
    context_object_name = 'restaurants'


class RestaurantDetailView(DeleteView):
    model = Restaurant

    template_name = 'restaurant/detail.html'


class RestaurantCreateView(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = ['name', 'description']
    template_name = 'restaurant/form.html'


class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    fields = ['name', 'description']
    template_name = 'restaurant/form.html'


class RestaurantDeleteView(LoginRequiredMixin, DeleteView):
    model = Restaurant
    template_name = 'restaurant/confirm_delete.html'
    success_url = '/restaurants'
