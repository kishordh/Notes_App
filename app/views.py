from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Efile
from .forms import NotesForm, NotesUpdate
# Create your views here.
def index(request):
    todo = Efile.objects.all()
    cnt = todo.count()
    complete = Efile.objects.filter(complete=True)
    comp = complete.count() 
    incomplte = cnt - comp
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = NotesForm()

    context = {
            'todos': todo,
            'form': form,
            'cnt':cnt,
            'comp':comp,
            'incomplte':incomplte,

    }
    return render(request, 'efiles/index.html', context)

def update(request, pk):
    todo = Efile.objects.get(id=pk)

    if request.method == 'POST':
        form = NotesUpdate(request.POST , instance=todo)
        if form.is_valid():
            form.save()

        return redirect('/')
    
    else:
        form = NotesUpdate(instance=todo)
    context = {
                'form': form
    }
    return render(request, 'efiles/update.html', context )

def delete(request, pk):
    todo = Efile.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
    return render(request, 'efiles/delete.html')