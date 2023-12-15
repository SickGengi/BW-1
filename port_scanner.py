import socket
import ipaddress

def port_scanner(ip_target, start_port, end_port):
    open_ports = []
    closed_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip_target, port))
        if result == 0:
            print(f"\nLa porta {port} è aperta\n")
            open_ports.append(port)
        else:
            print(f"La porta {port} è chiusa\n")
            closed_ports.append(port)
        sock.close()

    return open_ports, closed_ports

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def get_input():
    while True:
        ip_target = input("\nInserire l'indirizzo IP target: ")
        if validate_ip(ip_target):
            break
        else:
            print("Indirizzo IP non valido... Riprova...")

    while True:
        try:
            start_port = int(input("Inserire la prima porta: "))
            end_port = int(input("Inserire l'ultima porta: "))
            if start_port > 0 and end_port > 0 and start_port <= end_port:
                break
            else:
                print("Inserire un intervallo di porte valido...\n")
        except ValueError:
            print("Inserire numeri validi per le porte...\n")

    return ip_target, start_port, end_port

def main():
    while True:
        print("\n1. Avvia scansione delle porte")
        print("2. Esci")
        scelta = input("\nInserisci la tua scelta: ")

        if scelta == "1":
            ip_target, start_port, end_port = get_input()
            open_ports, closed_ports = port_scanner(ip_target, start_port, end_port)
            print("\nPorte aperte:", open_ports)
            print("Porte chiuse:", closed_ports)
        elif scelta == "2":
            print("Uscita dal programma...")
            break
        else:
            print("Scelta non valida. Riprova.")

        while True:
            nuova_scansione = input("\nVuoi eseguire un'altra scansione? (s/n): ").lower()
            if nuova_scansione == 's' or nuova_scansione == 'n':
                break
            else:
                print("Inserire 's' per sì o 'n' per no.")

        if nuova_scansione == 'n':
            print("Uscita dal programma...")
            break

if __name__ == "__main__":
    main()
