class ModelMixin:
    def to_dict(self):
        attrs = {}
        for field in self._meta.get_fields():
            attrs[field.attname] = getattr(self, field.attname, None)
        return attrs
