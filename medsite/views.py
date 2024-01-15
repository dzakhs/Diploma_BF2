from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from medsite.forms import MRIOrderForm, CTOrderForm, PETCTOrderForm, USOrderForm
from medsite.models.CT import CTStudy, CTOrder
from medsite.models.MRI import MRIStudy, MRIOrder
from medsite.models.PET_CT import PETCTStudy, PETCTOrder
from medsite.models.UltraSound import USStudy, USOrder
from medsite.models.contacts import Contacts


class IndexListView(generic.ListView):
    model = CTStudy
    template_name = 'medsite/index.html'


class MRIStudyListView(generic.ListView):
    model = MRIStudy
    template_name = 'medsite/mri.html'


class CTStudyListView(generic.ListView):
    model = CTStudy
    template_name = 'medsite/ct.html'


class USStudyListView(generic.ListView):
    model = USStudy
    template_name = 'medsite/us.html'


class PETCTStudyListView(generic.ListView):
    model = PETCTStudy
    template_name = 'medsite/petct.html'


class MRIOrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = MRIOrder
    form_class = MRIOrderForm
    success_url = reverse_lazy('medsite:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class MRIOrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = MRIOrder


class MRIOrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = MRIOrder
    form_class = MRIOrderForm
    success_url = reverse_lazy('medsite:index')


class MRIOrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = MRIOrder
    success_url = reverse_lazy('medsite:index')


class CTOrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = CTOrder
    form_class = CTOrderForm
    success_url = reverse_lazy('medsite:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class CTOrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = CTOrder


class CTOrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CTOrder
    form_class = CTOrderForm
    success_url = reverse_lazy('medsite:index')


class CTOrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CTOrder
    success_url = reverse_lazy('medsite:index')


class PETCTOrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = PETCTOrder
    form_class = PETCTOrderForm
    success_url = reverse_lazy('medsite:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class PETCTOrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = PETCTOrder


class PETCTOrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = PETCTOrder
    form_class = PETCTOrderForm
    success_url = reverse_lazy('medsite:index')


class PETCTOrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = PETCTOrder
    success_url = reverse_lazy('medsite:index')


class USOrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = USOrder
    form_class = USOrderForm
    success_url = reverse_lazy('medsite:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class USOrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = USOrder


class USOrderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = USOrder
    form_class = USOrderForm
    success_url = reverse_lazy('medsite:index')


class USOrderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = USOrder
    success_url = reverse_lazy('medsite:index')


class UserOrdersView(generic.View):
    login_url = 'users:login'

    def get(self, request):
        mri_orders = MRIOrder.objects.filter(user=self.request.user)
        ct_orders = CTOrder.objects.filter(user=self.request.user)
        petct_orders = PETCTOrder.objects.filter(user=self.request.user)
        us_orders = USOrder.objects.filter(user=self.request.user)

        context = {
            'mri': mri_orders,
            'ct': ct_orders,
            'petct': petct_orders,
            'us': us_orders
        }

        return render(request, 'medsite/user_orders.html', context)


class ContactsListView(generic.ListView):
    model = Contacts
    template_name = 'medsite/contacts.html'