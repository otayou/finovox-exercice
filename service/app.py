from flask import Flask, render_template, jsonify, send_from_directory, abort
from service import config, status
import os

app = Flask(__name__)
app.config.from_object(config)

######################################################################
# H E A L T H   C H E C K
######################################################################
@app.route("/health")
def healthcheck():
    """Let them know our heart is still beating"""
    return jsonify(status=200, message="OK"), status.HTTP_200_OK

######################################################################
# H O M E   P A G E
######################################################################
@app.route("/")
def index():
    """Base URL for our service"""
    return render_template("index.html")

######################################################################
# LIST ALL FILES
######################################################################
@app.route("/api/files")
def list():
    folder_path = app.config["FOLDER_PATH"]
    all_items = os.listdir(folder_path)
    files = [f for f in all_items if os.path.isfile(os.path.join(folder_path, f))]
    return jsonify(files=files), status.HTTP_200_OK

######################################################################
# DOWNLOAD FILES
######################################################################
@app.route("/download/<string:filename>")
def download_file(filename):
    folder_path = app.config["FOLDER_PATH"]
    full_path = os.path.join(folder_path, filename)
    
    if not os.path.isfile(full_path):
        abort(status.HTTP_404_NOT_FOUND, "File not found.")
    
    return send_from_directory(folder_path, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=False)