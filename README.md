# Intro
En este proyecto se efectúa la solución a 02 maquinas tipo CTF del vulnhub: Moneybox y Chronos

# Arquitectura

<p align="center"><img src="https://drive.google.com/uc?export=view&id=11QDDqj-isuiN-SsW05uhwUWtEOQnHjuF"></img></p>

# Creación de la máquina atacante

**`Windows`**
1. Descargar e instalar las siguientes herramientas:
+ [Cmder](https://cmder.app/)
+ [Vagrant](https://www.vagrantup.com/)
2. Descargar y ejecutar las maquinas CTF del repositorio de vulnhub en el entorno de virtualizacion Virtualbox, VMWare o libvirt
3. Una vez agregadas ambas instacias de prueba se procederá a crear el equipo atacante a través del VagrantFile:
+ Crear una carpeta en la ubicación deseada y abrir Cmder en esa ruta para efectuar el clonado del repositorio
```bash
git clone https://github.com/v1c4r10us/money-chronos.git
```
+ Crear la instancia de la máquina atacante
```bash
cd vagrant-project
vagrant up
```
4. Conectarse a la instancia creada y clonar el repositorio del proyecto dentro de la misma
```bash
vagrant ssh
git clone https://github.com/v1c4r10us/money-chronos.git
exit
```
5. Abrir el manager del virtualizador (Virtualbox, VMWare o libvirt) e ingresar a la instancia creada con la credenciales vagrant:vagrant
6. Abrir una terminal dentro de ella y ejecutar el fichero 'vnc-config/steps.sh' del repositorio clonado
```bash
cd vnc-config
bash steps.sh
```
7. **Importante**: Luego del paso 6 la terminal debe quedarse en ejecución, evitar cerrarla

**`Linux`**
1. Ejecutar tal como en Windows desde el paso 2 en adelante

# Habilitar el acceso remoto hacia la máquina atacante
+ Para este fin se habilitará un acceso VNC sobre SSH bajo el layer de ngrok
+ En la instancia atacante abrir el navegador y descargar el binario de [ngrok](https://dashboard.ngrok.com/signup) 
+ Añadir el token de conexión según el procedimiento que indica
+ Abrir una terminal y generar un túnel hacia el puerto 22
```bash
./ngrok tcp 127.0.0.1:22
```
+ **Importante**: Luego de ejecutar el comando se generará la uri + puerto de acceso a la instancia y se queda en modo escucha, evitar cerrar la terminal
+ Puede cerrar el visor del virtualizador con las 02 terminales en ejecución

# Conexión de los clientes hacia la máquina atacante
+ Sobre cualquier dispositivo cliente (ordenador/móvil) ejecutar la conexión al túnel SSH establecido con el port-forwarding respectivo
```bash
ssh -L 8081:localhost:8081 vagrant@<uri-ngrok> -p <port-ngrok>
```
+ Si no hay errores y se tiene la conexion ssh establecida, proceder a probar el acceso con interfaz gráfica

# Despliegue en AWS

**`Listado de instancias`**
```bash
aws ec2 describe-instances --query "Reservations[*].Instances[*].{PrivateIp:PrivateIpAddress,PublicIp:PublicIpAddress,Name:Tags[0].Value, State:State.Name, Id:InstanceId}" --output table
```
**`Iniciar/Detener instancia`**
```bash
aws ec2 start-instances --instance-ids <InstanceId>
aws ec2 stop-instances --instance-ids <InstanceId>
```

# Colaboradores
+ Daniel Henares
+ Alejandro Jimenez
+ Mateo Vizuete
+ Edgard Huanca
