from typing import Any
from django import forms
from contact.models import Contact
from django.forms import ValidationError


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeHolder": "Escreva seu nome",
            }
        ),
        label="Primeiro Nome",
        help_text="PO, é só botar o nome",
    )

    # novo_campo = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={'class': 'campoCriadoNoModel'}
    #     ),
    #     label='Campo que não existe no model',
    #     help_text="Campo que só existe no form de contact"
    # )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "fone",
            "email",
            "description",
            "category",
            'picture'
        )

    def clean(self) -> dict[str, Any]:
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        msgEqualsNames = ValidationError(
            "First name can not be equals to last name", code="invalid"
        )
        if first_name == last_name:
            self.add_error("first_name", msgEqualsNames)
            self.add_error("last_name", msgEqualsNames)
        return super().clean()

    def clean_first_name(self):  # existe um método para todos os campos
        # só port clean_(nome do campo)
        first_name = self.cleaned_data.get("first_name")
        if first_name == "ABC":
            self.add_error('first_name', ValidationError(
                "Proibido digitar ABC", code="invalid"))

            # raise e self.add_error retorna a mesma coisa
            # e tem o mesmo proposito
        return first_name
