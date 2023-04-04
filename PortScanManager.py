#!/usr/bin/python
# -*- coding: utf-8 -*-

# @LICENSE: This code is under MIT License.
# @AUTHOR: AlirızaGövce

import socket

def scan_ports(ip_address):
    print("Scanning ports on {}".format(ip_address))
    open_ports = []
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((ip_address, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Bilinmeyen servis"
            try:
                banner = banner_grabbing(ip_address, port)
            except:
                banner = "Banner bilgisi alınamadı."
            print("Port {}: AÇIK - Servis: {} - Banner: {}".format(port, service, banner))
            open_ports.append(port)
        s.close()

    if len(open_ports) == 0:
        print("Tarama sonucu: Açık port bulunamadı.")
    else:
        print("Tarama sonucu: Toplamda {} adet açık port bulundu.".format(len(open_ports)))

def banner_grabbing(ip_address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    s.connect((ip_address, port))
    s.send(b'GET / HTTP/1.1\r\n\r\n')
    banner = s.recv(1024)
    s.close()
    return banner.decode().strip()

ip_address = input("Lütfen taramak istediğiniz IP adresini girin: ")
scan_ports(ip_address)
