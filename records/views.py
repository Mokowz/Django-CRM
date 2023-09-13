from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import SignUpForm, RecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            return redirect('home')
        else:
            messages.success(request, "There was an eror logging in")
            return redirect('home')
    
    else:
        return render(request, 'home.html', {"records": records})
    



def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect("home")


def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(request, username = username, password = password)
            login(request, user)
            messages.success(request, "You have successfully registered! Welcome")
            return redirect("home")

    else:
        return render(request, 'signup.html', {'form': form})
    


# View single record
def view_record(request, pk):
    # Accessible to logged in users only
    if request.user.is_authenticated:
        record = Record.objects.get(id = pk)
        return render(request, 'single_record.html', {"record": record})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect("home")
    

# Add single record
def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added Successfully")
                return redirect("home")
        else:
            form = RecordForm()
            return render(request, 'add_record.html', {"form": form})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect("home")
    

# Update Record
def update_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        if request.method == "POST":
            form = RecordForm(request.POST, instance=record)
            if form.is_valid():
                form.save()
                messages.success(request, "Record was updated successfully")
                return redirect("home")
        else:
            form = RecordForm(instance=record)
            return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect("home")
    

# Delete a record
def delete_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect("home")
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect("home")