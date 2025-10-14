from django.shortcuts import render
from .forms import ComplaintForm

def complaint_view(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'complaint/contact.html', {
                'form': ComplaintForm(),  # return a fresh form
                'success': True
            })
    else:
            form = ComplaintForm()  # initial empty form

    return render(request, 'complaint/contact.html', {'form': form})
