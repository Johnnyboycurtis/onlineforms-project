from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BillHeaderForm, BillLineFormSet
from .models import BillHeader, BillLines


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