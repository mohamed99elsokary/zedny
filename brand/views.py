from django.shortcuts import render
from . import models, forms
from django.shortcuts import get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from zipfile import ZipFile


def all(request):
    brands = models.Brand.objects.all()
    paginator = Paginator(brands, 3)
    page_number = request.GET.get("page")
    brands = paginator.get_page(page_number)
    context = {"brands": brands}
    return render(request, "all.html", context)


def add(request):
    form = forms.BrandForm
    if request.method == "POST":
        form = forms.BrandForm(request.POST, request.FILES)
        if form.is_valid():
            brand = form.save()

        brochures = request.FILES.getlist("brochure")
        for brochure in brochures:
            models.Brochure.objects.create(brand_id=brand.id, brochure=brochure)

    context = {"form": form}
    return render(request, "add.html", context)


def details(request, id):
    brand = get_object_or_404(models.Brand, id=id)
    brochures = get_list_or_404(models.Brochure, brand=brand)
    zip = ZipFile(f"media/zips/{brand.id}.zip", "w")
    for brochure in brochures:
        zip.write(f"{brochure.brochure}")
    data_url = f"/media/media/zips/{brand.id}.zip"
    context = {"brand": brand, "data_url": data_url}
    return render(request, "details.html", context)
