#!/usr/bin/env python3
""" 
    ##########################################################
    #####              LS_AUTO_ZABBIX @ 2022             #####
    ##########################################################
    Auto Configuration Serveur zabbix mysql sur Debian 11 / Auto Configuration zabbix mysql Server on Debian 11
    Commentaire : Français / English
    licence : CC BY-NC-SA 4.0 | https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr
    Contact : logan.s.prog@gmail.com
    github_project : https://github.com/LSProg/LS-AUTO-ZABBIX
    my_github      : https://github.com/LSProg
"""
import os, getpass
from time import sleep

    
###### à modifier / to edit ####
DB_NAME = "db_zabbix"          # : Nom de l'utilisateur de la base de données / Username for database
DB_USER_PASSWORD = "password"  # : Mot de passe de la base de données / DataBase password
DB_USER_NAME = "zabbix"        # : Nom de l'utilisateur de la base de données / Username for database
FRENCH = True                  # : Si vrai les invites shell seront en Français sinon elles seront en Anglais / If true the shell prompts will be in French otherwise they will be in English
Set_Ip_Static = True           # ou/or False : Configuration static de l'adresse ip / static configuration ip
################################


def banner():
    """permet d'afficher une bannière en ASCII dans le shell """
    print("""
 #        #####             #    #     # ####### #######         #######    #    ######  ######  ### #     # 
 #       #     #           # #   #     #    #    #     #              #    # #   #     # #     #  #   #   #  
 #       #                #   #  #     #    #    #     #             #    #   #  #     # #     #  #    # #   
 #        #####          #     # #     #    #    #     #            #    #     # ######  ######   #     #    
 #             #         ####### #     #    #    #     #           #     ####### #     # #     #  #    # #   
 #       #     #         #     # #     #    #    #     #          #      #     # #     # #     #  #   #   #  
 #######  #####          #     #  #####     #    #######         ####### #     # ######  ######  ### #     # 
                 #######                                 #######                                             
    """)
    
    
def Print_Sheel(invite,invite2):
    """ affiche une invite dans le shell et marque un temps d'arrêt
        l'invite sera affichée en Français ou en Anglais selon le parametrage du script"""
    if FRENCH:
        print(invite)
    else:
        print(invite2)
    sleep(3)



########## SECTION MAIN ##########
banner()
if FRENCH:
    password_root = getpass.getpass("Mot de passe utilisateur Root (configuration de la base de données):\n>>>")
else:
    password_root = getpass.getpass("Password Root (for configuring database):\n>>>")

#Mofification des dépots / modification of repository
Print_Sheel("Modification du source liste","Modify source list")
with open("/etc/apt/source.list","a") as fichier:
    fichier.write("""

#Lien original /orginal link : https://debgen.simplylinux.ch/
#------------------------------------------------------------------------------#
#                   OFFICIAL DEBIAN REPOS                                      #
#------------------------------------------------------------------------------#
deb http://deb.debian.org/debian/ testing main contrib non-free
deb-src http://deb.debian.org/debian/ testing main contrib non-free

deb http://deb.debian.org/debian/ testing-updates main contrib non-free
deb-src http://deb.debian.org/debian/ testing-updates main contrib non-free

deb http://deb.debian.org/debian-security testing-security main
deb-src http://deb.debian.org/debian-security testing-security main
#-------------------------------------------------------------------------------#""")


Print_Sheel("Mise à jour des paquets","Update packages")
#mise à jour de l'ensemble des paquets
os.system("apt update --yes && apt full-upgrade --yes")

#récuperation du fichier deb sur les serveurs web zabbix
os.system("wget https://repo.zabbix.com/zabbix/6.0/debian/pool/main/z/zabbix-release/zabbix-release_6.0-3+debian11_all.deb")
#installation du paquet .deb
os.system("dpkg -i zabbix-release_6.0-3+debian11_all.deb")

Print_Sheel("Installation des paquets prerequis à zabbix","Installation of prerequisite packages to zabbix")
os.system("apt update --yes && apt install --yes apache2 php php-mysql php-mysqlnd php-ldap php-bcmath php-mbstring php-gd php-pdo php-xml libapache2-mod-php mariadb-server mariadb-client zabbix-server-mysql zabbix-frontend-php zabbix-apache-conf zabbix-sql-scripts zabbix-agent")




Print_Sheel("création de la base de données","creation of the database")
os.system(f'''mysql -uroot -p{password_root} -e "create database {DB_NAME} character set utf8mb4 collate utf8mb4_bin;"''')
os.system(f'''mysql -uroot -p{password_root} -e "create user '{DB_USER_NAME}'@'localhost' identified by '{DB_USER_PASSWORD}';"''')
os.system(f'''mysql -uroot -p{password_root} -e "grant all privileges on {DB_NAME}.* to '{DB_USER_NAME}'@'localhost';"''')
os.system(f'''mysql -uroot -p{password_root} -e "flush privileges;"''')

Print_Sheel("paramétrage de l'environement zabbix dans la base de donn&es","setting zabbix environment in database")
os.system(f"zcat /usr/share/zabbix-sql-scripts/mysql/server.sql.gz | mysql -uroot -p{password_root} {DB_NAME} -v")

Print_Sheel("Ajout des paramétres dans le fichier de zabbix_server.conf","Added parameters in zabbix_server.conf file")
with open("/etc/zabbix/zabbix_server.conf","a") as fichier:
    fichier.write(f"DBPassword={DB_USER_PASSWORD}\n")
    fichier.write(f"DBName={DB_NAME}\n")
    fichier.write(f"DBUser={DB_USER_NAME}\n")

Print_Sheel("Redémarage des services","Restarting services")
os.system("systemctl restart zabbix-server zabbix-agent apache2")

Print_Sheel("Configuration des tâches au demarrage de la machine","Configuration of tasks at machine startup")
os.system("systemctl enable zabbix-server zabbix-agent apache2")

Print_Sheel("FIN DU SCRIPT ...","END OF SCRIPT ...")
