from re import S
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


STORAGE_LIST_OBJECT = []
STORAGE_INDEX = 0


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if STORAGE_LIST_OBJECT:
            STORAGE_LIST_OBJECT.pop(STORAGE_INDEX)
        the_text_from_the_html_form = request.form['the_text']
        STORAGE_LIST_OBJECT.insert(
            STORAGE_INDEX,
            the_text_from_the_html_form
        )
        return redirect('/')

    value_to_send_to_template = STORAGE_LIST_OBJECT[STORAGE_INDEX]
    return render_template(
        'index.html',
        template_variable=value_to_send_to_template
    )


app.run(debug=True)