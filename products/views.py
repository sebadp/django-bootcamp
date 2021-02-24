from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ProductForm
from .models import Product

# from django.shortcuts import get_object_or_404

# Create your views here.


def home_view(request, *args, **wkargs):
    return render(request, "home.html", {})


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id="1")
    return render(request, "products/products_detail.html", {"obj": obj})


def product_list_view(request, *args, **kwargs):
    qs = Product.objects.all()
    context = {"object_list": qs}
    return render(request, "products/list.html", context)


@staff_member_required
def product_create_view(request, *args, **kwargs):
    # UNA FORMA DE LOGRAR EL RESULTADO: LA LARGA
    # if request.method == "POST":
    #     post_data = request.POST or None
    #     if post_data != None:
    #         my_form = ProductForm(request.POST)
    #         if my_form.is_valid():
    #             input_title= my_form.cleaned_data.get("title")
    #             Product.objects.create(title=input_title)

    #   OTRA MANERA, UN POCO MÁS CORTA:
    # form=ProductForm()
    # if request.method= "POST":
    #     form = ProductForm(request.POST)

    # LO MISMO SE LOGRA CON LA PROXIMA LINEA:
    form = ProductForm(request.POST or None)

    if form.is_valid():
        # Esta limpieza y creación de la instancia se realiza
        # data = form.cleaned_data            de una manera más
        # Product.objects.create(**data)      conveniente, como
        #                                 en las dos siguientes:
        obj = form.save(commit=False)
        # entremedio uno podría trabajar sobre obj y luego:
        obj.save()

        form = ProductForm()  # con esto reseteamos el contenido del form

    context = {"form": form}
    return render(request, "products/forms.html", context)


def search_view(request, *args, **kwargs):
    query = request.GET.get("q")
    # qs = Product.objects.filter(title__icontains=query[0])
    qs = str(query)
    print(qs)
    context = {"name": "abc", "query": qs}
    return render(request, "products/search.html", context)
