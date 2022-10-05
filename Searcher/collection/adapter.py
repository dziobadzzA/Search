from django.apps import apps

class Model():
    model = apps.get_model('collection.model')
