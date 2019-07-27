from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Name',
                'class':'form-control'
            }
        )

    )
    location=forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Location',
                'class':'form-control'
            }
        )
    )
    salary=forms.IntegerField(
        label="Enter Your Salary",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Your Salary',
                'class':'form-contol'
            }
        )
    )
    email=forms.EmailField(
        label="Enter Your Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Your Email',
                'class':'form-control'
            }
        )
    )

