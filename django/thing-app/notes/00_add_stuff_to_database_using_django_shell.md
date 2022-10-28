# Add Stuff to Database by Using Django Shell

## Process:

1. Start Django Shell:
    * `python .\manage.py shell`

1. Import models:
    * `from the_app.models import TheThing`

1. Create a `TheThing` object:
    * `a_specific_thing = TheThing.objects.create(attribute_01='String less than 20', attribute_02='String much much much much much greater than 20')`
        ```
        >>> a_specific_thing = TheThing.objects.create(attribute_01='String less than 20', attribute_02='String much much much much much greater than 20')
        >>>
        ```
    * NOTES:
        * Since we used `create()`, we do not need to call `save()` because `create()` creates the object and saves it to the database.
        * Our `models.CharField` attribute specifies `max_length=20`:
            * But the value for `attribute_02` is longer than `max_length`:
                * We can do this because the `max_length` `models.CharField` attribute only specifies `max_length` length for forms which Django creates.

1. Print out the thing we just created:
    * `a_specific_thing`
        ```
        >>> a_specific_thing
        <TheThing: String less than 20 : String much much much much much greater than 20>
        >>>
        ```

1. Get all `TheThing` objects from the database:
    * `all_the_things = TheThing.objects.all()`
        ```
        >>> all_the_things = TheThing.objects.all()
        >>>
        ```

1. Print out the variable we just assigned to `TheThing.objects.all()`:
    * `all_the_things`
        ```
        >>> all_the_things
        <QuerySet [<TheThing: Attribute 01 stuff! : Attribute 02 stuff?>, <TheThing: Something? : Something Else!>, <TheThing: String less than 20 : String much much much much much greater than 20>]>
        >>
        ```

1. Print out some stuff:
    * The commands:
        ```
        for thing in all_the_things:
            thing.pk
            thing.attribute_01
            thing.attribute_02
        
        ```
    * The output:
        ```
        >>> for thing in all_the_things:
        ...     thing.pk
        ...     thing.attribute_01
        ...     thing.attribute_02
        ... 
        1
        'Attribute 01 stuff!'
        'Attribute 02 stuff?'
        2
        'Something?'
        'Something Else!'
        3
        'String less than 20'
        'String much much much much much greater than 20'
        >>>
        ```

1. Get one object, which has `id=1` from the database:
    * `t = TheThing.objects.filter(id=1)`
    * `t`
        ```
        >>> t = TheThing.objects.filter(id=1)
        >>> t
        <QuerySet [<TheThing: Attribute 01 stuff! : Attribute 02 stuff?>]>
        >>>
        >>>
        ```
