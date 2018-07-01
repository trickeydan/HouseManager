from django.db.models import Model as DModel
from django.db.models import UUIDField, DateTimeField
import uuid


class Model(DModel):

    class Meta:
        abstract = True

    id = UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)