from audioop import reverse
from django.shortcuts import redirect, render
from django.views.generic import DetailView,ListView,TemplateView
from .models import Profile,Item
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import MyCustomSignupForm,MyCustomLoginForm,AccountDetails,UsernameForm,PhotoProfileForm,ChangePasswordMyForm,UpdataItemForm,AddItemForm,StyleItem,ProfileCustomizer,CustomPasswordResetForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from allauth.account.views import SignupView, LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import update_session_auth_hash
from django.templatetags.static import static
from allauth.account.views import PasswordResetView, PasswordResetDoneView,PasswordResetFromKeyView,PasswordResetFromKeyDoneView

import requests

# class CustomPasswordResetView(PasswordResetFromKeyView):
#     form_class = CustomPasswordResetForm

def uploadToCloud(image):
    headers = {
    'Content-Type': 'image/png',
    }

    params = {
        'key': 'Aps889HQN06qspnJrlg9Xz',
    }

    data = image
    response = requests.post('https://www.filestackapi.com/api/store/S3', params=params, headers=headers, data=data)
    return str(response.json()["url"])

class ResetPasswordView(PasswordResetView):
    template_name = "forgotpassword.html"
    success_url = reverse_lazy("DoneforgetPassword")

class DoneResetPasswordView(PasswordResetDoneView):
    template_name = "forgotpasswordDone.html"

class ChangePasswordView(PasswordResetFromKeyView):
    form_class = CustomPasswordResetForm
    template_name = 'resetpassword.html'

    def get_success_url(self):
        return reverse('login')
    # success_url = reverse_lazy("account_reset_password_from_key_done_gg")
    

class ChangePasswordViewDone(PasswordResetFromKeyDoneView):
    template_name = "ChangedSuccess.html"

class HomeView(ListView):
    model = Profile
    template_name = 'home.html'
    context_object_name = "gg"
# class HomeView(TemplateView):
#     model = Profile
#     template_name = 'home.html'


class ProfileView(DetailView):
    model = Profile
    template_name  = 'index.html'
    context_object_name = 'profile'
    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        user = User.objects.get(username=username)
        profiles = get_object_or_404(Profile,username=user)
        return profiles
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs.get('username')
        userx = User.objects.get(username=username)
        items =Item.objects.filter(user__username=userx)
        context['items'] = items
        return context


class SignUpCutosm(SignupView):
    form_class = MyCustomSignupForm
    template_name = 'regsiter.html'
    success_url = reverse_lazy('Account')

    def form_valid(self, form):
        messages.success(self.request,'The account has been Created')
        return super().form_valid(form)
    def get_absolute_url(self):
        return reverse_lazy('Account', args=[str(self.id)])
    def form_invalid(self, form):
        if 'username' in form.errors:
            messages.error(self.request,'The Username has been taken')
        elif 'password1' in form.errors or 'password2' in form.errors:
            messages.error(self.request,'Password not match')
        elif 'email' in form.errors:
            messages.error(self.request,'The Email has been taken')

        return redirect(reverse_lazy('signup'))


class LoginCutosm(LoginView):
    form_class= MyCustomLoginForm
    template_name = 'login.html'
    success_url = reverse_lazy('Account')
    def form_valid(self, form):
        messages.success(self.request,'Login successful.')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,'Login failed')
        return redirect(reverse_lazy('login'))



class AccountView(LoginRequiredMixin,TemplateView):
    template_name  = 'Account.html'
    login_url = "login"
    def get(self, request, *args, **kwargs):
        BackgroundProfile = static('/asstes/images/backgroundProfile.jpg')
        mU = User.objects.get(username=request.user.username)
        mf = Profile.objects.get(username=mU)
        It = Item.objects.filter(user=mf)
        cForm = ProfileCustomizer(instance=mf)
        eform = AccountDetails(instance=mf)
        pform = UsernameForm(instance=mU)
        tform = PhotoProfileForm(instance=mf)
        gform = ChangePasswordMyForm(request.user)
        Aform = AddItemForm()
        return self.render_to_response({'cForm':cForm,'Aform':Aform,'eform': eform, 'tform': tform, 'pform': pform,"BackgroundProfile":BackgroundProfile,'show':mf,'gform':gform,'items':It})
    def post(self, request, *args, **kwargs):
        if request.POST.get('form_type') == 'eform':
            mU = User.objects.get(username=request.user.username)
            mf = Profile.objects.get(username=mU)
            form = AccountDetails(request.POST,instance=mf)
            if form.is_valid():
                form.save()
                return redirect ("Account")


        elif request.POST.get('form_type') == 'tform':
            mU = User.objects.get(username=request.user.username)
            mf = Profile.objects.get(username=mU)
            pform = UsernameForm(request.POST,instance=mU)
            tform = PhotoProfileForm(request.POST, request.FILES,instance=mf)

            if pform.is_valid() and tform.is_valid():
                pform.save()
                uploaded_file  = request.FILES["photoProfile"]
                file_contents = b''
                for chunk in uploaded_file.chunks():
                    file_contents += chunk
                
                urlImage= uploadToCloud(file_contents)
                mf.photoProfile = urlImage
                mf.save()
                
                return redirect ("Account")
        elif request.POST.get('form_type') == 'gform':
            print(request.POST)
            form = ChangePasswordMyForm(request.user,request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect ("Account")
        ###########################################################
        
        elif request.POST.get('form_type') == 'Aform':
            mU = User.objects.get(username=request.user.username)
            mf = Profile.objects.get(username=mU)
            it = Item
            form = AddItemForm(request.POST,request.FILES)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user.profile
                item.save()
                return redirect ("Account")
        elif request.POST.get('form_type') == 'cForm':
            mU = User.objects.get(username=request.user.username)
            mf = Profile.objects.get(username=mU)
            
            form = ProfileCustomizer(request.POST,request.FILES,instance=mf)
            if form.is_valid():
                form.save()
                return redirect ("Account")
            else:
                errors = form.errors 
                print(errors)

        return redirect ("Account")

        ###########################################################################










def error_404_view(request,exception):
    return render(request,"404.html")

def logout_view(request):
    logout(request)
    return redirect('home')


class UpdataItemView(LoginRequiredMixin,TemplateView):
    login_url = "login"
    template_name = 'edit.html'
    def get(self, request, *args,**kwargs):
        mU = User.objects.get(username=request.user.username)
        mf = Profile.objects.get(username=mU)
        It = Item.objects.filter(user=mf).get(pk=kwargs.get('pk'))
        Iform = UpdataItemForm(instance=It)
        Sform = StyleItem(instance=It)
        return self.render_to_response({'Iform':Iform,'It':It,'Sform':Sform})
    def post(self, request, *args, **kwargs):
        mU = User.objects.get(username=request.user.username)
        mf = Profile.objects.get(username=mU)
        It = Item.objects.filter(user=mf).get(pk=kwargs.get('pk'))
        if request.POST.get('form_type') == 'Iform':
            form = UpdataItemForm(request.POST,request.FILES,instance=It)

            if form.is_valid():
                form.save()
        elif request.POST.get('form_type') == 'Sform':
            form = StyleItem(request.POST,instance=It)
            if form.is_valid():
                form.save()
            print(form.errors)
        elif request.POST.get('form_type') == 'Dform':
            mU = User.objects.get(username=request.user.username)
            mf = Profile.objects.get(username=mU)
            It = Item.objects.filter(user=mf).get(pk=kwargs.get('pk'))
            It.delete()
            return redirect("Account")
        return redirect("Account")
    

