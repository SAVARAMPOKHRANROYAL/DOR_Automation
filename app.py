from flask import Flask, render_template, request
import subprocess
import time
import os
os.environ['DISPLAY'] = ':0'
os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'
import pyautogui

app = Flask(__name__)

#def login_to_remote_desktop(username, password, server_address, server_addresses):
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

    #for server_address in server_addresses:
        # Run the PowerShell command
    #    pyautogui.write("tnc {} -port port_number".format(server_address))
    #    pyautogui.press("enter")
    #    time.sleep(5)  # Wait for the command to execute

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        server_address = request.form["server_address"]
        #server_addresses = request.form.getlist("server_addresses")

        #login_to_remote_desktop(username, password, server_address, server_addresses)
        login_to_remote_desktop(username, password, server_address)
        return "Commands executed successfully on remote servers!"
    return render_template("home.html")

if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    app.run(debug=True)
