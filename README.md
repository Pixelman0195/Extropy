# Extropy v1.0
Extropy: Cyber Threat Intelligence framework for profiling, enriching and visualizing Cowrie honeypot attacks.

## Highlights
Here are a couple of main uses and features of Extropy:
+ **Threat Profiling**: Extraction and cataloguing of credentials and payloads from Cowrie log files
+ **Data Enrichment Pipeline**: Automatic enhancement of the data with informations from Shodan API (InternetDB) and geolocalisation
+ **Clusterisation**: Grouping scattered botnet intrusions by their cryptographic fingerprint (HASSH) and client version
+ **Visualisation**: Presentation of collected data on an interactive world map
+ **Active Defense**: Built-in system that automatically reports ip addresses to AbuseIPDB with keyring library used to safely manage API keys  
#### All functions are capable of working fully automatically without *any* user input

## Overview
Extropy is an open-source framework that helps with managing Cowrie-based honeypot. It's main utility is parsing through Cowrie log files, extracting data and cataloguing it in JSON files.
Moreover, it allows for enrichment of collected data using Shodan API (InternetDB) and geolocalisation from IP-API. This makes precise threat profiling possible by gathering such info as: ip address, login attempts, payloads, ISP, 
ASN number and in some cases even informations on open ports and vulnerabilities!  

For easy and compact viewing and readability an interactive world map can be generated with all the intrusion sources highlighted.  

Extropy also groups separate intrusion attempts into clusters by the intruder's HASSH number and client version which enables quickly spotting botnets scattered around the globe.
Finally for a more active apporach to cybersecurity the framework has a built-in reporting tool connected to AbuseIPDB API with the API key being securely managed by the keyring library.

## Author
I'm Pixelman0195 and Extropy is my very first project. I created Extropy as sort of a supplement for my own Cowrie Honeypot that is running on Raspberry Pi 3B.  This year (2026) I am starting college and majoring in 
Computer Science - Information Security Management, so I will gladly accept any comments on my code and/or documentation ;).

## Installation
**Extropy can be installed with just 2 commands**

First, we use `git clone` to install all of the main scripts and files:  

`git clone https://github.com/Pixelman0195/Extropy.git`  

Then we open the freshly installed file `install.sh` in order to install Cowrie and all the dependencies:  

`sudo bash install.sh`  

And voila! Both Extropy and Cowrie should be installed!

## Join the discussion!
Thank you for reading through this readme. If you have any questions I would be happy to help and if you have any comments on my project then feel free to leave them as I would greatly appreciate any form of feedback!

~~If anyone is reading this then the readme file WILL be updated tomorrow (14.09.2026), because right now I just wanna go to sleep.~~

