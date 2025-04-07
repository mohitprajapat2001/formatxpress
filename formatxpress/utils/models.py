from django_extensions.db.models import TimeStampedModel
from django.db.models import ForeignKey, SET_NULL


class UserFieldAbstractModel(TimeStampedModel):
    user = ForeignKey("accounts.User", on_delete=SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True
