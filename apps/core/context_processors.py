from .sidebar import get_sidebar_items

def sidebar_items(request):
    return {'sidebar_items': get_sidebar_items()}