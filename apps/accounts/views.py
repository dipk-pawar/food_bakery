from .forms import UserForm
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from django.contrib import messages


# Create your views here.
class RegisterUser(View):
    form_class = UserForm
    model = User
    template_name = "accounts/register.html"

    def get(self, request, pk=None):
        if pk is None:
            # GET request for creating a new object
            form = self.form_class()
        else:
            # GET request for retrieving an existing object
            user_model = get_object_or_404(self.model, pk=pk)
            form = self.form_class(instance=user_model)
        return render(request, self.template_name, context={"form": form})

    def post(self, request, pk=None):
        form = self.form_class(request.POST)
        if form.is_valid():
            if pk is not None:
                # POST request for updating an existing object
                user_model = get_object_or_404(self.model, pk=pk)
                form.instance = user_model
            # POST request for creating a new object
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.role = self.model.CUSTOMER
            user.save()
            messages.success(request, "Your account has been registered sucessfully!")
            return redirect("register")
        return render(request, self.template_name, {"form": form})
