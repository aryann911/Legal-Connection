from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import *
from .forms import BookingForm
import datetime
from django.contrib import messages


def booknow(request):
    """renders to the booking page
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        # shows the message that the time of the day has been selected before
        date = datetime.datetime.strptime(str(request.POST['date']), '%Y-%m-%d')
        time = datetime.datetime.strptime(str(request.POST['time']), '%H:%M')
        time = request.POST['time']
        if Booking.objects.filter(date=date, time=time).exists():
            messages.error(request, "Sorry, this time is already booked, please select another time")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            return redirect('payment', booking_id=booking_form.id)
        else:
            messages.error(request, "Please enter correct data")
            return render(request, 'booknow.html', {'form': form})
    form = BookingForm()
    return render(request, 'booknow.html', {'form': form})


def bookings(request):
    """shows user bookings or redirects to the signup page
    """
    if request.user.is_authenticated:
        # Check if user is a lawyer
        try:
            if request.user.profile.user_type == 'lawyer':
                return redirect('lawyer_dashboard')
        except Profile.DoesNotExist:
            pass

        bookings = Booking.objects.filter(user=request.user)
        context = {
           'bookings': bookings
        }
        return render(request, 'bookings.html', context)
    else:
        return redirect('../accounts/signup')


def lawyer_dashboard(request):
    """
    View for lawyers to see all bookings
    """
    if not request.user.is_authenticated:
        return redirect('../accounts/signup')
    
    try:
        if request.user.profile.user_type != 'lawyer':
            messages.error(request, "Access denied. You are not registered as a lawyer.")
            return redirect('index')
    except Profile.DoesNotExist:
        messages.error(request, "Please select your role first.")
        return redirect('select_role')

    all_bookings = Booking.objects.all().order_by('date', 'time')
    context = {
        'bookings': all_bookings
    }
    return render(request, 'lawyer_dashboard.html', context)


from django.contrib.auth.decorators import login_required


@login_required
def select_role(request, role):
    """
    Sets the user's role (lawyer or client)
    """

    if role not in ['lawyer', 'client']:
        messages.error(request, "Invalid role selected.")
        return redirect('index')

    profile, created = Profile.objects.get_or_create(user=request.user)
    profile.user_type = role
    profile.save()

    messages.success(request, f"You are now logged in as a {role.capitalize()}.")
    if role == 'lawyer':
        return redirect('lawyer_dashboard')
    else:
        return redirect('bookings')


def change_booking(request, booking_id):
    """renders the change_booking page where the user can
    change a booking
    """
    record = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=record)

        date = datetime.datetime.strptime(str(request.POST['date']), '%Y-%m-%d')
        time = datetime.datetime.strptime(str(request.POST['time']), '%H:%M')
        time = request.POST['time']
        if Booking.objects.filter(date=date, time=time).exists():
            messages.error(request, "Sorry, this time is already booked, please select another time")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        if form.is_valid():
            form.save()
            messages.success(request, 'You succesfully updated your booking.')
            return redirect('bookings')
        # else:
        #     return render(request, 'change-booking.html', {'form': form})
    form = BookingForm(instance=record)
    context = {'form': form, 'record': record}
    return render(request, 'change-booking.html', context)


def delete_booking(request, booking_id):
    """
    renders the delete_booking page where the user can
    delete a booking
    """

    record = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=record)
        if record.delete():
            messages.success(request, 'Your booking has been deleted.')
            return redirect('bookings')

    form = BookingForm(instance=record)
    context = {
        'record': record}
    return render(request, 'delete-booking.html', context)


def payment(request, booking_id):
    """
    renders a dummy payment page
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user != booking.user:
        return redirect('bookings')

    if request.method == 'POST':
        # Simulate successful payment
        booking.is_paid = True
        booking.video_call_link = f"https://meet.jit.si/LegalConnectionBooking{booking.id}"
        booking.save()
        messages.success(request, 'Payment successful! Your video call link is ready.')
        return redirect('bookings')
    
    context = {'booking': booking}
    return render(request, 'payment.html', context)
