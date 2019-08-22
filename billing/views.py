from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import BillHeaderForm, BillLineFormSet
from .models import BillHeader, BillLines
from django.views.generic.edit import CreateView, UpdateView
from django.utils import timezone
from django.views.generic.list import ListView


@login_required
def invoicelistview(request):
    user_id = request.user.id
    invoices = BillHeader.objects.filter(user_id = user_id)
    context = {'title': 'Invoice List View', 'invoices': invoices}
    return render(request, 'billing/invoicelistview.html', context=context)


@login_required
def createinvoice(request, user_id):
    if request.method == "POST":
        form = BillHeaderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            messages.succcess(request, "Created new invoice")
            return redirect('createinvoice', user_id=user_id)
    context = {'title': 'Create New Invoice', 'form': BillHeaderForm}
    return render(request, 'billing/createinvoice.html', context=context)




@method_decorator(login_required, name='dispatch')
class BillHeaderCreate(CreateView):
    model = BillHeader
    template_name = 'billing/createinvoice.html'
    fields = ['company_name', 'street_address', 'city', 'state', 'phone', 'email']
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



@method_decorator(login_required, name='dispatch')
class UpdateBillHeader(UpdateView):
    model = BillHeader
    template_name = 'billing/createinvoice.html'
    fields = ['company_name', 'street_address', 'city', 'state', 'phone', 'email']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name = 'dispatch')
class BillListView(ListView):

    model = BillHeader
    paginate_by = 5  # if pagination is desired
    template_name = 'billing/billinghome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['title'] = 'Billing List View Home'
        print(context)
        return context


    def get_queryset(self):
        queryset = BillHeader.objects.filter(user = self.request.user)
        return queryset


@login_required
def editinvoice(request, invoice_id):
    headerinstance = BillHeader.objects.get(id = invoice_id)
    if request.method == "POST":
        headerform = BillHeaderForm(request.POST)
        lineformset = BillLineFormSet(request.POST, instance = headerinstance)

        if headerform.is_valid():
            headerform.save()

        if lineformset.is_valid():
            lineformset.save()

        if headerform.is_valid() or lineformset.is_valid():
            return redirect('editinvoice', invoice_id=invoice_id)

    headerform = BillHeaderForm(instance = headerinstance)
    lineformset = BillLineFormSet(instance = headerinstance)
    context = {'title':'Edit Invoice', 'headerform': headerform, 'lineform': lineformset}
    return render(request, 'billing/editinvoice.html', context=context)