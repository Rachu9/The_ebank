
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Account, Transaction, BillPayment
from .forms import TransactionForm, BillPaymentForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not Account.objects.filter(user=user).exists():
                Account.objects.create(user=user, balance=500000.00)
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    accounts = Account.objects.filter(user=user)
    transactions = Transaction.objects.filter(
        sender__user=user
    ).select_related('sender', 'receiver') | Transaction.objects.filter(
        receiver__user=user
    ).select_related('sender', 'receiver')
    
    bill_payments = BillPayment.objects.filter(account__user=user)
    
    return render(request, 'dashboard.html', {
        'accounts': accounts, 
        'transactions': transactions, 
        'bill_payments': bill_payments
    })

@login_required
def transfer_funds(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST, user=request.user)
        if form.is_valid():
            # Get cleaned data from the form
            receiver = form.cleaned_data.get('receiver')
            amount = form.cleaned_data.get('amount')
            
            # Get the sender (logged-in user) and check if the receiver is not the sender
            sender = request.user.account
            if sender == receiver:
                messages.error(request, "You cannot transfer funds to yourself.")
                return redirect('transfer_funds')
            
            # Check if the sender has sufficient funds
            if sender.balance < amount:
                messages.error(request, "Insufficient funds.")
                return redirect('transfer_funds')
            
            # Perform the transfer
            sender.balance -= amount
            receiver.balance += amount
            sender.save()
            receiver.save()
            
            # Create a transaction record
            Transaction.objects.create(
                sender=sender,
                receiver=receiver,
                amount=amount
            )
            
            messages.success(request, "Funds transferred successfully!")
            return redirect('transaction_history')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = TransactionForm(user=request.user)
    
    return render(request, 'transfer_funds.html', {'form': form})





@login_required

def pay_bill(request):
    if request.method == 'POST':
        form = BillPaymentForm(request.POST)
        if form.is_valid():
            account_id = form.cleaned_data['account'].id
            amount = form.cleaned_data['amount']
            bill_type = form.cleaned_data['bill_type']

            try:
                account_instance = Account.objects.get(id=account_id)
                bill_payment = BillPayment(account=account_instance, amount=amount, bill_type=bill_type)
                bill_payment.save()
                messages.success(request, 'Bill paid successfully!')
                return redirect('bill_payment_history')  # Redirect to history page
            except Account.DoesNotExist:
                messages.error(request, 'Account does not exist.')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = BillPaymentForm()
    
    return render(request, 'pay_bill.html', {'form': form})

# def pay_bill(request):
#     if request.method == 'POST':
#         form = BillPaymentForm(request.POST)
#         if form.is_valid():
#             account = form.cleaned_data['account']
#             amount = form.cleaned_data['amount']
#             bill_type = form.cleaned_data['bill_type']

#             try:
#                 account_instance = Account.objects.get(id=account.id)
#                 bill_payment = BillPayment(account=account_instance, amount=amount, bill_type=bill_type)
#                 bill_payment.save()
#                 messages.success(request, 'Bill paid successfully!')
#                 return redirect('bill_payment_history')
#             except Account.DoesNotExist:
#                 messages.error(request, 'Account does not exist.')
#         else:
#             messages.error(request, 'Form is not valid.')
#     else:
#         form = BillPaymentForm()
    
#     return render(request, 'pay_bill.html', {'form': form})


@login_required
def pay_bill(request):
    if request.method == 'POST':
        form = BillPaymentForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']
            amount = form.cleaned_data['amount']
            bill_type = form.cleaned_data['bill_type']

            try:
                account_instance = Account.objects.get(id=account.id)
                bill_payment = BillPayment(account=account_instance, amount=amount, bill_type=bill_type)
                bill_payment.save()
                print(f'Bill Payment Saved: {bill_payment}')  # Debugging
                messages.success(request, 'Bill paid successfully!')
                return redirect('bill_payment_history')
            except Account.DoesNotExist:
                messages.error(request, 'Account does not exist.')
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = BillPaymentForm()

    return render(request, 'pay_bill.html', {'form': form})


@login_required
def transaction_history(request):
    transactions = Transaction.objects.all().order_by('-timestamp')
    return render(request, 'transaction_history.html', {'transactions': transactions})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_required
def logout(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        if not Account.objects.filter(user=instance).exists():
            Account.objects.create(user=instance, balance=500000.00)




# def bill_payment_history(request):
#     if request.user.is_authenticated:
#         try:
#             user_account = Account.objects.get(user=request.user)
#             bill_payments = BillPayment.objects.filter(account=user_account).order_by('-timestamp')
#             return render(request, 'bill_payment_history.html', {'bill_payments': bill_payments})
#         except Account.DoesNotExist:
#             messages.error(request, 'Account not found.')
#             return redirect('login')
#     else:
#         return redirect('login')

@login_required
def bill_payment_history(request):
    try:
        user_account = Account.objects.get(user=request.user)
        print(f'User Account: {user_account}')  # Debugging
        bill_payments = BillPayment.objects.filter(account=user_account).order_by('-timestamp')
        print(f'Bill Payments: {bill_payments}')  # Debugging
        return render(request, 'bill_payment_history.html', {'bill_payments': bill_payments})
    except Account.DoesNotExist:
        messages.error(request, 'Account not found.')
        return redirect('login')
