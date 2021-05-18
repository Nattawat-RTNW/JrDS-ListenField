from app import app
from flask import Flask, send_file, render_template,request
import ee
import folium
import numpy as np
import pandas as pd
import proplot as plot
import matplotlib.pyplot as plt
import datetime
from pandas.plotting import register_matplotlib_converters

service_account = 'nattawat@geeproject-313808.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'key.json')
ee.Initialize(credentials)

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('input.html')

@app.route('/download_img')
def link_download_files():
	
	True_color = 'True_color.zip'

	return send_file(True_color, as_attachment=True)

	
if __name__ == "__main__":
    app.run(debug=True)