from flask import Flask, render_template, send_file, request, after_this_request


app = Flask(__name__)
app.config['CSRF_ENABLED'] = True
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

from qrgen import routes
