from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from medsite.forms import MRIOrderForm, CTOrderForm, PETCTOrderForm, USOrderForm
from medsite.models.CT import CTStudy, CTOrder
from medsite.models.MRI import MRIStudy, MRIOrder
from medsite.models.PET_CT import PETCTStudy, PETCTOrder
from medsite.models.UltraSound import USStudy, USOrder


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


class CTOrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = CTOrder
    form_class = CTOrderForm
    success_url = reverse_lazy('medsite:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class PETCTOrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = PETCTOrder
    form_class = PETCTOrderForm
    success_url = reverse_lazy('medsite:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class USOrderCreateView(LoginRequiredMixin, generic.CreateView):
    model = USOrder
    form_class = USOrderForm
    success_url = reverse_lazy('medsite:index')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)
