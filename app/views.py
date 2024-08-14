from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    # queryset retrieves all the menu items from the model
    queryset = MenuItem.objects.all()
    # serializer_class to display and storage the data
    serializer_class = MenuItemSerializer

# single menu item view to retrieve, update, and delete a single menu item
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer