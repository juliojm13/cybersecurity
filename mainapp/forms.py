import hashlib
import random
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, HTML, Submit
from django import forms
from mainapp.models import Organisation


class AddOrganizationForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = ('org_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['org_name'].label = "Nombre:"
        # self.template = "../static/js/highslide.js"
        self.helper.layout = Layout(
            Div(
                Field('org_name'),
                css_class='field'
            ),
            Div(
                Submit('submit', css_class='grey_col', value="Agregar"),
                css_class='field margin_top_50'),
        )
