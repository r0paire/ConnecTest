# File: connec_test.py
# Author: r0paire
# Repo: https://www.github.com/r0paire/ConnecTest
# Date: 17/12/2023
# Last Updated: 17/12/2023 [Rev 2.0]
# Info: Website connectivity Tester in Python
# Tested on: Windows 11
# Python: 3.9.13

# Install missing modules if not present
#Imports
import platform
import subprocess
import socket
import tkinter
from tkinter import Button, Label, messagebox, Text, Toplevel, Tk
import tkinter.font as tkFont
#from PIL import Image, ImageTk #Buggy hopefully working in future
import requests
import re


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
btn_font = tkFont.Font(family='Ubuntu', weight='bold', size=10)

# Title Labels
title_1 = Label(app, text="Connec", font=title_font, fg="#d0d0d0", bg="#464542")
title_1.place(x=440, y=20)
title_2 = Label(app, text="Test", font=title_font, fg="#00ff00", bg="#464542")
title_2.place(x=535, y=20)


# misc labels
authorLabel = Label(app, text="r0paire  2023", font=('Ubuntu', '8', 'bold italic'), fg="yellow", bg="#464542")
authorLabel.place(x=920, y=785)

# Icon
# pre_img = Image.open("images/connec_test.png")
# resized_img = pre_img.resize((50,50))
# icon = ImageTk.PhotoImage(resized_img)
# icon_label = Label(image=icon, bg="#464542")
# icon_label.place(x=594,y=5)

# loop for app
loop = tkinter.IntVar()

# Functions to test connectivity

# PING TEST - NEW WINDOW VERSION
def openPingwindow():
    app.withdraw()
    openPingwindow = Toplevel(app)
    openPingwindow.title("Ping Test Window")
    openPingwindow.geometry("1000x800")
    openPingwindow.configure(bg="#464542")
    openPingwindow.resizable(False, False)

    # Fonts
    title_font = tkFont.Font(family='Ubuntu', size=20, weight='bold', slant='italic')
    label_font = tkFont.Font(family='Ubuntu', size=11,)
    desc_font = tkFont.Font(family='Ubuntu', size=14)
    txt_font = tkFont.Font(family='Ubuntu', size=14)
    btn_font = tkFont.Font(family='Ubuntu', size=12)
    rtrnbtn_font = tkFont.Font(family='Ubuntu', size=20, weight='bold')

    # Title Labels
    title_1 = Label(openPingwindow, text="Connec", font=title_font, fg="#d0d0d0", bg="#464542")
    title_1.place(x=440, y=20)
    title_2 = Label(openPingwindow, text="Test", font=title_font, fg="#00ff00", bg="#464542")
    title_2.place(x=535, y=20)

    # Website Input
    website_input_label = Label(openPingwindow, text="Website/Address:", font=label_font, fg="white", bg="#464542")
    website_input_label.place(x=230, y=160)
    website_input = Text(openPingwindow, font=txt_font, fg="black", bg="white", height=2, width=50)
    website_input.place(x=230, y=180)

    website_format = Label(openPingwindow, text="Format:   www.google.com/192.168.1.1", fg="red", font=label_font, bg="#464542")
    website_format.place(x=230, y=230)

    # Ping description
    ping_descLabel = Label(openPingwindow, text="Internet Control Message Protocol (ICMP), also known as 'Ping', \n is a protocol for testing the availability of a network host on an network.", font=desc_font, fg="white", bg="#464542")
    ping_descLabel.place(x=230, y=85)

    # Results Box
    response_label = Label(openPingwindow, text="Response:", font=label_font, fg="white", bg="#464542")
    response_label.place(x=230,y=320)
    response_out = Text(openPingwindow, font=txt_font, fg="black", bg="white", height=10, width=50)
    response_out.bind("<Button-1>", lambda e: "break")
    response_out.bind("<Key>", lambda e: "break")
    response_out.place(x=230,y=340)

    # misc labels
    authorLabel = Label(openPingwindow, text="r0paire 2023", font=('Ubuntu', '8', 'bold italic'), fg="yellow", bg="#464542")
    authorLabel.place(x=920, y=785)

    # Button to return to main window
    def return2Menu():
        openPingwindow.destroy()
        app.deiconify()
    rtnBtn = Button(openPingwindow, text="↶", font=rtrnbtn_font, fg="white", bg="#464542", command=return2Menu, width=8, height=1)
    rtnBtn.place(x=30, y=40)

    # Button to clear input
    def _clear():
        website_input.delete(1.0, "end")
        response_out.delete(1.0, "end")

    def pingTest():
        website = website_input.get("1.0", "end-1c")

        if website != '':
            # Platform filter
            param = '-n' if platform.system().lower()=='windows' else '-c'

            ping_cmd = ['ping', param, '1', website]
            ping_out = subprocess.call(ping_cmd)

            if ping_out == 0:
                response_out.delete(1.0, "end")
                response_out.insert('1.0', website +" is up and working!")
            else:
                response_out.delete(1.0, "end")
                response_out.insert('1.0', "Error pinging " +website +"")
        elif website == '' or None:
            response_out.delete(1.0, "end")
            response_out.insert(1.0, "Please enter a valid domain or address.")

    # Buttons
    ping_testBtn = Button(openPingwindow, text="Ping", font=btn_font, fg="white", bg="#00ff00", command=pingTest)
    ping_testBtn.place(x=230, y=260)


