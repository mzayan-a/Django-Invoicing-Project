from django.forms import ModelForm, inlineformset_factory

from .models import Invoice, InvoiceItem

class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = ['date','customer']
        
class InvoiceItemForm(ModelForm):
    class Meta:
        model = InvoiceItem
        fields = ['product', 'quantity', 'price']
        
InvoiceItemFormSet = inlineformset_factory(Invoice, InvoiceItem, form=InvoiceItemForm, extra=1)