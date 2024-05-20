from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse
from .models import *
from .forms import * 
#involving decorators to implement authentication
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

#login and register views
def registerpage(request):
    form =CreateUserForm()
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user =form.cleaned_data.get('username')
            messages.success(request, 'Account was created for'+ user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'DaystarApp/register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
          

    context = {}    
    return render(request, 'DaystarApp/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')



# Create your views here.
def index(request):
    return render(request, 'DaystarApp/index.html')

@login_required
def home(request):
    return render(request, 'DaystarApp/home.html')

def about(request):
    return render(request, 'DaystarApp/about.html')

# Create your views here.

def Sitters(request):
    return render(request, 'DaystarApp/addsitters.html')

def babies(request):
    return render(request, 'DaystarApp/addbabies.html')

@login_required
def display_babies(request):
    allbabies = BabyReg.objects.all()
    return render(request, 'DaystarApp/display_babies.html', {'allbabies': allbabies}) #babies list 


def AddBabies(request):    
    getbabiesform  = BabyRegForm()
    BabiesForm =  BabyRegForm(request.POST)
    if request.method == 'POST':
        if BabiesForm.is_valid():
            BabiesForm.save()
            print("form is not valid")
            print(BabiesForm)
            
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'DaystarApp/addbabies.html', {'getbabiesform': getbabiesform})

def delete_baby(request, BabyReg_id):
    babies = BabyReg.objects.filter(id=BabyReg_id).delete()
    redirect_url = reverse('home')
    return HttpResponseRedirect(redirect_url)

def edit(request,id):
    if request.method =='POST':
     baby = BabyReg.objects.get(pk=id)
     form = BabyRegForm(request.POST, instance=baby)
     if form.is_valid():
        form.save()
        return render(request, 'DaystarApp/edit.html', {
            'form':form,
            'success':True
            })
    else:
        baby = BabyReg.objects.get(pk=id)
        form = BabyRegForm(instance=baby)
    return render(request, 'DaystarApp/edit.html',{'form':form})


def present_babies(request):
    attendance_list = BabyAttendance.objects.all()
    return render(request, 'DaystarApp/presentbabies.html', {'attendance_list': attendance_list})
def baby_attendance(request):
    if request.method == 'POST':
        form = BabyAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = BabyAttendanceForm() 
    
    return render(request, 'DaystarApp/baby_attendance.html', {'form': form})








def allsitters(request):
    allsitters = Sitter.objects.all()
    return render(request, 'DaystarApp/allsitters.html', {'allsitters': allsitters}) #sitters list 


def addsitters(request):    
    getsittersform = (SitterForm)
    SittersForm =  SitterForm(request.POST)
    if request.method == 'POST':
        if SittersForm .is_valid():
            SittersForm .save()
            print("form is not valid")
            print(SittersForm )
            
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'DaystarApp/addsitters.html', {'getsittersform': getsittersform})
def delete_sitter(request, BabyReg_id):
    sitters = Sitter.objects.filter(id=BabyReg_id).delete()
    redirect_url = reverse('home')
    return HttpResponseRedirect(redirect_url)

def edit_sitter(request,id):
    if request.method =='POST':
        sitter= Sitter.objects.get(pk=id)
        form = SitterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
        return render(request, 'DaystarApp/editsitter.html', {
            'form':form,
            'success':True
            })
    else:
        sitter = Sitter.objects.get(pk=id)
        form = SitterForm(instance=sitter)
    return render(request, 'DaystarApp/editsitter.html',{'form':form})


def sitter_attendance(request):
    if request.method == 'POST':
        form = SitterAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = SitterAttendanceForm() 
    
    return render(request, 'DaystarApp/sitter_attendance.html', {'form': form})

def present_sitters(request):
    attendance_list = SitterAttendance.objects.all()
    return render(request, 'DaystarApp/presentsitters.html', {'attendance_list': attendance_list})

#Payment views
@login_required
def addpayment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = PaymentForm() 
    
    return render(request, 'DaystarApp/addpayment.html', {'form': form})

@login_required
def paymentlist(request):
    payment_list = Payment.objects.all()
    return render(request, 'DaystarApp/paymentlist.html', {'payment_list': payment_list})

def edit_payment(request,id):
    if request.method =='POST':
     payment = Payment.objects.get(pk=id)
     form = PaymentForm(request.POST, instance=payment)
     if form.is_valid():
        form.save()
        return render(request, 'DaystarApp/editpayment.html', {
            'form':form,
            'success':True
            })
    else:
        payment = Payment.objects.get(pk=id)
        form = PaymentForm(instance=payment)
    return render(request, 'DaystarApp/editpayment.html',{'form':form})


@login_required
def doll(request): #doll table
    dolls=Doll.objects.all()
    return render(request,'DaystarApp/doll.html',{'dolls':dolls}) 


