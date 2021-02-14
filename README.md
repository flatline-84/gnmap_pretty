# gnmap_pretty
A parser for gnmap files.

## Requirements

Requires Python 3.5+ and Colorama.  
`pip3 install colorama`

## Usage

`python3 gnmapretty.py <infile>`

## Output Sample

```
NMAP Version:        v7.91
Scan Start:          Sun Jan 31 20:31:08 2021
Scan End:            Sun Jan 31 20:51:56 2021
Host:                10.11.1.72
Status:              Up
        Port: 22
                State:             open
                Protocol:          tcp
                Service:           ssh
                Banner:            OpenSSH 5.8p1 Debian 7ubuntu1 (Ubuntu Linux; protocol 2.0)
        Port: 25
                State:             open
                Protocol:          tcp
                Service:           smtp?
                Banner:
        Port: 80
                State:             open
                Protocol:          tcp
                Service:           http
                Banner:            Apache httpd 2.2.20 ((Ubuntu))
        Port: 110
                State:             open
                Protocol:          tcp
                Service:           pop3?
                Banner:
        Port: 111
                State:             open
                Protocol:          udp
                Service:           rpcbind
                Banner:            2-4 (RPC #100000)
        Port: 119
                State:             open
                Protocol:          tcp
                Service:           nntp?
                Banner:
        Port: 2049
                State:             open
                Protocol:          udp
                Service:           nfs_acl
                Banner:            2-3 (RPC #100227)
        Port: 5353
                State:             open
                Protocol:          udp
                Service:           mdns
                Banner:            DNS-based service discovery
```