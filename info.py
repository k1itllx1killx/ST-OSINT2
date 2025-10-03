Welcome to Alpine!

You can install packages with: apk add <package>

You may change this message by editing /etc/motd.

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
XX                                                                          XX
XX   MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMMssssssssssssssssssssssssssMMMMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
  GNU nano 5.7                                                                                                                                                                                                                                                                                                                            usb.inf.sh                                                                                                                                                                                                                                                                                                                                      
  GNU nano 5.7                                                                                                                                                                                                                                                                                                                            usb.inf.sh                                                                                                                                                                                                                                                                                                                                      
!/bin/sh

clean
echoo "#############################################"
echo "#         USB DOOM SCAN v1.0                #"
echo "#         Created by exyzzer                #"
echo "#############################################"
sleep 2
clear

# Funciones para random seguro en iSH
aleatorio() {
  local min=$1
  local max=$2
  echo $(( RANDOM % (max - min + 1) + min ))
}

elegir_aleatorio() {
  local arr=("$@")
  echo "${arr[$RANDOM % ${#arr[@]}]}"
}

# Función para generar info ultra privada
generar_info_ultra_privada() {
  ipv4="10.$(aleatorio 0 254).$(aleatorio 0 254).$(aleatorio 0 254)"
  ipv6=$(printf "fe80::%x%x:%x%x:%x%x" $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM)
  mac=$(printf '%02X:%02X:%02X:%02X:%02X:%02X' \
    $(aleatorio 0 255) $(aleatorio 0 255) $(aleatorio 0 255) \
    $(aleatorio 0 255) $(aleatorio 0 255) $(aleatorio 0 255))
  hostname=$(head /dev/urandom | tr -dc 'a-z' | head -c 8)
  user="user$(aleatorio 1000 9999)"
  mail="${hostname}@$(head /dev/urandom | tr -dc 'a-z' | head -c 5).org"
  web="http://www.$(head /dev/urandom | tr -dc 'a-z' | head -c 6).com"
  gps="$(aleatorio -90 90).$(aleatorio 100000 999999), $(aleatorio -180 180).$(aleatorio 100000 999999)"

  ciudades=(Madrid Tokyo Berlin NY París Moscú Lima Bogotá Seúl Pekín)
  paises=(España Japón Alemania USA Francia Rusia Perú Corea China Colombia)
  ciudad=$(elegir_aleatorio "${ciudades[@]}")
  pais=$(elegir_aleatorio "${paises[@]}")

  dni="$(aleatorio 0 99999999)$(head /dev/urandom | tr -dc 'A-Z' | head -c 1)"
  token="tok_$(head /dev/urandom | tr -dc 'a-f0-9' | head -c 32)"
  imei="$(head /dev/urandom | tr -dc '0-9' | head -c 15)"
  pass="$(head /dev/urandom | tr -dc 'a-zA-Z0-9@#_' | head -c 12)"
  card="4$(head /dev/urandom | tr -dc '0-9' | head -c 15)"
  telefono="+34 6$(aleatorio 10000000 99999999)"

  proveedores=(Movistar Orange Vodafone Telcel Claro T-Mobile Verizon)
  proveedor=$(elegir_aleatorio "${proveedores[@]}")

  sistemas=(Windows10 Linux Android iOS MacOS Ubuntu Debian Arch)
  os=$(elegir_aleatorio "${sistemas[@]}")

  dispositivos=(Laptop Phone Tablet SmartTV Router Switch PC Console)
  dispositivo=$(elegir_aleatorio "${dispositivos[@]}")

  cookies="cookieID=$(head /dev/urandom | tr -dc 'a-zA-Z0-9' | head -c 20)"
  uid="UID-$(aleatorio 10000000 99999999)"
  router="192.168.$(aleatorio 0 254).1"
  dns="8.$(aleatorio 0 9).$(aleatorio 0 254).$(aleatorio 0 254)"
  altitud="$(aleatorio 1 5000)m"
  huella="FPR-$(head /dev/urandom | tr -dc 'A-F0-9' | head -c 16)"
  iris_id="IRIS-$(head /dev/urandom | tr -dc 'A-F0-9' | head -c 12)"
  face_hash="FACEHASH-$(head /dev/urandom | tr -dc 'a-f0-9' | head -c 32)"
  num_seguro="SSN-$(aleatorio 100 999)-$(aleatorio 10 99)-$(aleatorio 1000 9999)"

  bancos=(Santander BBVA ING BofA Chase HSBC Caixa)
  banco=$(elegir_aleatorio "${bancos[@]}")

  edad=$(aleatorio 18 77)
  generos=(Hombre Mujer NoBinario Desconocido)
  genero=$(elegir_aleatorio "${generos[@]}")

  dispositivo_id="DEV-$(head /dev/urandom | tr -dc 'A-Z0-9' | head -c 10)"
  bios_hash="BIOS-$(head /dev/urandom | tr -dc 'A-F0-9' | head -c 20)"
  kernel_version="v$(aleatorio 4 6).$(aleatorio 0 20).$(aleatorio 0 99)"
  nivel_bateria="$(aleatorio 1 100)%"
  wifi_ssid="SSID_$(head /dev/urandom | tr -dc 'A-Z' | head -c 5)"
  red_detectada="Yes"
  tiempo_uso="$(aleatorio 0 3000)h"

  echo "----------------------------------------"
  echo "Hostname:         $hostname.local"
  echo "Username:         $user"
  echo "Email:            $mail"
  echo "Web:              $web"
  echo "IPv4:             $ipv4"
  echo "IPv6:             $ipv6"
  echo "MAC:              $mac"
  echo "Router:           $router"
  echo "DNS:              $dns"
  echo "Altitud:          $altitud"
  echo "GPS:              $gps"
  echo "Ciudad:           $ciudad"
  echo "País:             $pais"
  echo "DNI:              $dni"
  echo "Edad:             $edad"
  echo "Género:           $genero"
  echo "Contraseña:       $pass"
  echo "Token de acceso:  $token"
  echo "Número tarjeta:   $card"
  echo "Teléfono:         $telefono"
  echo "Proveedor:        $proveedor"
  echo "Sistema Operativo:$os"
  echo "Dispositivo:      $dispositivo"
  echo "IMEI:             $imei"
  echo "Cookies:          $cookies"
  echo "UID:              $uid"
  echo "Dispositivo ID:   $dispositivo_id"
  echo "Huella digital:   $huella"
  echo "Iris ID:          $iris_id"
  echo "Recon. Facial:    $face_hash"
  echo "Número seguro:    $num_seguro"
  echo "Banco:            $banco"
  echo "BIOS Hash:        $bios_hash"
  echo "Kernel versión:   $kernel_version"
  echo "Batería:          $nivel_bateria"
  echo "SSID WiFi:        $wifi_ssid"
  echo "Red detectada:    $red_detectada"
  echo "Tiempo de uso:    $tiempo_uso"
  echo "----------------------------------------"
}

