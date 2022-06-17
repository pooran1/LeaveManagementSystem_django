
from .forms import Leave_type_Form, LeaveCreationForm, ProfileUpdateForm2, RegisterUserForm2, RoleForm
from .models import Leave_type, LeaveBank, Role
from .forms import PermissionForm
from .models import Permission
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as loginuser, logout, update_session_auth_hash
from .forms import RegisterUserForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile, Role
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.contrib import messages


from .models import Profile

from django.contrib.auth.models import User, Permission


# -----------home--------------------


@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        show_leave_link = "yes"
        print(user)
        roles = Role.objects.filter(Q(name='HR') | Q(name='Team lead'))
        Uprofile = Profile.objects.filter(
            Q(reporting_manager=user) | Q(profile_user=user))
        # user_role = Profile.objects.get(profile_user=user).role.name
        # if user_role in ['HR', 'Team lead']:
        #     show_leave_link = "no"
        user_role = request.user.profile_user.role.name
        if user_role in ['HR', 'Team lead']:
            show_leave_link = "no"

    return render(request, 'index.html', context={'Uprofile': Uprofile, 'name': request.user.username, 'roles': roles, 'current_user_role': user_role, 'show_leave': show_leave_link})


# ---------------login------------------------------


def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, 'login.html', context=context)
    else:
        # reed the data
        print(type(request.GET))
        print(type(request.POST))
        print(request.POST, "IIIIIIIIIIII")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # print(user)
            if user is not None:
                loginuser(request, user)
                return redirect('home')

        else:
            context = {
                "form": form
            }
            return render(request, 'login.html', context=context)

# -----------------signup/registor----------------------------


def signup_view(request):
    if request.method == "GET":
        form = RegisterUserForm2()
        context = {
            'form': form
        }
        return render(request, 'signup_normal_user.html', context=context)
    else:
        # read the data or form filed ko read kaerna
        print(request.POST, "IIIIIIIIIIII")
        form = RegisterUserForm2(request.POST)
        context = {
            'form': form
        }
        # if form.is_valid():
        #     return HttpResponse('form is valid')
        # else:
        #     return render(request, 'sinup.html', context=context)

        if form.is_valid():
            # print(form.cleaned_data)
            # get the data when user is post and send though email
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')

            subject = 'new user'
            massage = f'hi{username} \n cogratulation your account is create \n your login your Account \n usersname: {username} \n password:{password1}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, massage, from_email,
                      recipient_list, fail_silently=False)
            user = form.save()
            # reporting_manager = form.cleaned_data.get('reporting_manager')
            contact_no = form.cleaned_data.get('contact_no')
            # leave_assign = form.cleaned_data.get('leave_assign')
            gender = form.cleaned_data.get('gender')
            departmant = form.cleaned_data.get('departmant')
            role = form.cleaned_data.get('role')
            category = form.cleaned_data.get('category')
            Permissions = form.cleaned_data.get("permission")
            # status = form.cleaned_data.get('status')
            print(user, contact_no, gender, 'ggggggggggg')

            user_profile = Profile.objects.create(
                contact_no=contact_no,  gender=gender, departmant=departmant, role=role,  category=category, profile_user=user)
            for p in Permissions:
                user_profile.Permission.add(p)
            user_profile.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup_normal_user.html', context=context)


