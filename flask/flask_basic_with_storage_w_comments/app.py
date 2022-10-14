from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# A list object to store the user-input value from `POST` request
# and save it to be provided with the redirected `GET` request:
STORAGE_LIST_OBJECT = []

# An integer index for the storage position of the user-input value:
STORAGE_INDEX = 0


@app.route('/', methods=["GET", "POST"])
def index():
    # If `POST` request:
    if request.method == 'POST':

        # Clear `STORAGE_LIST_OBJECT` if not empty:
        if STORAGE_LIST_OBJECT:
            STORAGE_LIST_OBJECT.pop(STORAGE_INDEX)

        # Get 'the_text' value from the request form  and save as
        # `the_text_from_the_html_form`:
        the_text_from_the_html_form = request.form['the_text']

        # Add the value of `the_text_from_the_html_form` to
        # `STORAGE_LIST_OBJECT` at the zeroth index so we can send it
        # to template in `GET` request:
        STORAGE_LIST_OBJECT.insert(
            STORAGE_INDEX,
            the_text_from_the_html_form
        )

        # Redirect to server root to prevent double submit of form:
        return redirect('/')

    # Else a `GET` request:
    # Render the template with the stored value in `STORAGE_LIST_OBJECT`
    # from the `POST` request:
    return render_template(
        'index.html',
        template_variable=STORAGE_LIST_OBJECT
    )


app.run(debug=True)
