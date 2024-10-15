from django.shortcuts import render

# Create your views here.

data_productos = [
    {"id": 1, "nombre": "Producto 1", "imagen": "https://picsum.photos/id/684/600/400"},
    {"id": 2, "nombre": "Producto 2", "imagen": "https://picsum.photos/id/685/600/400"},
    {"id": 3, "nombre": "Producto 3", "imagen": "https://picsum.photos/id/686/600/400"},
    {"id": 4, "nombre": "Producto 4", "imagen": "https://picsum.photos/id/687/600/400"}, 
]

def productos(request):
    contexto = {
        "titulo": "Nuestros productos",
        "productos": data_productos
    }
    return render(request, 'productos/productos.html', contexto)