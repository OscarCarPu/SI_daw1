function accion1() {
	echo "Listando archivos en el directorio actual:"
	ls
}
function accion2() {
	read -p "Ingrese la cadena a buscar en el nombre: " string
	find / -name "*$string*" -print 2>/dev/null | while read -r item;
	do
		if [ -d "$item" ]; then
			echo  "$item es un directorio"
		elif [ -f "$item" ]; then
			echo "$item es un archivo"
		fi
	done
}
function accion3() {
	read -p "Ingresa el nombre del nuevo directorio: " nombre_directorio
	mkdir "$nombre_directorio"
	echo "Directorio '$nombre_directorio' creado correctamente."
}
function accion4() {
	read -p "Ingresa la extensión de archivo a buscar (txt,html): " extension
	echo "Buscando archivos con extensión .$extension:"
	find / -type f -name "*.$extension" -print 2>/dev/null
}
function accion5(){
	read -p "Ingesa la direccion de un directorio: " nombre_directorio
	total=0
	find "$nombre_directorio" -type f -print 2>/dev/null | while read -r archivo; 
	do
		if [ -f "$archivo" ]; then
			palabra=$(wc -w < "$archivo")
			total=$((total + palabras))
		fi
	done
	echo "El numero de palabras en '$nombre_directorio' es '$total'."
}
clear
opcion=-1
while [ "$opcion" -ne 0 ];
do
	echo "Pulsa INTRO para escoger opcion"
	read
	clear
	echo "0 - Salir"
	echo "1 - Listar archivos y directorios del directorio actual"
	echo "2 - Buscar archivos y directorios con una cadena"
	echo "3 - Crear un directorio"
	echo "4 - Buscar archivos con una extension"
	echo "5 - Numero de palabras de cierto directorio"
	read -p "Seleccione una opción(0-5):" opcion
	case "$opcion" in
		1) accion1 ;;
		2) accion2 ;;
		3) accion3 ;;
		4) accion4 ;;
		5) accion5 ;;
		0) echo "Saliendo" ;;
		*) echo "Opcion invalida" ;;
	esac
done