def sinup(request):
    if request.method == "GET":
        form = RegisterUserForm()
        context = {
            'form': form
        }
        return render(request, 'sinup.html', context=context)
    else:
        # read the data or form filed ko read kaerna
        print(request.POST, "IIIIIIIIIIII")
        form = RegisterUserForm(request.POST)
        context = {
            'form': form
        }
        # if form.is_valid():
        #     return HttpResponse('form is valid')
        # else:
        #     return render(request, 'sinup.html', context=context)

        if form.is_valid():
            # print(form.cleaned_data)
            # get the data when user is post and send though email
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')

            # subject = ' new user'
            # massage = f'hi{username} \n cogratulation your Account is create \n your login your LMS \n usersname: {username} \n password:{password1}'
            # from_email = settings.EMAIL_HOST_USER
            # recipient_list = [email]
            # send_mail(subject, massage, from_email,
            #           recipient_list, fail_silently=False)

            subject = ' new user'
            massage = f'hi{username} \n cogratulation your Account is create \n your login your LMS \n usersname: {username} \n password:{password1}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, massage, from_email,
                      recipient_list, fail_silently=False)
            user = form.save()
            reporting_manager = form.cleaned_data.get('reporting_manager')
            contact_no = form.cleaned_data.get('contact_no')
            leave_assign = form.cleaned_data.get('leave_assign')
            gender = form.cleaned_data.get('gender')
            departmant = form.cleaned_data.get('departmant')
            role = form.cleaned_data.get('role')
            Permissions = form.cleaned_data.get("permission")
            category = form.cleaned_data.get('category')
            # status = form.cleaned_data.get('status')
            print(user, reporting_manager, contact_no, gender, 'ggggggggggg')
            user_profile = Profile.objects.create(
                reporting_manager=reporting_manager, contact_no=contact_no, leave_assign=leave_assign, gender=gender, departmant=departmant, role=role, category=category, profile_user=user)
            for p in Permissions:
                user_profile.Permission.add(p)
            user_profile.save()
            if user is not None:
                return redirect('home')
        else:
            return render(request, 'sinup.html', context=context)

# -------------------logout/sinout---------------------------------


def signout(request):
    logout(request)
    return redirect('login')


# -----------------------userupdate-------------------------

@login_required(login_url='login')
def updateuser(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm2(request.POST,
                                        instance=request.user.profile_user)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated!')
                return redirect('home')

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfileUpdateForm2(instance=request.user.profile_user)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, 'updateuser.html', context)
    else:
        return redirect('login')

# -----------------change-password----------------


def user_change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # update  session  ker na ho ta kun ke him ager password change ker te hn to him direct logot ker de ta gn aus ke lya him update session ker te hn
                update_session_auth_hash(request, fm.user)
                
                return redirect('login')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'changepassword.html', {'form': fm})
    else:
        return redirect('login')


# ----------enable------------------


def active(request, id):
    print(id)
    prnt = User.objects.get(id=id)
    prnt.is_active = True
    prnt.save()
    return redirect('home')


# ----------disabled------------------


def Inactive(request, id):
    print(id)
    prnt = User.objects.get(id=id)
    prnt.is_active = False

    prnt.save()
    return redirect('home')


# -------------------user update by reporting manager-------------

@login_required(login_url='login')
def updateuser_reporting_manager(request, id):
    u = get_object_or_404(User, id=id)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=u)
        p_form = ProfileUpdateForm(request.POST,
                                   instance=u.profile_user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
           
            return redirect('home')

    else:
        u_form = UserUpdateForm(instance=u)
        p_form = ProfileUpdateForm(instance=u.profile_user)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'updateuser.html', context)


# ------cretePermission-----------


def create_permission(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = PermissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

    context['form'] = form
    return render(request, "create_permission.html", context)


# --------updatepermission--------
def update_Permssion(request, id):

    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Permission, id=id)

    # pass the object as instance in form
    form = PermissionForm(request.POST or None, instance=obj)

 # form in save the data redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect("/"+id)

    context["form"] = form

    return render(request, "update_Permission.html", context)


# ----------enable_permission------------------


def active_permission(request, id):
    print(id)
    perm = Permission.objects.get(id=id)
    perm.is_active = True
    perm.save()
    return redirect('home')


# ----------disable_permission------------------


def Inactive_permission(request, id):
    print(id)
    perm = Permission.objects.get(id=id)
    perm.is_active = False

    perm.save()
    return redirect('home')


# -------listviewRole--------
def list_view_Role(request):

    context = {}

    context["roles"] = Role.objects.all()

    return render(request, "list_view_role.html", context)


# ------creteRole-----------


