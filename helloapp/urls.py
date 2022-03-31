from django.urls import path
from helloapp.views import HelloWorldView, HelloView


urlpatterns = [
    # helloapp/
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('<name>', HelloView.as_view(), name='hello_name'),
    path('', HelloWorldView.as_view(), name='goodbye_world'),
    path('<name>', HelloView.as_view(), name='goodbye_name'),
]