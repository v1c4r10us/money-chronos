# Intro
Cybersecurity capstone project

# Architecture

<p align="center"><img src="https://drive.google.com/uc?export=view&id=11QDDqj-isuiN-SsW05uhwUWtEOQnHjuF"></img></p>

# VM
+ Moneybox
+ Chronos

# Tools
+ Nmap
+ Nessus
+ Nikto
+ Metasploit
+ Wireshark

# Steps
1. Install docker on your Kali & start the service:

```bash
sudo apt install docker
sudo systemctl start docker
```

2. Signup on [ngrok](https://dashboard.ngrok.com/signup) (preferably with github account)

2. Open two terminals:
+ In first terminal execute:
```bash
sudo docker run -p 80:80 nginx:alpine
```
+ In second terminal execute:
```bash
sudo docker run -it -e NGROK_AUTHTOKEN=<YOUR-NGROK-TOKEN> ngrok/ngrok http 80
```

+ Test the link generated from other device. If you have access, It's possible to access other ports as 22.

# Colaborators
+ Daniel Henares
+ Alejandro Jimenez
+ Mateo Vizuete
+ Edgard Huanca
