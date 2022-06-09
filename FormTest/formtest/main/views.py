from django.http import Http404
from django.shortcuts import redirect, render
from django.forms import inlineformset_factory
from django.views import View

from .models import Product, Delivery
from .forms import *


class SupportCreateDelivery(View):
    template_name = 'main/main.html'

    def get_object(self, name_pk):
        try:
            obj = Product.objects.get(prod_name=name_pk)
        except Product.DoesNotExist:
            raise Http404('Product not found!')
        return obj.id

    def get_context_data(self, **kwargs):
        if 'create_form' not in kwargs:
            kwargs['create_form'] = SupportAddDeliveryForm()
        if 'choose_form' not in kwargs:
            kwargs['choose_form'] = SupportChooseDeliveryForm()

        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        ctxt = {}

        if 'create' in request.POST:
            create_form = SupportAddDeliveryForm(request.POST, request.FILES)

            if create_form.is_valid():
                print(create_form.data)
                create_form.save()
                pk = self.get_object(create_form.data.get('prod_name'))
                return redirect(f"/create/{pk}")

            else:
                ctxt['create_form'] = create_form

        elif 'choose' in request.POST:
            choose_form = SupportChooseDeliveryForm(request.POST)

            if choose_form.is_valid():
                print(choose_form.data)
                return redirect(f"/create/{choose_form.data.get('delivery_name')}")
            else:
                ctxt['choose_form'] = choose_form

        return render(request, self.template_name, self.get_context_data(**ctxt))


class CreateDelivery(View):
    template_name = 'main/main2.html'

    def get_object(self):
        try:
            obj = Product.objects.get(pk=self.kwargs['pk'])
        except Product.DoesNotExist:
            raise Http404('Question not found!')
        return obj

    productformset = inlineformset_factory(Product, Delivery, fields=("delivery_date", "delivery_address"))

    def get(self, request, **kwargs):
        product = self.get_object()
        formset = self.productformset(instance=product)
        return render(request, self.template_name, {'form': formset})

    def post(self, request, **kwargs):
        product = self.get_object()
        formset = self.productformset(request.POST, instance=product)
        if formset.is_valid():
            formset.save()
            return redirect(f'/create/{kwargs.get("pk")}')

        return render(request, self.template_name, {'form': formset})
