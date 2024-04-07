import os
import time
import shutil
import sqlite3
import urllib.request
import scratchattach as scratch3
from flask import Flask, render_template
#from backend_functions import get_profile_information

#Lines 1-5 import the esential libraries needed to make this project work :)

start = time.time()
print("Updating all libraries before starting.")
os.system("pip install -U scratchattach") 
os.system("pip install -U sqlite3")

#Lines 9-12 check to make sure all libraries are updated before running any code using them

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

#Will add table creation later
#conn.commit

cursor.close()
conn.close()

end = time.time()
elapsed = end-start
print(f"Starting server! Time taken to run checks: {elapsed} seconds\n")
app = Flask('app', template_folder='site')

@app.route('/')
def main_page():
    return render_template('main.html')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