# @login_required
def issue_item(request,id):  #selling of dolls
    issued_item=Doll.objects.get(id=id) 
    sales_form=SalesrecordForm(request.POST)  

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale=sales_form.save(commit=False)
            new_sale.doll=issued_item
            new_sale.unit_price=issued_item.unit_price
            new_sale.save()
            issued_quantity=int(request.POST['quantity_sold'])
            issued_item.quantity-=issued_quantity
            issued_item.save()
            print(issued_item.doll_name)
            print(request.POST['quantity_sold'])
            print(issued_item.quantity)
            return redirect('receipt')
    return render(request, 'DaystarApp/issue_item.html',{'sales_form':sales_form} )
def edit_doll(request,id):
    if request.method =='POST':
        doll=Doll.objects.get(id=id) 
        form = DollForm(request.POST, instance=doll)
        if form.is_valid():
            form.save()
            return render(request, 'DaystarApp/edit_doll.html', {
            'form':form,
            'success':True
            })
    else:
        doll = Doll.objects.get(id=id) 
        form = DollForm(request.POST, instance=doll)
    return render(request, 'DaystarApp/edit_doll.html',{'form':form})



def receipt(request):
    sales= Salesrecord.objects.all().order_by('id') 
    return render(request,'DaystarApp/receipt.html',{'sales':sales})  

# #@login_required
def receipt_detail(request,id):
    receipt = Salesrecord.objects.get(id=id)
    return render(request,'DaystarApp/receipt_detail.html',{'receipt':receipt})


# #@login_required
def add_to_stock(request,id):
    issued_item = Doll.objects.get(id=id)
    if request.method == 'POST':
        form = DollForm(request.POST)
        if form.is_valid():
            received_quantity = request.POST.get('received_quantity')
            if received_quantity:
                try:
                    added_quantity = int(received_quantity)
                    issued_item.quantity += added_quantity
                    issued_item.save()
                    print(added_quantity)
                    print(issued_item.quantity)
                    return redirect('doll')
                except ValueError:
                    return HttpResponseBadRequest("Invalid quantity")
            else:
                print("Form is not valid")
    else:
        form = DollForm()
    return render(request, 'DaystarApp/add_to_stock.html', {'form': form})
  

#trial 
def trial(request):
    baby_attendance_today = BabyAttendance.objects.filter(timeIn__date=timezone.now().date())
    children_present = baby_attendance_today.count()


    babies_status = []
    for attendance in baby_attendance_today:
        status = 'Checked In' if attendance.timeOut is None else 'Checked Out' #If attendance.timeOut is None, it means the baby has not been checked out yet, so the status is 'Checked In'.
        #If attendance.timeOut has a value, it means the baby has been checked out, so the status is 'Checked Out'.

        babies_status.append({   #This creates a dictionary for each attendance record and appends it to the babies_status list:
            'baby': attendance.B_name.B_name,
            'status': status,
            'timeIn': attendance.timeIn,
            'timeOut': attendance.timeOut,
        })
        sitter_attendance_today = SitterAttendance.objects.filter(timeIn__date=timezone.now().date())
        sitters_present = baby_attendance_today.count()
    sitters_status = []
    for attendance in sitter_attendance_today:
        status = 'Checked In' if attendance.timeOut is None else 'Checked Out'
        sitters_status.append({
            'sitter': attendance.S_name.S_name,
            'status': status,
            'timeIn': attendance.timeIn,
            'timeOut': attendance.timeOut,
        })
    
    context = {
        'children_present': children_present,
        'babies_status': babies_status,
        'sitters_status': sitters_status,
    }
    
   
    return render(request, 'DaystarApp/trial.html', context)
def baby_checkin(request):
    if request.method == 'POST':
        form = BabyAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trial')
    else:
        form = BabyAttendanceForm()
    return render(request, 'DaystarApp/baby_checkin.html', {'form': form})

def sitter_checkin(request):
    if request.method == 'POST':
        form = SitterAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trial')
    else:
        form = SitterAttendanceForm()
    return render(request, 'DaystarApp/sitter_checkin.html', {'form': form})

def baby_checkout(request):
    if request.method == 'POST':
        form = BabyCheckoutForm(request.POST)
        if form.is_valid():
            baby_attendance = BabyAttendance.objects.filter(B_name=form.cleaned_data['B_name'], timeOut__isnull=True).first()
            if baby_attendance:
                baby_attendance.timeOut = timezone.now()
                baby_attendance.save()
            return redirect('trial')
    else:
        form = BabyCheckoutForm()
    return render(request, 'DaystarApp/baby_checkout.html', {'form': form})

def sitter_checkout(request):
    if request.method == 'POST':
        form = SitterCheckoutForm(request.POST)
        if form.is_valid():
            sitter_attendance = SitterAttendance.objects.filter(S_name=form.cleaned_data['S_name'], timeOut__isnull=True).first()
            if sitter_attendance:
                sitter_attendance.timeOut = timezone.now()
                sitter_attendance.save()
            return redirect('trial')
    else:
        form = SitterCheckoutForm()
    return render(request, 'DaystarApp/sitter_checkout.html', {'form': form})