# HTTP - NEW WINDOW VERSION
def openHTTPwindow():
    app.withdraw()
    openHTTPwindow = Toplevel(app)
    openHTTPwindow.title("HTTP/HTTPS Test Window")
    openHTTPwindow.geometry("1000x800")
    openHTTPwindow.configure(bg="#464542")
    openHTTPwindow.resizable(False, False)

    # Fonts
    title_font = tkFont.Font(family='Ubuntu', size=20, weight='bold', slant='italic')
    label_font = tkFont.Font(family='Ubuntu', size=11)
    desc_font = tkFont.Font(family='Ubuntu', size=13)
    txt_font = tkFont.Font(family='Ubuntu', size=14)
    btn_font = tkFont.Font(family='Ubuntu', size=12)
    rtrnbtn_font = tkFont.Font(family='Ubuntu', size=20, weight='bold')

    # Title Labels
    title_1 = Label(openHTTPwindow, text="Connec", font=title_font, fg="#d0d0d0", bg="#464542")
    title_1.place(x=440, y=20)
    title_2 = Label(openHTTPwindow, text="Test", font=title_font, fg="#00ff00", bg="#464542")
    title_2.place(x=535, y=20)

    # HTTP & HTTPS explanation label
    http_descriptionLabel = Label(openHTTPwindow, text="Hypertext Transfer Protocol (HTTP) is an IP protocol for distributed, collaborative, \n and hypermedia information systems.", font=desc_font, fg="lime", bg="#464542")
    http_descriptionLabel.place(x=220, y=120)

    https_descriptionLabel = Label(openHTTPwindow, text="Hypertext Transfer Protocol Secure (HTTPS) is an improvement on the HTTP Protocol \n that implements TLS (Transport Layer Security) amongst other additions to \n make browsing more secure.", font=desc_font, fg="gold", bg="#464542")
    https_descriptionLabel.place(x=220, y=160)

    # Website Input
    website_input_label = Label(openHTTPwindow, text="Website:", font=label_font, fg="white", bg="#464542")
    website_input_label.place(x=230, y=240)
    website_input = Text(openHTTPwindow, font=txt_font, fg="black", bg="white", height=2, width=50)
    website_input.place(x=230, y=260)

    website_format = Label(openHTTPwindow, text="Format:   www.google.com", fg="red", font=label_font, bg="#464542")
    website_format.place(x=230, y=310)

    # Results Box
    response_label = Label(openHTTPwindow, text="Response:", font=label_font, fg="white", bg="#464542")
    response_label.place(x=230,y=340)
    response_out = Text(openHTTPwindow, font=txt_font, fg="black", bg="white", height=10, width=50)
    response_out.bind("<Button-1>", lambda e: "break")
    response_out.bind("<Key>", lambda e: "break")
    response_out.place(x=230,y=360)

    # misc labels
    authorLabel = Label(openHTTPwindow, text="r0paire 2023", font=('Ubuntu', '8', 'bold italic'), fg="yellow", bg="#464542")
    authorLabel.place(x=920, y=785)

    # Button to return to main window
    def return2Menu():
        openHTTPwindow.destroy()
        app.deiconify()
    rtnBtn = Button(openHTTPwindow, text="↶", font=rtrnbtn_font, fg="white", bg="#464542", command=return2Menu, width=8, height=1)
    rtnBtn.place(x=30, y=40)

    https_result = False
    http_result = False

    # Button to clear input
    def _clear():
        website_input.delete(1.0, "end")
        response_out.delete(1.0, "end")

    # Test Button
    def testHTTP():
        website = website_input.get(1.0, "end-1c")
        HTTPS_URL = f'https://{website}'
        HTTP_URL = f'http://{website}'
        http_result = ""
        https_result = ""
        
        def checkProtocol(url):
            try:
                response = requests.head(url, allow_redirects=False)
                print(response.status_code)
                if response.status_code == 200:
                    if response.url.startswith("http://"):  # webpage is using HTTP
                        print(response.url)
                        http_result = "http"
                        return http_result
                    elif response.url.startswith("https://"):   # webpage is using HTTPS
                        print(response.url)
                        https_result = "https"
                        return https_result
                elif response.status_code == 301:   # webpage redirects to another
                        print(response.url)
                        print ("redirected")
                        https_result = "redirected"
                        return https_result
                elif response.status_code == 405:   # bugged, will get first response but then crash
                        print(response.url)
                        print ("rejected")
                        https_result = "rejected"
                        return https_result
                else:                               # misc reason for no connection or invalid website
                        print(response.url)
                        print ("failed")
                        return ''
            except requests.RequestException as e:
                return f"error occured: {e}"

        http_result = checkProtocol(HTTP_URL)
        https_result = checkProtocol(HTTPS_URL)

        #if https_result == 'https' and http_result == 'http':
        if https_result == "https" and http_result == "http":
            response_out.delete(1.0, "end")
            response_out.insert(1.0, website +" is reachable via HTTP and HTTPS")
            http_result == ''
            https_result == ''
        elif http_result == "http" and https_result != "https":
            response_out.delete(1.0, "end")
            response_out.insert(1.0, website +" is only reachable via HTTP, not HTTPS")
            http_result == ''
            https_result == ''
        elif https_result != "https" and http_result == "http":
            response_out.delete(1.0, "end")
            response_out.insert(1.0, website +" is only reachable via HTTPS, not HTTP")
            http_result == ''
            https_result == ''
        elif https_result == "https" and http_result == "redirected":
            response_out.delete(1.0, "end")
            response_out.insert(1.0, website +" is only reachable via HTTPS, not HTTP")
            http_result == ''
            https_result == ''
        elif https_result == "rejected" and http_result == "rejected":
            response_out.delete(1.0, "end")
            response_out.insert(1.0, "Test failed due to server rejecting connection")
            http_result == ''
            https_result == ''
        elif https_result == "redirected" and http_result == "redirected":
            response_out.delete(1.0, "end")
            response_out.insert(1.0, website +" is unreachable due to a redirect to another page or domain.")
            http_result == ''
            https_result == ''
        else:
            response_out.delete(1.0, "end")
            response_out.insert(1.0, website +" is unreachable using HTTP and HTTPS!")
            http_result == ''
            https_result == ''

    http_testBtn = Button(openHTTPwindow, text="Test", font=btn_font, command=testHTTP, height=3, width=25, fg="white", bg="#2c552c")
    http_testBtn.place(x=150,y=700)

    clear_btn = Button(openHTTPwindow, text="Clear", font=btn_font, command=_clear, height=3, width=25, fg="black", bg="white")
    clear_btn.place(x=580,y=700)


