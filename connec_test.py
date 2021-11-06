# File: connec_test.py
# Author: r0paire
# Repo: https://www.github.com/r0paire/ConnecTest
# Date: 02/11/2021
# Last Updated: 06/11/2021 [Rev 1.0]
# Info: Website connectivity Tester in Python
# Tested on: Ubuntu 21.10 (GNU/Linux) & Windows 10
# Python: 3.9

# Imports 1/2
import subprocess

# Install missing packages
def _install_missing():
    subprocess.call(['python3', '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.call(['python3', '-m', 'pip', 'install', '--upgrade', 'pillow'])
_install_missing()

# Imports 2/2
import platform
import urllib.request
import socket
import tkinter
from tkinter import Button, IntVar, Label, Radiobutton, Text, Tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

# Configuration
app = Tk()
app.title("ConnecTest")
app.iconphoto(False, tkinter.PhotoImage(file="images/connec_test.png"))
app.configure(bg="#464542")
app.geometry("1000x800")
app.resizable(False, False)

# Fonts
header_Font = tkFont.Font(family="Ubuntu", size=12, weight='bold', slant='italic')
title_font = tkFont.Font(family='Ubuntu', size=20, weight='bold', slant='italic')
label_font = tkFont.Font(family='Ubuntu', size=11,)
txt_font = tkFont.Font(family='Ubuntu', size=14)
btn_font = tkFont.Font(family='Ubuntu', size=12)

# Variables
bad_website = "Please enter a valid website."

# Title Labels
title_1 = Label(app, text="Connec", font=title_font, fg="#d0d0d0", bg="#464542")
title_1.place(x=440, y=20)
title_2 = Label(app, text="Test", font=title_font, fg="#00ff00", bg="#464542")
title_2.place(x=535, y=20)

# Website Input
website_input_label = Label(app, text="Website:", font=label_font, fg="white", bg="#464542")
website_input_label.place(x=230, y=110)
website_format = Label(app, text="Format:   www.google.com", fg="red", font=label_font, bg="#464542")
website_format.place(x=230, y=185)
website_input = Text(app, font=txt_font, fg="black", bg="white", height=2, width=50)
website_input.place(x=230, y=130)

# Results Box
response_label = Label(app, text="Response:", font=label_font, fg="white", bg="#464542")
response_label.place(x=230,y=300)
response_out = Text(app, font=txt_font, fg="black", bg="white", height=10, width=50)
response_out.bind("<Button-1>", lambda e: "break")
response_out.bind("<Key>", lambda e: "break")
response_out.place(x=230,y=320)

# misc labels
authorLabel = Label(app, text="r0paire © 2021", font=('Ubuntu', '8', 'bold italic'), fg="yellow", bg="#464542")
authorLabel.place(x=920, y=785)

# Icon
pre_img = Image.open("images/connec_test.png")
resized_img = pre_img.resize((50,50))
icon = ImageTk.PhotoImage(resized_img)
icon_label = Label(image=icon, bg="#464542")
icon_label.place(x=594,y=5)

# loop for app
loop = tkinter.IntVar()

# Radio buttons
r = IntVar(0)

# Function to test connectivity
def _connect():
    # Ping
    # Uses ICMP or Ping to test if a host is reachable (Windows, Linux and Mac).
    if r.get() == 1:
        website = website_input.get("1.0", "end-1c")

        if website != '':
            # Platform filter
            param = '-n' if platform.system().lower()=='windows' else '-c'

            ping_cmd = ['ping', param, '1', website]
            ping_out = subprocess.call(ping_cmd)

            if ping_out == 0:
                response_out.delete(1.0, "end")
                response_out.insert('1.0', website +" is up and working! \n [PING]")
            else:
                response_out.delete(1.0, "end")
                response_out.insert('1.0', "Error connecting to " +website +" \n [PING]")
        elif website == '' or None:
            response_out.delete(1.0, "end")
            response_out.insert(1.0, bad_website)

    # HTTP
    # Uses HTTP to test if a website is up and working
    elif r.get() == 2:

        website = website_input.get("1.0", "end-1c")
        http_response= urllib.request.urlopen("https://" +website).getcode()

        if http_response == 200:                   # Code 200 = Success
            response_out.delete(1.0, "end")
            response_out.insert(1.0, website +" is up and working! \n [HTTP]")
        elif website == '' or None:                # Reject empty or null
            response_out.delete(1.0, "end")
            response_out.insert('1.0', bad_website)
        else:
            response_out.delete(1.0, "end")         # Error
            response_out.insert(1.0, website +" is not working! \n [HTTP]")
        
    # TCP
    # Uses powershell Test-NetConnection (Windows) or telnet (Linux/Mac) with TCP on port 80 (typical TCP port) to check if website can be connected to - or up.
    elif r.get() == 3:

        website = website_input.get(1.0, "end-1c")

        # Platform filter
        # Windows
        if platform.system().lower()=='windows':
            tcp_cmd = ["powershell.exe ", "Test-NetConnection ", "-ComputerName ", website, "-Port 80"]
            tcp_out = subprocess.run(tcp_cmd, shell=True, universal_newlines = True, stdout = subprocess.PIPE)
            tcp_filtered_out = tcp_out.stdout.splitlines()

            if "TcpTestSucceeded : True" in tcp_filtered_out:      # Success
                response_out.delete(1.0, "end")
                response_out.insert(1.0, website +" is up and working! \n [TCP Port 80]")
            elif website == '' or None:                            # Reject empty or null website field
                response_out.delete(1.0, "end")
                response_out.insert('1.0', bad_website)
            else:                                                  # Error
                response_out.delete(1.0, "end")
                response_out.insert(1.0, website +" is not reachable! \n [TCP Port 80]")

        # Linux and Mac OSX
        else:                                               # Linux and Mac OSX
            tcp_cmd = ["echo -e '\x1dclose\x0d' | telnet " +website +" 53"]
            tcp_out = subprocess.run(tcp_cmd, shell=True, stdout=subprocess.PIPE)
            tcp_out = str(tcp_out)
            
            if ("Connected to" in tcp_out):                 # Success if 'Connected to' found
                response_out.delete(1.0, "end")
                response_out.insert(1.0, website +" is up and working! \n [TCP Port 80]")
            elif website == '' or None :                    # Reject empty or null website
                response_out.delete(1.0, "end")
                response_out.insert('1.0', bad_website)
            else:                                           # Error
                response_out.delete(1.0, "end")
                response_out.insert(1.0, website +" is not reachable! \n [TCP Port 80]")

    # UDP
    # Uses a socket connection (Windows) and netcat (Linux/Mac) in UDP-mode on port 53 (common DNS port) to test if a host is up.
    elif r.get() == 4:

        website = website_input.get(1.0, "end-1c")

        # Platform filter
        # Windows
        if platform.system().lower()=='windows':

            if website != '' or None:                   # If website is not null, do test
                udp_socket = socket.socket(socket.SOCK_DGRAM)
                port = 53
                try:
                    udp_socket.connect((website, port))
                    response_out.delete(1.0, "end")
                    response_out.insert(1.0, website +" is up and working! \n [UDP Port 53]") # Success
                except Exception as e: 
                    response_out.delete(1.0, "end")
                    response_out.insert(1.0, website +" is not reachable! \n [UDP Port 53]")  # Error
                finally:
                    udp_socket.close()
            else:                                           # Reject empty or null
                response_out.delete(1.0, "end")
                response_out.insert('1.0', bad_website)

        # Linux and Mac OSX
        else:
            udp_cmd = ["nc -u -zv " +website +" 53 2>&1 | grep succeeded"]
            udp_out = subprocess.run(udp_cmd, shell=True)
            udp_out = str(udp_out)

            if ("succeeded" in udp_out):                  # Success if 'succeeded' found
                response_out.delete(1.0, "end")
                response_out.insert(1.0, website +" is up and working! \n [UDP Port 53]")
            elif website == '' or None:                   # Reject empty or null
                response_out.delete(1.0, "end")
                response_out.insert('1.0', bad_website)
            else:
                response_out.delete(1.0, "end")            # Error
                response_out.insert(1.0, website +" is not reachable! \n [UDP Port 53]")


# Function to clear I/O
def _clear():
    website_input.delete(1.0, "end")
    response_out.delete(1.0, "end")

# Function to display warning to wait for a response
def _wait_warn():
    if r.get() == 1:
        response_out.delete(1.0, "end")
        response_out.insert(1.0, " ")  # Wait not necessary for pings
    elif r.get() == 2:
        response_out.delete(1.0, "end")
        response_out.insert(1.0, "Please wait a few seconds for a response when testing. \n [HTTP]")
    elif r.get() == 3:
        response_out.delete(1.0, "end")
        response_out.insert(1.0, "Please wait a few seconds for a response when testing. \n [TCP Port 80]")
    elif r.get() == 4:
        response_out.delete(1.0, "end")
        response_out.insert(1.0, "Please wait a few seconds for a response when testing. \n [UDP Port 53]")

# Buttons
# Test Button
test_btn = Button(app, text="Test", font=btn_font, command=_connect, height=3, width=25, fg="white", bg="#2c552c")
test_btn.place(x=150,y=700)
# Clear Button
clear_btn = Button(app, text="Clear", font=btn_font, command=_clear, height=3, width=25, fg="black", bg="white")
clear_btn.place(x=580,y=700)

# Radio Buttons
# Ping Button
ping_btn = Radiobutton(app, text="Ping", font=btn_font, command=_wait_warn, fg="white", bg="red", height=3, selectcolor="red", width=20, variable=r, value=1)
ping_btn.place(x=45,y=570)
# HTTP Button
http_btn = Radiobutton(app, text="HTTP", font=btn_font, command=_wait_warn, fg="white", bg="#1f1e1e", selectcolor="black", height=3, width=20, variable=r, value=2)
http_btn.place(x=280,y=570)
# TCP Button
tcp_btn = Radiobutton(app, text="TCP", font=btn_font, command=_wait_warn, fg="red", bg="#e6ad00", selectcolor="#e6ad00", height=3, width=20, variable=r, value=3)
tcp_btn.place(x=510,y=570)
# UDP Button
udp_btn = Radiobutton(app, text="UDP", font=btn_font, command=_wait_warn, fg="#e6ad00", bg="#13588d", selectcolor="#13588d", height=3, width=20, variable=r, value=4)
udp_btn.place(x=740,y=570)

app.mainloop()
