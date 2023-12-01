from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:  # algumas coisas já confguradas. checar documentação.
        # verbose_name = 'Categoria'
        verbose_name_plural = "Categories"

    def __str__(self) -> str:  # type: ignore
        return f"{self.name}"


# Create your models here.
class Contact(models.Model):
    # basicamente oq vai pro bd
    # id(primary key) = gerado automaticamente pelo django
    first_name = models.CharField(
        max_length=50,
    )
    last_name = models.CharField(max_length=50, blank=True)
    fone = models.CharField(
        max_length=50
    )
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m/")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)
    # on_delete = define o que vai acontecer se aforeign key for deletado
    # cascade = vai deletar o contato junto
    # SET_NULL = seta o campo para nulo

    def __str__(self) -> str:
        return (
            # como o nome será mostrado no admin
            f"{self.first_name} {self.last_name}"
        )
