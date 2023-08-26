from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Journey, Car, Driver, Ride, User, Profile
from django.contrib import messages

# Create your views here.


def home(request):
    user = request.user
    if (user.is_authenticated):
        messages.success(request, (f"Welcome, { user.username.title() }!"))
    else:
        messages.error(request, ("Please Login to Access all features."))
    return render(request, "pool_car/index.html")


def publish(request):
    if request.method == 'POST':
        user, created = Profile.objects.filter(
            user=request.user)

        source = request.POST.get('source')
        destination = request.POST.get('destination')
        dateOfJourney = request.POST.get('date_of_journey')
        numberOfSeats = request.POST.get('number_of_seats')
        costPerPerson = request.POST.get('cost_per_person')
        journey, created = Journey.objects.get_or_create(
            source=source, destination=destination, date_of_journey=dateOfJourney, number_of_seats=numberOfSeats, cost_per_person=costPerPerson)
        journey.save()

        carName = request.POST['car_name']
        carNumber = request.POST['vehicle_number']
        car, created = Car.objects.get_or_create(
            car_name=carName, vehicle_number=carNumber)
        car.save()

        driverName = request.POST['driver_name']
        driverLicenceNumber = request.POST['driver_licence_number']

        driver, created = Driver.objects.get_or_create(
            driver_name=driverName, driver_licence_number=driverLicenceNumber)
        driver.save()

        ride = Ride.objects.create(publisher=user,
                                   journey_details=journey, car_details=car, driver_details=driver)
        # ride.poolers.add(user)
        print("Poolers = ")
        for p in ride.poolers.all():
            print(p.user.username)
        ride.save()
        return redirect(reverse('home-page'))
    return render(request, "pool_car/publish.html")


def search(request):
    user = request.user
    rides = Ride.objects.exclude(publisher__user__username=user.username)
    return render(request, "pool_car/search.html", {
        'rides': rides,
    })


def filter_rides(request):
    user = request.user
    rides = Ride.objects.exclude(publisher__user__username=user.username)
    try:
        source = request.GET.get('source')
        destination = request.GET.get('destination')
        date = request.GET.get('journey-date')
        if source != "" and destination != "" and date != "":
            rides = rides.filter(journey_details__source=source,
                                 journey_details__destination=destination, journey_details__date_of_journey=date)
        elif source != "" and destination != "" and date == "":
            rides = rides.filter(journey_details__source=source,
                                 journey_details__destination=destination)
        elif source == "" and destination == "" and date == "":
            rides = rides.all()
    except:
        pass
    return render(request, "pool_car/search.html", {
        'rides': rides,
    })


def delete_ride(request, ride_id):
    ride = Ride.objects.get(pk=ride_id)
    ride.delete()
    return redirect("published-rides-page")


def join_ride(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    exists = ride.poolers.filter(user=request.user)
    if exists:
        messages.warning(request, 'User has already joined')
        return redirect(request.META['HTTP_REFERER'])
    if not exists and ride.journey_details.number_of_seats > 0:
        ride.journey_details.number_of_seats -= 1
        ride.journey_details.save()
    else:
        messages.warning(request, 'No seats left')
        return render(request, 'pool_car/search.html')
    user = Profile.objects.create(user=request.user)
    ride.poolers.add(user)
    messages.success(request, 'Joined ride successfully')
    return render(request, 'pool_car/index.html')


def published_rides(request):
    user = request.user
    rides = Ride.objects.filter(publisher__user__username=user.username)
    return render(request, "pool_car/published.html", {
        'rides': rides,
    })


def about(request):
    return render(request, "pool_car/about.html")