#TCP - NEW WINDOW VERSION
def openTCPwindow():
    app.withdraw()   
    openTCPwindow = Toplevel(app)
    openTCPwindow.title("TCP Test Window")
    openTCPwindow.geometry("1000x800")
    openTCPwindow.configure(bg="#464542")
    openTCPwindow.resizable(False, False)

    # Fonts
    title_font = tkFont.Font(family='Ubuntu', size=20, weight='bold', slant='italic')
    label_font = tkFont.Font(family='Ubuntu', size=11,)
    desc_font = tkFont.Font(family='Ubuntu', size=13,)
    txt_font = tkFont.Font(family='Ubuntu', size=14)
    btn_font = tkFont.Font(family='Ubuntu', size=12)
    rtrnbtn_font = tkFont.Font(family='Ubuntu', size=20, weight='bold')

    # Variables
    bad_address = "Please enter a valid address."

    # Title Labels
    title_1 = Label(openTCPwindow, text="Connec", font=title_font, fg="#d0d0d0", bg="#464542")
    title_1.place(x=440, y=20)
    title_2 = Label(openTCPwindow, text="Test", font=title_font, fg="#00ff00", bg="#464542")
    title_2.place(x=535, y=20)

    # Website Input
    website_input_label = Label(openTCPwindow, text="Website/Address:", font=label_font, fg="white", bg="#464542")
    website_input_label.place(x=230, y=180)
    website_input = Text(openTCPwindow, font=txt_font, fg="black", bg="white", height=2, width=50)
    website_input.place(x=230, y=200)


    website_format = Label(openTCPwindow, text="Format:   www.google.com or 123.456.789.012", fg="red", font=label_font, bg="#464542")
    website_format.place(x=230, y=255)

    # Port Input
    # Port Input validation
    def validate_port(event):
        user_input = port_input.get(1.0, "end-1c")  # Get the input from the text field
        try:
            # Attempt to convert the input to an integer
            value = int(user_input)
            if value > 0 and value < 65536:

                # If successful, create a variable with the integer value
                port = value

            else:
                # If the input is not an integer, display a messagebox
                messagebox.showerror("Error", "Please enter an integer between 1 and 65535 for Port number")
                # Clear the text field
                port_input.delete(1.0, "end")
        except ValueError:
            # If the input is not an integer, display a messagebox
            messagebox.showerror("Error", "Please enter an integer between 1 and 65535 for Port number")
            # Clear the text field
            port_input.delete(1.0, "end")

    port_input_label = Label(openTCPwindow, text="Port:", font=label_font, fg="white", bg="#464542")
    port_input_label.place(x=230, y=280)

    port_input = Text(openTCPwindow, font=txt_font, fg="black", bg="white", height=1, width=8)
    port_input.place(x=230, y=300)
    port_input.bind("<FocusOut>", validate_port)

    # TCP description 
    tcp_descLabel = Label(openTCPwindow, text="Transmission Control Protocol (TCP) is an IP procotol that provides reliable, ordered, \n and error-checked delivery of a stream of bytes across networks. TCP is often chosen over \n UDP due to reliability and stability when making connections or sending data.", font=desc_font, fg="white", bg="#464542")
    tcp_descLabel.place(x=230, y=100)

    # Results Box
    response_label = Label(openTCPwindow, text="Response:", font=label_font, fg="white", bg="#464542")
    response_label.place(x=230,y=350)
    response_out = Text(openTCPwindow, font=txt_font, fg="black", bg="white", height=10, width=50)
    response_out.bind("<Button-1>", lambda e: "break")
    response_out.bind("<Key>", lambda e: "break")
    response_out.place(x=230,y=370)

    # misc labels
    authorLabel = Label(openTCPwindow, text="r0paire 2023", font=('Ubuntu', '8', 'bold italic'), fg="yellow", bg="#464542")
    authorLabel.place(x=920, y=785)

    # Button to return to main window
    def return2Menu():
        openTCPwindow.destroy()
        app.deiconify()
    rtnBtn = Button(openTCPwindow, text="↶", font=rtrnbtn_font, fg="white", bg="#464542", command=return2Menu, width=8, height=1)
    rtnBtn.place(x=30, y=40)

    # Button to clear input
    def _clear():
        website_input.delete(1.0, "end")
        port_input.delete(1.0, "end")
        response_out.delete(1.0, "end")
    # Test Button
    def testTCP():
        website = website_input.get(1.0, "end-1c")
        port = port_input.get(1.0, "end-1c")

        # Platform filter
        # Windows
        if platform.system().lower()=='windows':
            tcp_cmd = ["powershell.exe ", "Test-NetConnection", "-ComputerName", website, "-Port", port]
            tcp_out = subprocess.run(tcp_cmd, shell=True, universal_newlines = True, stdout = subprocess.PIPE)
            tcp_filtered_out = tcp_out.stdout.splitlines()

            if "TcpTestSucceeded : True" in tcp_filtered_out:      # Success
                response_out.delete(1.0, "end")
                response_out.insert(1.0, website +" is up and working on port " +port +"!")
            elif website == '' or None:                            # Reject empty or null website field
                response_out.delete(1.0, "end")
                response_out.insert('1.0', bad_address)
            else:                                                  # Error
                response_out.delete(1.0, "end")
                response_out.insert(1.0, website +" is not reachable on port " +port +"!")

        # Linux and Mac OSX
        else:                                               # Linux and Mac OSX
            tcp_cmd = ["echo -e '\x1dclose\x0d' | telnet " +website +" 53"]
            tcp_out = subprocess.run(tcp_cmd, shell=True, stdout=subprocess.PIPE)
            tcp_out = str(tcp_out)
            
            if ("Connected to" in tcp_out):                 # Success if 'Connected to' found
                response_out.delete(1.0, "end")
                response_out.insert(1.0, website +" is up and working on port " +port +"!")
            elif website == '' or None :                    # Reject empty or null website
                response_out.delete(1.0, "end")
                response_out.insert('1.0', bad_address)
            else:                                           # Error
                response_out.delete(1.0, "end")
                response_out.insert(1.0, website +" is not reachable on port " +port +"!")
        
    tcp_testBtn = Button(openTCPwindow, text="Test", font=btn_font, command=testTCP, height=3, width=25, fg="white", bg="#2c552c")
    tcp_testBtn.place(x=150,y=700)


    clear_btn = Button(openTCPwindow, text="Clear", font=btn_font, command=_clear, height=3, width=25, fg="black", bg="white")
    clear_btn.place(x=580,y=700)


