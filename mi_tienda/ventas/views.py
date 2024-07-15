from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto

def index(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/index.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'ventas/detalle_producto.html', {'producto': producto})

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = Producto.objects.filter(id__in=carrito.keys())
    total = sum(producto.precio * cantidad for producto, cantidad in zip(productos, carrito.values()))
    return render(request, 'ventas/carrito.html', {'productos': productos, 'total': total})

def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    carrito[producto_id] = carrito.get(producto_id, 0) + 1
    request.session['carrito'] = carrito
    return redirect('ver_carrito')
