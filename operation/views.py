from django.shortcuts import render
from django.views.generic import View
from operation.forms import ElecBillForm

class ElectricityView(View):
    def get(self,request,*args,**kwargs):
        form_obj=ElecBillForm()

        return render(request,"electricity.html",{"form":form_obj})
    def post(self,request,*args,**kwargs):
        form_obj=ElecBillForm(request.POST)
        if form_obj.is_valid():
            consumerno=form_obj.cleaned_data.get("consumer_number")
            current_reading=form_obj.cleaned_data.get("current_month_reading")
            previous_reading=form_obj.cleaned_data.get("previous_month_reading")
            rate=form_obj.cleaned_data.get("unit_rate")
            
            phase=form_obj.cleaned_data.get("phase")

            unit_consumed_in_kwh=current_reading-previous_reading
            energy_charge=unit_consumed_in_kwh*int(rate)
            fixed_rate=40
            load=1
            fixed_charge=load*fixed_rate
            tax_rate=20
            electricity_duty=((energy_charge+fixed_charge)*tax_rate)/100
            total=energy_charge+fixed_charge+electricity_duty

            data={
                "number":consumerno,
                "load":load,
                "phase":phase,
                "reading":current_reading,
                "prev_reading":previous_reading,
                "rate":fixed_rate,
                "tax":tax_rate,
                "total":abs(total),
                "form":form_obj

            }
            return render(request,"electricity.html",data)
        else:
            return render(request,"electricity.html",{"form":form_obj})

class IndexView(View):
    def get(self,request,*args,**kwargs):

        return render(request,"index.html")