def openUDPwindow():
    app.withdraw()
    openUDPwindow = Toplevel(app)
    openUDPwindow.title("UDP Test Window")
    openUDPwindow.geometry("1000x800")
    openUDPwindow.configure(bg="#464542")
    openUDPwindow.resizable(False, False)
    

    # Fonts
    title_font = tkFont.Font(family='Ubuntu', size=20, weight='bold', slant='italic')
    label_font = tkFont.Font(family='Ubuntu', size=11,)
    warn_font = tkFont.Font(family='Ubuntu', size=11, weight='bold', slant='italic')
    desc_font = tkFont.Font(family='Ubuntu', size=13,)
    txt_font = tkFont.Font(family='Ubuntu', size=14)
    btn_font = tkFont.Font(family='Ubuntu', size=12)
    rtrnbtn_font = tkFont.Font(family='Ubuntu', size=20, weight='bold')

    # Variables
    port_in = ''

    #Labels
    # Title Labels
    title_1 = Label(openUDPwindow, text="Connec", font=title_font, fg="#d0d0d0", bg="#464542")
    title_1.place(x=440, y=20)
    title_2 = Label(openUDPwindow, text="Test", font=title_font, fg="#00ff00", bg="#464542")
    title_2.place(x=535, y=20)

    # Address Input Labels
    website_input_label = Label(openUDPwindow, text="Website/Address:", font=label_font, fg="white", bg="#464542")
    website_input_label.place(x=230, y=180)
    website_input = Text(openUDPwindow, font=txt_font, fg="black", bg="white", height=2, width=50)
    website_input.place(x=230, y=200)

    # Address Format Label
    website_format = Label(openUDPwindow, text="Format:   www.google.com or 192.168.0.1", fg="red", font=label_font, bg="#464542")
    website_format.place(x=230, y=255)

    # Port Labels

    # Port Input validation
    def validate_port(event):
        user_input = port_input.get(1.0, "end-1c")  # Get the input from the text field
        try:
            # Attempt to convert the input to an integer
            value = int(user_input)
            if value > 0 and value < 65536:

                # If successful, create a variable with the integer value
                port = value

            else:
                # If the input is not an integer, display a messagebox
                messagebox.showerror("Error", "Please enter an integer between 1 and 65535 for Port number")
                # Clear the text field
                port_input.delete(1.0, "end")
        except ValueError:
            # If the input is not an integer, display a messagebox
            messagebox.showerror("Error", "Please enter an integer between 1 and 65535 for Port number")
            # Clear the text field
            port_input.delete(1.0, "end")

    port_input_label = Label(openUDPwindow, text="Port:", font=label_font, fg="white", bg="#464542")
    port_input_label.place(x=230, y=280)
    port_input = Text(openUDPwindow, font=txt_font, fg="black", bg="white", height=1, width=8)
    port_input.place(x=230, y=300)
    port_input.bind("<FocusOut>", validate_port)

    # UDP Description
    udp_descLabel = Label(openUDPwindow, text="User Datagram Protocol (UDP) is a IP protocol of a connectionless nature used \n for lightweight traffic. UDP is far less reliable than TCP, with a higher chance of packet \n loss and no error-checking.", font=desc_font, fg="white", bg="#464542")
    udp_descLabel.place(x=230, y=100)

    # Results Box
    response_label = Label(openUDPwindow, text="Response:", font=label_font, fg="white", bg="#464542")
    response_label.place(x=230,y=360)
    response_out = Text(openUDPwindow, font=txt_font, fg="black", bg="white", height=10, width=50)
    response_out.bind("<Button-1>", lambda e: "break")
    response_out.bind("<Key>", lambda e: "break")
    response_out.place(x=230,y=380)

    # Warning Label
    udp_warn_label = Label(openUDPwindow, text="Warning: UDP isn't widely supported by hosts. \n Please make sure your target is intended to be reachable via UDP.", font=warn_font, fg="red", bg="#464542")
    udp_warn_label.place(x=270, y=620)

    # misc labels
    authorLabel = Label(openUDPwindow, text="r0paire 2023", font=('Ubuntu', '8', 'bold italic'), fg="yellow", bg="#464542")
    authorLabel.place(x=920, y=785)

    # Button to closed UDP window and return to main window
    def return2Menu():
        openUDPwindow.destroy()
        app.deiconify()
    rtnBtn = Button(openUDPwindow, text="↶", font=rtrnbtn_font, fg="white", bg="#464542", command=return2Menu, width=8, height=1)
    rtnBtn.place(x=30, y=40)

    # Button to clear input
    def _clear():
        website_input.delete(1.0, "end")
        response_out.delete(1.0, "end")
    
    def testUDP():
        website = website_input.get(1.0, "end-1c")
        ip_address = ''
        port_in = port_input.get(1.0, "end-1c")
        port = int(port_in)
        
        # Regular expression patterns for IPv4 and IPv6 addresses
        ipv4_pattern = r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
        ipv6_pattern = r"^(?:[A-F0-9]{1,4}:){7}[A-F0-9]{1,4}$"

        # Regular expression pattern for domain name
        domain_pattern = r"^([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.)+[a-zA-Z]{2,}$"

        if re.match(ipv4_pattern, website) or re.match(ipv6_pattern, website):
            ip_address = website
            try:
                udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                udp_socket.settimeout(10)  # 5 seconds timeout

                test_message = b"Test message"
                udp_socket.sendto(test_message, (ip_address, port))
                data, server = udp_socket.recvfrom(1024)

                print(f"Received data from {server}: {data.decode('utf-8')}")
                print("UDP connection successful!")
                response_out.delete(1.0, "end")
                port_num = str(port)
                response_out.insert(1.0, website +" is up and working on port " +port_num +"!")
                return
            except socket.error as e:
                print(f"Error: {e}")
                print("UDP connection failed.")
                response_out.delete(1.0, "end")
                port_num = str(port)
                response_out.insert(1.0, website +" is unreachable via UDP on port " +port_num +"!")
            finally:
            # Close the socket
                if udp_socket:
                    udp_socket.close()

        elif re.match(domain_pattern, website):
            ip_address = socket.gethostbyname(website)
            print("input is a website - traslating to " +ip_address)
            try:
                udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                udp_socket.settimeout(5)  # 5 seconds timeout

                test_message = b"Test message"
                udp_socket.sendto(test_message, (ip_address, port))
                data, server = udp_socket.recvfrom(1024)

                print(f"Received data from {server}: {data.decode('utf-8')}")
                print("UDP connection successful!")
                response_out.delete(1.0, "end")
                port_num = str(port)
                response_out.insert(1.0, website +" is up and working on port " +port_num +"!")
                udp_socket.close()
            except socket.error as e:
                print(f"Error: {e}")
                print("UDP connection failed.")
                response_out.delete(1.0, "end")
                port_num = str(port)
                response_out.insert(1.0, website +" is unreachable via UDP on port " +port_num +"! \n (Error: " +str(e) +")")
                udp_socket.close()
            finally:
                # Close the socket
                if udp_socket:
                    udp_socket.close()  
        else:
            return "Neither IP Address nor Domain"

        
    # Button to start test
    udp_testBtn = Button(openUDPwindow, text="Test", font=btn_font, command=testUDP, height=3, width=25, fg="white", bg="#2c552c")
    udp_testBtn.place(x=150,y=700)

    # Button to clear input and response fields
    clear_btn = Button(openUDPwindow, text="Clear", font=btn_font, command=_clear, height=3, width=25, fg="black", bg="white")
    clear_btn.place(x=580,y=700)

        
