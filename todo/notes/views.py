from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages


from notes.forms import AddNoteForm, LoginForm
from notes.models import Note


def notes_index(request):
    notes = []
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddNoteForm(request.POST)
            if form.is_valid():
                Note.objects.create(
                    title=form.cleaned_data["title"], text=form.cleaned_data["text"]
                )
                return redirect("index")
        else:
            form = AddNoteForm()
        notes = Note.objects.all()
        return render(request, "note_list.html", {"notes": notes, "form": form})
    else:
        messages.info(request, f"You don't logIn")
        return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request, f"Authenticated successfully")
                    return redirect('index')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == "POST":
        logout(request)

        return redirect('home')
    return render(request, "logged_out.html",)

