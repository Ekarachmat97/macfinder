import uuid

def get_mac_address(essid):
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    formatted_mac = ':'.join([mac[i:i+2] for i in range(0, 12, 2)])
    return formatted_mac

if __name__ == "__main__":
    essid = input("Silakan isi ESSID: ")
    mac_address = get_mac_address(essid)
    if mac_address:
        print(f"MAC Address untuk ESSID '{essid}': {mac_address}")
    else:
        print(f"MAC Address untuk ESSID '{essid}' tidak ditemukan.")