# Buttons
# Ping Window Button
pingBtn = Button(app, text ="Ping", command = openPingwindow, fg="white", bg="red", font=btn_font, height=3, width=25)
pingBtn.place(x=290, y=120)
pingBtn_label = Label(app, text="The Ping Test uses the ICMP protocol to test if a host \n is up and reachable.", font=label_font, fg="white", bg="#1f1e1e")
pingBtn_label.place(x=530, y=125)

# HTTP Window Button
httpBtn = Button(app, text ="HTTP", command = openHTTPwindow, fg="black", bg="white", font=btn_font, height=3, width=25)
httpBtn.place(x=290,y=270)
HttpBtn_label = Label(app, text="The HTTP Test uses both the HTTP and HTTPS protocols \n to test if a host  is up and reachable via \n traditional HTTP and more  secure HTTPS.", font=label_font, fg="white", bg="#1f1e1e")
HttpBtn_label.place(x=530, y=265)

 # TCP Window Button
tcpBtn = Button(app, text ="TCP", command = openTCPwindow, fg="red", bg="#e6ad00", font=btn_font, height=3, width=25)
tcpBtn.place(x=290,y=420)
tcpBtn_label = Label(app, text="The TCP Test uses the TCP procotol to test if a host \n is up and reachable.", font=label_font, fg="white", bg="#1f1e1e")
tcpBtn_label.place(x=530, y=425)

# UDP Window Button - TBD
udpBtn = Button(app, text ="UDP", command = openUDPwindow, fg="white", bg="blue", font=btn_font, height=3, width=25)
udpBtn.place(x=290,y=590)
udpBtn_label = Label(app, text="The UDP Test uses the UDP procotol to test if a host \n is up and reachable.", font=label_font, fg="white", bg="#1f1e1e")
udpBtn_label.place(x=530, y=580)
udp_warn_label = Label(app, text="WARNING: UDP support in this context is not widely \n supported for domains due to it's nature.", font=label_font, fg="red", bg="#1f1e1e")
udp_warn_label.place(x=530, y=625)

app.mainloop()
