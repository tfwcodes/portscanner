import socket
import threading
from queue import Queue

print(
"""
                  _                                       
 _ __   ___  _ __| |_ ___  ___ __ _ _ __  _ __   ___ _ __ 
| '_ \ / _ \| '__| __/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|
| |_) | (_) | |  | |_\__ \ (_| (_| | | | | | | |  __/ |   ~>Portscanner app build in python<~
| .__/ \___/|_|   \__|___/\___\__,_|_| |_|_| |_|\___|_|   ~~>Made by tfwcodes(github)<~~
|_|                                                       



""")

while True:
    try:
        print("[!] Enter start_scan to start the portscanner" + "\n" + "[!] Enter scan_info to see how to start the scan" + "\n" + "[!] Enter Ctrl+C to exit the program")
        command = input("[+] Enter a command: ")
        if command == "start_scan":
            try:
                ip = input("Enter the ip/website you want to scan: ")
                number_of_threads = input("Enter the number of threads: ")

                print_lock = threading.Lock()


                def pscan(port):
                    try:
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        con = sock.connect((ip, port))
                        with print_lock:
                            print("Port", port, "is open")
                        con.close()
                    except:
                        pass


                def threader():
                    while True:
                        worker = q.get()
                        pscan(worker)
                        q.task_done()

                q = Queue()

                for x in range(int(number_of_threads)):
                    t = threading.Thread(target=threader)
                    t.daemon = True
                    t.start()

                for worker in range(1, 16000):
                    q.put(worker)

                q.join()
            except KeyboardInterrupt:
                exit()
        if command == "scan_info":
            try:
                print("If you want to scan a website ex [http://www.example.com/] you need to enter only example.com not the whole name")
            except KeyboardInterrupt:
                exit()
    except KeyboardInterrupt:
        exit()
