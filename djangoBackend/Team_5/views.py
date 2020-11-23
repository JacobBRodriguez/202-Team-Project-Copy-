from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import Listing
from django.shortcuts import render, redirect


# from .models import
# Create your views here.
def index_view(request):
    # Render function takes request argument
    # return HTML
    return render(request, 'main_app/index.html')


def login_view(request):
    # return sign-up.html
    if request.method == 'GET':
        return render(request, 'main_app/login.html')

    elif request.method == "POST":
        name = request.POST.get('username', '')
        passW = request.POST.get('password', '')

        user = authenticate(username=name, password=passW)
        if user is not None:
            login(request, user)
            return redirect('/index.html')
        else:
            return render(request, 'main_app/login.html')

    # return login.html
    return render(request, 'main_app/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'main_app/index.html')


def services_view(request):
    # return services.html
    return render(request, 'main_app/services.html')


def searching_view(request):
    queryset_list = Listing.objects.order_by('-list_date')

    context = {
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'main_app/searching.html', context)


def posting_view(request):

    if request.method == 'GET':
        return render(request, 'main_app/posting.html')

    elif request.method == "POST":
        listing = Listing()
        listing.title = request.POST.get('title')
        listing.address1 = request.POST.get('address1')
        listing.address2 = request.POST.get('address2')
        listing.description = request.POST.get('Description')
        listing.zipcode = request.POST.get('zipcode')
        listing.category = request.POST.get('Category')
        listing.bedrooms = request.POST.get('Bedroom')
        listing.bathrooms = request.POST.get('Bathroom')
        listing.price = request.POST.get('price')
        images = request.POST.getlist('img')

        if images:
            listing.photo_main = images[0]
            del images[0]
            if images:
                listing.photo_1 = images[0]
                del images[0]
                if images:
                    listing.photo_2 = images[0]
                    del images[0]
                    if images:
                        listing.photo_3 = images[0]
                        del images[0]
                        if images:
                            listing.photo_4 = images[0]
                            del images[0]
                            if images:
                                listing.photo_5 = images[0]
                                del images[0]
                                if images:
                                    listing.photo_6 = images[0]
        listing.save()
        return redirect('/services.html')

    # If error out return to sign-up page
    # TODO: Give message of invalid sign-up
    return render(request, 'main_app/posting.html')
    # return posting.html
    return render(request, 'main_app/posting.html')


def approve_listing_view(request):
    # return approve_listing.html
    return render(request, 'main_app/approve_listing.html')


def offers_view(request):
    # return offers.html
    return render(request, 'main_app/offers.html')


def remove_user_view(request):
    # return remove_user.html
    return render(request, 'main_app/remove_user.html')


def send_offer_view(request):
    # return send offer.html
    return render(request, 'main_app/send offer.html')


def sign_up_view(request):
    # return sign-up.html
    if request.method == 'GET':
        return render(request, 'main_app/sign-up.html')
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main_app/login.html')
    # If error out return to sign-up page
    # TODO: Give message of invalid sign-up
    return render(request, 'main_app/sign-up.html')


def single_view(request):
    # return single.html
    return render(request, 'main_app/single.html')


# Other views for behavior

def determine_route_index_view(request):
    if request.user.is_authenticated:
        return redirect('/services.html')

    return redirect('/login.html')


def search_view(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category=category)

    # Zipcode
    if 'zipcode' in request.GET:
        zipcode = request.GET['zipcode']
        if zipcode:
            queryset_list = queryset_list.filter(zipcode=zipcode)

    # Address
    if 'address' in request.GET:
        address = request.GET['address']
        if address:
            queryset_list = queryset_list.filter(address1__icontains=address)

    # Year
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            # TODO: Item not in posting functionality yet
            print(year)
            # queryset_list = queryset_list.filter(year=year)

    # Min Sqft
    if 'square' in request.GET:
        square = request.GET['square']
        if square:
            # TODO: Item not in posting functionality yet
            print(square)
            # queryset_list = queryset_list.filter(square=square)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms=bedrooms)

    # Bathrooms
    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            queryset_list = queryset_list.filter(bathrooms=bathrooms)

    context = {
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'main_app/searching.html', context)

