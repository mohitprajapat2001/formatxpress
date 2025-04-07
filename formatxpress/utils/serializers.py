from rest_framework.serializers import ModelSerializer


class DynamicModelSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(DynamicModelSerializer, self).__init__(*args, **kwargs)
        fields = kwargs.pop("fields", None)
        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
