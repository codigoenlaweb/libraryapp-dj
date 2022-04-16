from django import forms

class CateoryForm(forms.Form):
    name = forms.CharField(label='Category name', max_length=28)
    
    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) <= 3:
            raise ValidationError("the category name is too short")

        return data