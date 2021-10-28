from django.db import models


class PublishStateOptions(models.TextChoices):
    # CONSTAN = DB_VALUE, USER_DISPLAY_VA
    PUBLISH = 'PB', 'Publicado'
    DRAFT = 'BR', 'Borrador'
    # UNLISTED = 'UN', 'No incluido'
    # PRIVATE =  'PR', 'Privado'