from flask import Flask, render_template, request
import subprocess
import time
import os
import pyautogui

app = Flask(__name__)

def setup_xvfb():
    # Start Xvfb with a virtual display
    xvfb_process = subprocess.Popen(["Xvfb", ":99", "-screen", "0", "1024x768x24"])
    time.sleep(2)  # Wait for Xvfb to start
    os.environ["DISPLAY"] = ":99"  # Set DISPLAY environment variable

def login_to_remote_desktop(username, password, server_address):
    # Open Remote Desktop Connection
    subprocess.Popen("mstsc")
    time.sleep(2)  # Wait for the Remote Desktop Connection window to open

    rdc_window = pyautogui.getWindowsWithTitle("Remote Desktop Connection")[0]
    rdc_window.activate()

    # Type the server address and press Enter
    pyautogui.write(server_address)
    pyautogui.press("enter")
    time.sleep(2)

    # Type the username and press Tab
    pyautogui.write(username)
    pyautogui.press("tab")
    time.sleep(1)

    # Type the password and press Enter
    pyautogui.write(password)
    pyautogui.press("enter")
    time.sleep(10)  # Wait for the remote desktop to load

    # Once logged in, open PowerShell in administration mode
    pyautogui.hotkey("ctrl", "shift", "enter")
    time.sleep(2)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        server_address = request.form["server_address"]

        setup_xvfb()  # Start Xvfb and set DISPLAY environment variable
        login_to_remote_desktop(username, password, server_address)
        return "Commands executed successfully on remote servers!"
    return render_template("home.html")

if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    app.run(debug=True)