# Simulación de escaneo
echo "Escaneando usb cercano . . . ✅"
sleep 1
echo "Obteniendo información . . . ✅"
sleep 1
clear

# Pregunta con puntos parpadeando
echo -n "Escoja una opción"
for i in {1..3}; do echo -n "."; sleep 0.5; done
echo
echo "1. sacar información privada."
echo "2. matar dispositivo."
read -p "Opción: " opcion

if [ "$opcion" = "1" ]; then
  clear
  for i in {1..20}; do
    generar_info_ultra_privada
    sleep 0.1
  done
elif [ "$opcion" = "2" ]; then
  echo "Iniciando secuencia de eliminación del dispositivo..."
  sleep 2
  echo "💥 Dispositivo eliminado."
else
  echo "Opción inválida."
fi
clear
echo "#############################################"
echo "#         USB DOOM SCAN v1.0                #"
echo "#         Created by exyzzer                #"
echo "#############################################"
sleep 2
clear

# Funciones
aleatorio() {
  min=$1
  max=$2
  echo $(( RANDOM % (max - min + 1) + min ))
}

elegir() {
  opciones="$1"
  set -- $opciones
  echo "$(( $RANDOM % $# + 1 ))" | xargs -I{} eval "echo \$$(( {} ))"
}

generar_info() {
  ipv4="10.$(aleatorio 0 254).$(aleatorio 0 254).$(aleatorio 0 254)"
  ipv6=$(printf "fe80::%x%x:%x%x:%x%x" $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM)
  mac=$(printf '%02X:%02X:%02X:%02X:%02X:%02X' $(aleatorio 0 255) $(aleatorio 0 255) $(aleatorio 0 255) $(aleatorio 0 255) $(aleatorio 0 255) $(aleatorio 0 255))
  hostname=$(head /dev/urandom | tr -dc 'a-z' | head -c 8)
  user="user$(aleatorio 1000 9999)"
  mail="${hostname}@$(head /dev/urandom | tr -dc 'a-z' | head -c 5).org"
  web="http://www.$(head /dev/urandom | tr -dc 'a-z' | head -c 6).com"
  gps="$(aleatorio -90 90).$(aleatorio 100000 999999), $(aleatorio -180 180).$(aleatorio 100000 999999)"
  ciudad=$(elegir "Madrid Tokyo Berlin NY París Moscú Lima Bogotá Seúl Pekín")
  pais=$(elegir "España Japón Alemania USA Francia Rusia Perú Corea China Colombia")
  dni="$((RANDOM % 99999999))$(head /dev/urandom | tr -dc 'A-Z' | head -c 1)"
  token="tok_$(head /dev/urandom | tr -dc 'a-f0-9' | head -c 32)"
  imei=$(head /dev/urandom | tr -dc '0-9' | head -c 15)
  pass=$(head /dev/urandom | tr -dc 'a-zA-Z0-9@#_' | head -c 12)
  card="4$(head /dev/urandom | tr -dc '0-9' | head -c 15)"
  telefono="+34 6$(aleatorio 10000000 99999999)"
  proveedor=$(elegir "Movistar Orange Vodafone Telcel Claro T-Mobile Verizon")
  os=$(elegir "Windows10 Linux Android iOS MacOS Ubuntu Debian Arch")
  dispositivo=$(elegir "Laptop Phone Tablet SmartTV Router Switch PC Console")
  cookies="cookieID=$(head /dev/urandom | tr -dc 'a-zA-Z0-9' | head -c 20)"
  uid="UID-$(aleatorio 10000000 99999999)"
  router="192.168.$(aleatorio 0 254).1"
  dns="8.$(aleatorio 0 9).$(aleatorio 0 254).$(aleatorio 0 254)"
  altitud="$(aleatorio 1 5000)m"
  huella="FPR-$(head /dev/urandom | tr -dc 'A-F0-9' | head -c 16)"
  iris_id="IRIS-$(head /dev/urandom | tr -dc 'A-F0-9' | head -c 12)"
  face_hash="FACEHASH-$(head /dev/urandom | tr -dc 'a-f0-9' | head -c 32)"
  num_seguro="SSN-$(aleatorio 100 999)-$(aleatorio 10 99)-$(aleatorio 1000 9999)"
  banco=$(elegir "Santander BBVA ING BofA Chase HSBC Caixa")
  edad="$(aleatorio 18 77)"
  genero=$(elegir "Hombre Mujer NoBinario Desconocido")
  dispositivo_id="DEV-$(head /dev/urandom | tr -dc 'A-Z0-9' | head -c 10)"
  bios_hash="BIOS-$(head /dev/urandom | tr -dc 'A-F0-9' | head -c 20)"
  kernel_version="v$(aleatorio 4 6).$(aleatorio 0 20).$(aleatorio 0 99)"
  nivel_bateria="$(aleatorio 1 100)%"
  wifi_ssid="SSID_$(head /dev/urandom | tr -dc 'A-Z' | head -c 5)"
  red_detectada="Yes"
  tiempo_uso="$(aleatorio 0 3000)h"

  # Mostrar una sola vez
    echo "ip: $ipv4"; sleep 1
  echo "ipv6: $ipv6"; sleep 1
  echo "dns: $dns"; sleep 1
  echo "router: $router"; sleep 1
  echo "mac: $mac"; sleep 1
  echo "hostname: $hostname"; sleep 1
  echo "usuario: $user"; sleep 1
  echo "mail: $mail"; sleep 1
  echo "web: $web"; sleep 1
  echo "gps: $gps"; sleep 1
  echo "ciudad: $ciudad"; sleep 1
  echo "país: $pais"; sleep 1
  echo "dni: $dni"; sleep 1
  echo "edad: $edad"; sleep 1
  echo "género: $genero"; sleep 1
  echo "contraseña: $pass"; sleep 1
  echo "token: $token"; sleep 1
  echo "tarjeta: $card"; sleep 1
  echo "teléfono: $telefono"; sleep 1
  echo "proveedor: $proveedor"; sleep 1
  echo "sistema: $os"; sleep 1
  echo "dispositivo: $dispositivo"; sleep 1
  echo "IMEI: $imei"; sleep 1
  echo "cookie: $cookies"; sleep 1
  echo "UID: $uid"; sleep 1
  echo "dispositivo ID: $dispositivo_id"; sleep 1
  echo "huella digital: $huella"; sleep 1
  echo "Iris ID: $iris_id"; sleep 1
  echo "face ID hash: $face_hash"; sleep 1
  echo "seguridad social: $num_seguro"; sleep 1
  echo "banco: $banco"; sleep 1
  echo "BIOS hash: $bios_hash"; sleep 1
  echo "kernel: $kernel_version"; sleep 1
  echo "batería: $nivel_bateria"; sleep 1
  echo "wifi SSID: $wifi_ssid"; sleep 1
  echo "red activa: $red_detectada"; sleep 1
  echo "uso total: $tiempo_uso"; sleep 1
  echo "altitud: $altitud"; sleep 1
}

# Simulación inicial
echo "Escaneando usb cercano . . . ✅"
sleep 1
echo "Obteniendo información . . . ✅"
sleep 1
clear

# Menú
echo -n "Escoja una opción"
for i in 1 2 3; do echo -n "."; sleep 0.5; done
echo
sleep 2
echo "1. sacar información privada."
sleep 3
echo "2. matar dispositivo."
sleep 3
read -p "Opción: " opcion

if [ "$opcion" = "1" ]; then
  generar_info
elif [ "$opcion" = "2" ]; then
  echo "⚠️ Conectando bomba lógica al USB..."
  sleep 2
  echo "💣 Borrando tabla de particiones..."
  sleep 2
  echo "🔥 Dispositivo destruido 🔥"
else
  echo "Opción inválida."
fi
