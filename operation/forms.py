from django import forms

class ElecBillForm(forms.Form):
    consumer_number=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    current_month_reading=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    previous_month_reading=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))
    unit_rate_choice=(
        (1,"Rs.6.50"),
        (2,"Rs.7.60"),
        (3,"Rs.8.70"),
       

    )
    unit_rate=forms.ChoiceField(choices=unit_rate_choice,widget=forms.Select(attrs={"class":"form-control form-select mb-3"}))
    # sanction_load=forms.CharField(widget=forms.TextInput(attrs={"value":"1KWh"}))
    phase=forms.CharField(widget=forms.TextInput(attrs={"value":"single","class":"form-control mb-3"}))