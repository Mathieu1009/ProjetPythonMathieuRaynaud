import os

convertion = False

def convertir_html(file) :

    with open(file, 'r') as file :

        new_html_file = open(file.name[:-3]+".html", 'a')

        lignes_md = file.read().splitlines()

        for ligne_md in lignes_md:

            ligne_html = ""

            if (ligne_md.startswith("# ")):

                ligne_html = "<h1>"+ligne_md[2:]+"</h1>"

            if (ligne_md.startswith("## ")):
                ligne_html = "<h2>" + ligne_md[3:] + "</h2>"

            if (ligne_md.startswith("### ")):
                ligne_html = "<h3>" + ligne_md[4:] + "</h3>"

            if (ligne_md.startswith("http")):
                ligne_html = "<a href=\""+ligne_md+"\">"+ligne_md+"</a>"

            if (ligne_md.startswith("- ")):
                ligne_html = "<ul><li>" + ligne_md[2:] + "</li></ul>"

            ligne_html = ligne_md.replace("*", "</em>")

            new_html_file.write(ligne_html)

def convertir_dans_fichier(chemin):

    if(os.path.isfile(chemin)):

        convertir_html(chemin)

    else:

        print("le chemin est incorrect")

def afficher_help():

    print("-i et --input-directory : commande obligatoire qui converti le fichier donné en html dans le mêmem répertoire")
    print("-h et --help : permet d'afficher l'aide concernant les commandes de ce programme")
    print("exemple : -i fichier.md")

while not convertion :

    clavier = input("-- ")
    arguments = clavier.split(" ")

    if len(arguments) == 1 :

        if (arguments[0] == "-h" or arguments[0] == "--help") :

            afficher_help()

    elif( len(arguments) == 2):

        if (arguments[0] == "-i" or arguments[0] == "--input-directory"):

            convertir_dans_fichier(arguments[1])