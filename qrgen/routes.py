from flask import Flask, render_template, send_file, request, after_this_request
from qrgen import app
from qrgen.generator import Generator
from qrgen.folder_zipper import FolderZipper
import time
import os
import shutil
from threading import Timer
from qrgen.forms import GenerateForm

@app.route("/")
def index():
    form = GenerateForm()
    return render_template("index.html", form=form)


@app.route("/generate", methods=['GET', 'POST'])
def generate():
    form = GenerateForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        gen = Generator(
            form.fragment_size.data,
            form.fragment_count.data,
            form.common_name.data,
            form.delimeter.data,
            form.start_index.data,
            form.end_index.data)
        folder_name = str(time.time())
        gen.generate_to(folder_name)
        zip_name = request.form.get('common_name')
        z = FolderZipper.folder_to_zip(
            os.path.join('temporary_marks', folder_name),
            os.path.join('temporary_marks', folder_name))
        f = open(z, 'r')

        @after_this_request
        def remove_zip(response):
            print('Trying to delete')
            print(response)

            def rem():
                try:
                    shutil.rmtree(os.path.join('temporary_marks', folder_name))
                    os.remove(z)
                except Exception as rem_exp:
                    return str(rem_exp)

            t = Timer(5.0, rem)
            t.start()
            return response

        print('Returning file')
        try:
            return send_file(z, as_attachment=True, attachment_filename=(zip_name + '.zip'))
        except Exception as e:
            return str(e)

    return render_template("index.html", form=form)


