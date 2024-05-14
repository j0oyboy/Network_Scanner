## Network Scanner
This is a Python script that scans a given IP range and lists the IP and MAC addresses of all devices on the network. It uses the scapy library to perform an ARP scan, which is a technique used to discover all the devices connected to a local network.

## Prerequisites
- Python 3.x
- Scapy library

You can install the required library using pip:

``` bash 
pip install scapy
```
## Installation 

1. Clone the repository:
    ```bash
    git clone https://github.com/souhaib-soo/Network-Scanner.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Network-Scanner
    ```
## Usage
To run the script, use the following command:

``` bash
python network_scanner.py -t <target IP / IP range>
```

## Arguments

``` bash
-t or --target: Specifies the target IP or IP range to scan.
```

## Example
To scan a specific IP range, for example 192.168.1.1/24, use:
``` bash
python network_scanner.py -t 192.168.1.1/24
```
