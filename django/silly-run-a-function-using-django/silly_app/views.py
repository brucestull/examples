from django.http import HttpResponse

# from some_python_file import some_python_function
from some_python_file_with_main import some_python_function


def silly_view(request):

    some_python_function()
    
    return HttpResponse(
        '''
        This is a silly view. Check the console output where you
        are running this Django app.
        '''
    )
