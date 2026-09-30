from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class ShopProductGridView(TemplateView):
    template_name = 'shop/product/grid.html'


class ShopProductListView(TemplateView):
    template_name = 'shop/product/list.html'
