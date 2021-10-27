from scapy.layers.inet import ICMP, IP
from scapy.all import *
from collections import Counter
import pandas as pd


def pingAddress(ip: str)->None:
    """
    The function pings any address provided by the user via scapy IP/ICMP packet
    ---------------------------------------------------------------------------
    pingAddress(IP_address)
    """
    ip = IP(dst=ip)
    packet = ip / ICMP()
    srloop(packet, count=4)

while(True):
    print("Enter the IP address or q to end")
    ip = input()
    if(ip=='q'):
        break
    pingAddress(ip)



# Create a Packet Counter
packetCounts = Counter()

packet_data = pd.DataFrame({
    'Packet': pd.array(["0"]),
    'Source address': pd.array(['none']),
    'Destination address': pd.array(['none'])
})


def customAction(packet: str)->None:
    """
    The function creates the tuple and adds data to data frame called packet_data
    """
    key = tuple(sorted([packet[0][1].src, packet[0][1].dst]))
    packetCounts.update([key])
    packet_data.loc[sum(packetCounts.values())] = [sum(packetCounts.values())] + [packet[0][1].src] + [packet[0][1].dst]


def capturePacket()->None:
    """
    The function captures 10 recent IP packets and put source and destination addresses into pandas DataFrame
    """
    # Setup sniff, filtering for IP traffic
    x = sniff(filter="ip", prn=customAction, count=10)
    x.summary()
    packet_data_updated = packet_data.drop(0)
    print(packet_data_updated.to_string(index=False))
    # Print out packet count per A <--> Z address pair
    print("\n".join(f"{f'{key[0]} <--> {key[1]}'}: sent {count} times" for key, count in packetCounts.items()))


capturePacket()
