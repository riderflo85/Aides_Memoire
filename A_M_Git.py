#coding:utf-8

"""
Title: Aide Mémoire Git
Date: 17/04/2018
Comment: Aide Mémoire pour utiliser Git corrctement
Create By: GRENAILLE Florent (riderflo85) (DevOne)
"""

print(" ")
print("\t\tAide Mémoire Pour Utiliser Git")
print(" ")
print("\tCommandes de base: ")
print(" ")
print("git status --> voir l'état de Git DANS le répertoire courant")
print("\trenvoi n°1 -> 'fatal: ni ceci ni aucun de ses répertoires parents n'est un dépôt git .git'")
print("\tEN -> 'fatal: Not a git repository (or any of the parent directories): .git'")
print(" ")
print("\trenvoi n°2 -> 'Sur la branche master")
print("\t\tAucun commit")
print("\t\trien à valider (créez/copiez des fichies et utilisez 'git add' pour les suivre)'")
print("\tEN -> 'On branch master")
print("\t\tInitial commit")
print("\t\tnothing to commit (create/copy files and use 'git add' to track)'")
print(" ")
print("git init --> initialise le répertoire courant en répertoire git")
print("\trenvoi -> 'Dépôt Git vide initialisé dans /chemin/du/dossier/courant/'")
print("\tEN -> 'Initialized empty Git repository in /road/of/the/folder/'")
print(" ")
print("git add nom_du_fichier --> ajoute le fichier à l'index et dit à Git de se souvenir du fichier ainsi que des modifications dans l'index Git")
print(" ")
print("git commit [options] --> enregistre la suite des modifications, accompagné d'un message")
print("\t[options] : ")
print("\t-m -> lie(/lier) un message au commit !!!IMPORTANT TOUJOURS FAIRE UN MESSAGE AVEC -m !!! (exemple: git commit -m ''Ajout de fichier''")
print("\t-a -> tous les fichiers qui sont déjà dans l'index rajoute les si ils ont des modifications (cette option évite de faire 'git add' et peut s'utiliser comme ceci; git commit -a -m ''commentaire'')")
print(" ")
print("git checkout --> se positionne sur le commit sélectionné/voulu grâce au sha")
print(" ")
print("git checkout master --> reviens sur la branch master / reviens sur le dernier commit")
print(" ")
print("git clone --> clone/télécharge un code/projet/repository de github.com sur la machine/l'ordi courrant, pour pouvoir le modifié")
print(" ")
print("git push origin master --> envoi le code/repository;")
print("\torigin -> selectionne où  on veut envoyer le repository; autre PC, téléphone... (origin est par defaut github)")
print("\tmaster -> nom de la branche voulu (master est le nom de la branche principal)")
print(" ")
print("git pull origin master --> récupère le code/repository sur github et qui a eu des modifications d'éffectuer depuis une autre machine (autre PC, amis, collègues, github.com...)")
print(" ")
print("git branch --> affiche les branch")
print(" ")
print("git branch nom_de_la_nouvelle_branch --> créer une  nouvelle branch")
print(" ")
print("git checkout --> se  positionne sur la branch voulu")
print("\tgit checkout nom_de_la_branch")
print(" ")
print("git merge --> fusionne deux branch ensemble")
print("\tgit merge nom_de_la_branch -> fusionne la branch 'nom_de_la_branch' avec la branch sur laquelle je suis positionner")
print("\t\texemple: git branch test -> créer la branch 'test'\n\t\tgit checkout master -> se positionne sur la branch master\n\t\tgit merge test -> fusionne la branch test avec la branch master")
print(" ")
print("git blame --> liste toute les modifications qui ont été faites en indiquant les débuts des sha !!!REGARDER LA VIDEO DU COURS POUR PLUS DE COMPREHENSION!!!")
print("\tgit blame nom_du_fichier")
print(" ")
print("git show --> voir le contenu exact d'un commit")
print("\tgit show le_n°_sha > infos: le n° sha peut être celui du log ou celui de git blame")
print(" ")
print("\t!!!IMPORTANT!!!\nLa commande qui suit est très importante pour une question de sécurité car il est important de ne pas versionner et ne pas suivre à l'aide de git, des fichiers de configuration, de mot de passe, de clé de cryptage....")
print("Cette commande n'est pas une commande git directement. C'est un fichier a créer et à nommé .gitignore. Dans se fichier doit être inscrit le nom des fichiers a ignorer par git ainsi que le chemin du fichier/répertoire si celui se trouve dans des répêrtoires qui succède la racine du répertoire initialise de git (git init)")
print("Le fichier .gitignore doit être suivie/tracker en l'ajoutant à l'index de git (git add .gitignore && git commit -a -m 'message_commit')")
print(" ")
