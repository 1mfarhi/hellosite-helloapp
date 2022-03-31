from django.urls import path
from helloapp.views import HelloWorldView, HelloView, Goodbye
# from hellosite.helloapp.views import Goodbye


urlpatterns = [
    # helloapp/
    path('', HelloWorldView.as_view(), name='hello_world'),
    path('<name>', HelloView.as_view(), name='hello_name'),
    path('', Goodbye.as_view(), name='goodbye_world'),
    path('<name>', Goodbye.as_view(), name='goodbye_name'),
]