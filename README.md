# LS-AUTO-ZABBIX
Script d'automatisation de l'installation d'un serveur zabbix sur une distribution Debian 11
## Introduction  
Bonjour est bienvenue sur mon projet LS-AUTO-ZABBIX.
Je suis actuellement étudiant en alternance pour un cursus de responsable en ingénierie système et réseaux.
Ce projet fait partie de mon projet de fin d'étude.
Il permet d'automatiser le déploiement d'un serveur zabbix sur une distribution Debian 11.
Avant de commencer, je vous invite à consulter la Licence ci-dessous

## Licence
Vous pouvez utiliser ce script selon les termes de la licence : Creative Commons CC BY-NC-SA 4.0 [disponible ici](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr) 
***
## Utilisation
### Prérequis :
>* Un environnement Debian 11 fraichement installé
>* Une adresse IP Statique
>* Le paquet Git

### Astuces
Utiliser ce scrit post-installation d'un serveur Debian 11 après avoir installé les prérequis
> **Note**: Ce script n'aborde pas la partie sécurité du serveur, c'est à vous de vous en charger.
***
 Ouvrez un terminal et connectez vous en ROOT:
 ```
 su root
 su -l
 ```
Déplacez vous dans le repertoire temporaire
 ```
 cd /tmp
 ```
 Faites un git clone du projet
 ```
  git clone https://github.com/LSProg/LS-AUTO-ZABBIX
  ```
  Déplacez vous dans le dossier LS-AUTO-ZABBIX
   ```
   cd ./LS-AUTO-ZABBIX
   ```
  Editez le script afin de changer les informations d'authentification
   ```
   DB_NAME = "Nouveau nom de la base de données"        
   DB_USER_PASSWORD = "Nouveau mot de passe"  
   DB_USER_NAME = "Nouveau nom pour l'utilisateur de la base de données "
   ```
  Executez le script python avec python3
   ```
   python3 ./main.py
   ```
   Entrez le mot de passe de l'utilisateur root (il n'est pas visible dans le terminal)
   > **Warning**: Attention il n'y a pas de vérification de mot de passe avant de lancer l'installation
   
   Et validez par la touche entrer
   Un message vous indique la fin de l'execution du script
   Pour terminer la configuration du serveur, dans votre navigateur entrez l'url http://adress_ip_serveur/zabbix
   Renseignez les diverses informations selon la configuration paramétrées dans le script.
   Un fois la configuration terminée, vous pouvez vous connecter en utilisant :
   ```
   LOGIN        : Admin
   MOT DE PASSE : zabbix
   ```
   La configuration de votre serveur zabbix devrait être normalement terminée
   ***   
   Merci d'avoir utilisé mon script
   
   Vous avez des suggestions, un problème, ou toute autre demande, n'hésitez pas à m'enovyer un email : logan.s.prog@gmail.com
