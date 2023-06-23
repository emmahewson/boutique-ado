from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """

        # This code over-rides the default form settings
        # This allows you to customise the form in the backend
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()

        # Creates a list of tuples of the id & friendly name
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]
        print(friendly_name)

        # sets the name in the category select as the friendly name
        self.fields['category'].choices = friendly_names

        # Adds classes to fields to match styling of site
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
