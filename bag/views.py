from django.shortcuts import render


def view_bag(request):
    """ Renders bag contents """

    return render(request, 'bag/bag.html')
