from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import InvoiceForm, InvoiceItemFormSet

# Create your views here.
class InvoiceView(LoginRequiredMixin, FormView):
    login_url = "/accounts/login/"
    template_name = "invoices/create_invoice.html"
    form_class = InvoiceForm
    success_url = "/create/"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        data = super().get_context_data(**kwargs)
        print(data)
        if self.request.POST:
            data['item_formset'] = InvoiceItemFormSet(self.request.POST)
        else:
            data['item_formset'] = InvoiceItemFormSet()
            
        return data
    
    def form_valid(self, form: Any) -> HttpResponse:
        
        context_data = self.get_context_data()
        item_formset = context_data['item_formset']
       #print(item_formset.cleaned_data)
        
        form.instance.created_by = self.request.user
        added_invoice_object = form.save()
        
        if item_formset.is_valid():
            item_formset.instance = added_invoice_object
            item_formset.save()
            
        return super().form_valid(form)