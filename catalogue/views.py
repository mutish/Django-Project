from django.shortcuts import render, redirect
from catalogue.forms import CatalogueForm
from catalogue.models import Catalogue

# Create your views here.
def cat(request):
    if request.method == "POST":
        form = CatalogueForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
        else:
            form = CatalogueForm()
        return render(request, 'index.html',{'form': form})

def show(request):
    catalogues = Catalogue.objects.all()
    return render(request, "show.html", {'catalogues': catalogues})

def edit(request, id):
    catalogue = Catalogue.objects.get(id=id)
    return render(request, 'edit.html', {'catalogue':catalogue})
def update(request, id):
    catalogue = Catalogue.objects.get(id=id)
    form = CatalogueForm(request.POST, instance=catalogue)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return redirect(request, 'edit.html', {'catalogue': catalogue})
def destroy(request, id):
    catalogue = Catalogue.objects.get(id=id)
    catalogue.delete()
    return redirect("/show")