def create_role(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = RoleForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            name = form.cleaned_data.get('name')
            Permissions = form.cleaned_data.get("permission")
            instance = Role.objects.create(name=name)
            for p in Permissions:
                instance.Permission.add(p)
            instance.save()

            return redirect('home')  # Redirect after POST
    else:

        form = RoleForm()  # An unbound form

    return render(request, 'create_role.html', {'form': form})


#


# --------updateRole--------


def update_role(request, id):

    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Role, id=id)

    if request.method == "GET":
        form = RoleForm(instance=obj)
        context["form"] = form

        return render(request, "update_Role.html", context)
    else:

        form = RoleForm(request.POST or None, instance=obj)

        # save the data from the form and
        # redirect to detail_view
        if form.is_valid():
            name = form.cleaned_data.get('name')
            Permissions = form.cleaned_data.get("permission")
            instance = Role.objects.filter(id=id)
            print(Permissions)
            instance.update(name=name)
            for r in instance:
                for p in Permissions:
                    r.Permission.add(p)

            return redirect("home")

        # add form dictionary to context
        context["form"] = form

        return render(request, "update_Role.html", context)


# ----------enable_role------------------


def active_role(request, id):
    print(id)
    r = Role.objects.get(id=id)
    r.is_active = True
    r.save()
    return redirect('home')


# ----------disable_role------------------


def Inactive_role(request, id):
    print(id)
    r = Role.objects.get(id=id)
    r.is_active = False

    r.save()
    return redirect('home')


# --------------list
def list_view_leave(request):

    context = {}

    context["LeavesType"] = Leave_type.objects.all()

    return render(request, "list_view_Leave_type.html", context)


# ------crete_leave type-----------


def create_leave_type(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = Leave_type_Form(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create_leave_type.html", context)


# --------updatepermission--------
def update_leave_type(request, id):

    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Leave_type, id=id)
    if request.method == "GET":
        form = Leave_type_Form(instance=obj)
        context["form"] = form

        return render(request, "update_leave_type.html", context)
    else:

        # pass the object as instance in form
        form = Leave_type_Form(request.POST or None, instance=obj)

        # form in save the data redirect to detail_view
        if form.is_valid():
            form.save()
            return redirect("update_leave_type/"+id)

        # context dictionary to add form
        context["form"] = form

        return render(request, "update_leave_type.html", context)

# -----leave sections ----------


@login_required(login_url='login')
def leave(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = LeaveCreationForm()
        roles = Role.objects.filter(Q(name='HR') | Q(name='Team lead'))
        user_role = Profile.objects.get(profile_user=user).role.name
        la = LeaveBank.objects.filter(Q(user__profile_user__reporting_manager=user) | Q(
            user=user))
        show_leave_link = "yes"
        if user_role in ['HR', 'Team lead']:
            show_leave_link = "no"

    return render(request, 'leave.html', context={'form': form, 'la': la, 'roles': roles, 'current_user_role': user_role, 'show_leave': show_leave_link})


# ------apply leave --------
@login_required(login_url='login')
def apply_leave(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
    form = LeaveCreationForm(data=request.POST)
    if form.is_valid():
        print(form.changed_data)
        leave = form.save(commit=False)
        leave.user = user
        leave.save()
        print(leave)
        return redirect('leave')
    else:
        print("jgjggjg")
        return render(request, 'leave.html', context={'form': form})


# --------update--------


def update_appyleave(request, id):

    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(LeaveBank, id=id)

    # pass the object as instance in form
    form = LeaveCreationForm(request.POST or None, instance=obj)

    # form in save the data redirect to detail_view
    if form.is_valid():
        form.save()
        return redirect('leave')

    # context dictionary to add form
    context["form"] = form

    return render(request, "update_leave.html", context)


def approve(request, id):
    print(id)
    prnt = LeaveBank.objects.get(id=id)
    prnt.is_active = True
    prnt.status = 'approved'
    prnt.save()
    return redirect('leave')


def unapprove(request, id):
    print(id)
    prnt = LeaveBank.objects.get(id=id)
    prnt.is_active = False
    prnt.status = 'unapproved'
    prnt.save()
    return redirect('leave')
