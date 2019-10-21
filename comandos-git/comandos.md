# Comandos git

## Crear un repo git    
    git init
## Comitear los cambios en ficheros
    git commit -am "Mensaje"
## Ver el estado actual del repo
    git status
## Subir todos los commits a github
    git push origin master
## Revisar que el repositorio esta vinculado correctamente con github
    git remote -v

# PR - Pull Request

Cuando no puedas realizar un push porque no tienes permisos, haz una PR.
Ejemplo: labs de clase.

### Formato titulo PR
`[lab-xxxx] <Nombre Completo>`


## Crear una rama nueva
    git checkout -b <nombre_nueva_rama>

## Moverse a otra rama 
    git checkout <nombre_rama>

## Comprobar en que rama estoy
    git status

