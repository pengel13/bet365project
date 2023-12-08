# flake8: noqa
from typing import Any
from django import forms
from contact.models import Contact
from django.forms import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(attrs={"accept": "image/*"})
    )  # flake8: noqa

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
            "picture",
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
            self.add_error(
                "first_name", ValidationError("Proibido digitar ABC", code="invalid")
            )

            # raise e self.add_error retorna a mesma coisa
            # e tem o mesmo proposito
        return first_name


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
        error_messages={
            "required": "Esse campo é necessário",
            "min_length": "A quantidade mínima de caracteres requirida é 3",
        },
    )
    last_name = forms.CharField(required=True, min_length=3)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            msgError = "This email is already logged into our database"
            self.add_error("email", ValidationError(msgError, "invalid"))

        return email


class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text="Primeiro nome",
        error_messages={"min_length": "Please enter at least 2 characters"},
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text="Sobrenome ",
        error_messages={"max_length": "Please do not enter more than 30 characters"},
    )

    password1 = forms.CharField(
        label='Password 1',
        strip=False,
        widget=forms.PasswordInput(attrs={'auto-complete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )
    # password2 = forms.CharField(
    #     label='Password 2',
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'auto-complete': 'new-password'}),
    #     help_text='Use the same password as in the first one',
    #     required=False,
    # )
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            'password1',
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        cur_email = self.instance.email
        if cur_email != email:
            if User.objects.filter(email=email).exists():
                msgError = "This email is already logged into our database"
                print('oi')
                self.add_error("email", ValidationError(msgError, "invalid"))


        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as e:
                self.add_error("password1", ValidationError(e))

        return password1
