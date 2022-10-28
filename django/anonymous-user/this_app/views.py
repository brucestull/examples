from django.http import HttpResponse

def index(request):

    ###################################################################
    # Print Statements
    # print('request.user: ', request.user)
    # request.user:  AnonymousUser
    # print('dir(request.user): ', dir(request.user))
    """
    dir(request.user):  [
        '__class__',
        '__delattr__',
        '__dict__',
        '__dir__',
        '__doc__',
        '__eq__',
        '__format__',
        '__ge__',
        '__getattribute__',
        '__gt__',
        '__hash__',
        '__init__',
        '__init_subclass__',
        '__int__',
        '__le__',
        '__lt__',
        '__module__',
        '__ne__',
        '__new__',
        '__reduce__',
        '__reduce_ex__',
        '__repr__',
        '__setattr__',
        '__sizeof__',
        '__str__',
        '__subclasshook__',
        '__weakref__',
        '_groups',
        '_user_permissions',
        'check_password',
        'delete',
        'get_all_permissions',
        'get_group_permissions',
        'get_user_permissions',
        'get_username',
        'groups',
        'has_module_perms',
        'has_perm',
        'has_perms',
        'id',
        'is_active',
        'is_anonymous',
        'is_authenticated',
        'is_staff',
        'is_superuser',
        'pk',
        'save',
        'set_password',
        'user_permissions',
        'username']
    """
    # print('request.user.username: ', request.user.username)
    # request.user.username:
    # print(type(request.user))
    # <class 'django.utils.functional.SimpleLazyObject'>
    ###################################################################

    return HttpResponse("String response!")

