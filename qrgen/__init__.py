from flask import Flask, render_template, send_file, request, after_this_request


app = Flask(__name__)


from qrgen import routes
