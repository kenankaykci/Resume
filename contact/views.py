from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def contact_form(request):
    context = {'success': True, 'message': 'Contact form sent successfully!'}
    return JsonResponse(context)

def contact(request):
      return render(request, 'contact.html')


def contact_process(request):
    if request.method == 'POST':
        # Process form data here
        # For example, you can access form data like this:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Process the form data further (e.g., save to database, send email, etc.)

        # Return a JSON response indicating successful form submission
        return JsonResponse({'success': True, 'message': 'Form submitted successfully!'})
    else:
        # Return a JSON response for invalid request method (shouldn't happen in this case)
        return JsonResponse({'error': 'Invalid request method.'}, status=400)