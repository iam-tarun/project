from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Itemlist
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserFilter
from groups.models import GroupUserTable
from notification.models import Notification
from notification.models import SharedItemsList

@login_required
def dashboard(request):
    user = request.user
    items = Itemlist.objects.all()
    groups = user.groupusertable_set.filter(status=1)
    items_s = SharedItemsList.objects.filter(shared_user=request.user.username)
    items_b = SharedItemsList.objects.filter(borrowed_user=request.user.username)

    context = {'items_s': items_s,
               'items_b': items_b,
               'form': user.itemlist_set.all(),
               'groups':groups,
               'count': Notification.objects.filter(user=request.user, viewed=False, type="Personal")|
                          Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL")|
                          Notification.objects.filter(user=request.user, viewed=False, type="Item")|
                          Notification.objects.filter(user=request.user, viewed=False, type="Group"),

               'count_a': Notification.objects.filter(user=request.user, viewed=False, type="PERSONAL"),
               'count_i': Notification.objects.filter(user=request.user, viewed=False, type="Item"),
               'count_g': Notification.objects.filter(user=request.user, viewed=False, type="Group"),
               'count_f': Notification.objects.filter(user=request.user, viewed=False, type="Friend"),
               }
    return render(request, 'userapp/dashboard.html', context)


class UserItemlist(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Itemlist
    template_name = 'userapp/user_itemlist.html'
    context_object_name = 'items'

    def test_func(self):
        return self.request.user.is_authenticated

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Itemlist.objects.filter(name=user).order_by('-date_created')


class Itemlistview(ListView):
    model = Itemlist
    template_name = 'userapp/dashboard.html'
    context_object_name = 'Items'


class Itemlistdetailview(DetailView):
    model = Itemlist
    template_name = 'userapp/Itemlist_detail.html'


class ItemlistCreateview(LoginRequiredMixin, CreateView):
    model = Itemlist
    fields = ['item', 'condition', 'Category', 'ItemStatus', 'Image']

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)


class ItemlistUpdateview(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Itemlist
    fields = ['item', 'condition', 'Category', 'ItemStatus', 'Image']

    def form_valid(self, form):
        form.instance.name = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.name:
            return True
        return False


class Itemlistdeleteview(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Itemlist
    success_url = '/dashboard'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.name:
            return True
        return False
