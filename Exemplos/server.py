import os

import ReconhecimentoFacial
import json
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
from werkzeug import secure_filename

app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'media/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def index():
    return """<html><body>
        Olá mundo.
        </body></html>"""


# Route that will process the file upload
@app.route('/entrada/reconhecer', methods=['POST'])
def entradaReconhecer():
    content = request.get_json(silent=True)

    j = json.loads(jsonify(content))

    print(content)
    return jsonify(content)

if __name__ == '__main__':
    app.run(
        debug=True
    )
