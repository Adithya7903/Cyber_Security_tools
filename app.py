import socket
import subprocess
import ipaddress
import os
import struct

def run(*args):
    val = entryIp.value  # Assuming entryIp is defined elsewhere
    print(val)

def main():
    try:
        while True:
            print("""\n
-----------------------------HACKING TOOLS-----------------------------------
||                                                                         ||
||                           1.Port Scanner                                ||
||                           2.Ip Scanner                                  ||
||                           3.Send Ping                                   ||
||                           4.Nmap Scanner                                ||
||                           5.MSFConsole                                   ||
||                                                                         ||
-----------------------------------------------------------------------------""")
            print("Please Choose a Tool (1-5) :")
            chosen = input()

            if chosen == "1":
                portScanner()
            elif chosen == "2":
                ipScanner()
            elif chosen == "3":
                sendPing()
            elif chosen == "4":
                nmapScanner()
            elif chosen == "5":
                msfConsole()
            else:
                print("Wrong Choice. Try Again")

    except KeyboardInterrupt:
        sys.exit()

def portScanner():
    try:
        remoteServer = input("Enter a host to scan: ")
        remoteServerIP = socket.gethostbyname(remoteServer)

        print("-" * 60)
        print("Scanning...", remoteServerIP)
        print("-" * 60)

        for port in (20, 21, 22, 80, 443):
            print("port {} scanning ".format(port))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                info = socket.getservbyport(port)
                print("Port {}. Open -- {}".format(port, info))
            sock.close()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        return

    except socket.error:
        print("Couldn't connect to the server")
        return

    print('Scanning Completed.')
    return

def ipScanner():
    net_addr = input("Enter a network address in CIDR format(ex.192.168.1.0/24): ")
    ip_net = ipaddress.ip_network(net_addr)
    all_hosts = list(ip_net.hosts())

    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE

    for i in range(len(all_hosts)):
        output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(all_hosts[i])], stdout=subprocess.PIPE,
                                  startupinfo=info).communicate()[0]

        if "Destination host unreachable" in output.decode('utf-8'):
            print(str(all_hosts[i]), "is Offline")
        elif "Request timed out" in output.decode('utf-8'):
            print(str(all_hosts[i]), "is Offline")
        else:
            print(str(all_hosts[i]), "is Online")
    return

def sendPing():
    ipaddr = input("Enter IP address or hostname : ")
    command = "ping {}".format(ipaddr)
    print(os.system(command))

def nmapScanner():
    target_ip = input("Enter the target IP address for Nmap scan: ")
    command = f'nmap {target_ip}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Print the Nmap scan results
    print(result.stdout)

    # Check for errors in the command execution
    if result.returncode != 0:
        print(f"Error: {result.stderr}")

def msfConsole():
    # Run the msfconsole
    subprocess.run(['msfconsole'])

if __name__ == "__main__":
    main()