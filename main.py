from scapy.arch import get_if_addr
from scapy.config import conf
from collections import Counter
from scapy.layers.inet import IP, TCP, ICMP, UDP
import pandas as pd
from scapy.sendrecv import send, sendp, sr, srloop, sr1, sniff

packetCounts = Counter()
packet_data = pd.DataFrame({
    'Packet': pd.array(["0"]),
    'Source address': pd.array(['none']),
    'Destination address': pd.array(['none']),
})


def ping(my_adresse:str, adresse: str, message:str = "This is a seizure!", counter:int = 10) -> None:

    # creating package for IP
    ip = IP(src=my_adresse, dst=adresse)
    packet = (ip / ICMP()/message)

    # a loop of packets
    send(packet, count=counter)


def get_my_adresse() -> str:

    #getting adresse to variable and return
    ip = get_if_addr(conf.iface)
    return ip

def port_scan() -> None:

    ans=sr(IP(dst="83.10.56.219")/UDP(dport=(1,1024)))
    ans.nsummary()

def customAction(packet: str)->None:
    """
    The function creates the tuple and adds data to data frame called packet_data
    """
    key = tuple(sorted([packet[0][1].src, packet[0][1].dst]))
    packetCounts.update([key])
    packet_data.loc[sum(packetCounts.values())] = [sum(packetCounts.values())] + [packet[0][1].src] + [packet[0][1].dst]


def capturePacket(protocol: str, counter:int=5)->None:
    """
    The function captures 10 recent IP packets and put source and destination addresses into pandas DataFrame
    """
    # Setup sniff
    x = sniff(prn=customAction, filter=protocol, count=counter)
    packet_data_updated = packet_data.drop(0)
    print(packet_data_updated.to_string(index=False))
    # Print out packet count per A <--> Z address pair
    print("\n".join(f"{f'{key[0]} <--> {key[1]}'}: sent {count} times" for key, count in packetCounts.items()))

n = 1

while n != 0:
    print("""╔╗ ┌─┐┌┬┐┌┬┐┌─┐┬─┐  ┬ ┬┬┬─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┬┌─
╠╩╗├┤  │  │ ├┤ ├┬┘  ││││├┬┘├┤ └─┐├─┤├─┤├┬┘├┴┐
╚═╝└─┘ ┴  ┴ └─┘┴└─  └┴┘┴┴└─└─┘└─┘┴ ┴┴ ┴┴└─┴ ┴""")
    print("What do you want to do? \nFor send packet enter: 1 \nFor scan enter: 2")
    n = int(input("Choice: "))
    if n == 1:
        adresse = str(input("Enter the victim's address: "))
        message = str(input("Write a message! "))
        counter = int(input("How much? "))
        ping(get_my_adresse(), adresse, message, counter)
    elif n == 2:
        protocol = str(input("Enter the protocol name: "))
        counter = int(input("How much? "))
        capturePacket(protocol, counter)
    else:
        break



