#!/usr/bin/python3
############################################################
# Script simple multi-platforme pour renommer des fichiers #
# avec des motifs simples ("Copy of ", "_n#", dates)       #
# ou ajouter les informations (semestre, I.D., hash)       #
# Testé sur Python 3.6 Windows(Cygwin et non)/Linux        #
# NOTE: À l'instant c'est créer pour un motif spécifique.  #
############################################################
# TODO: Error handling
# NOTE: re.error(***)?

import os
import re

def main():
    inputs = input()
    renommer(inputs)

def input():
    # TODO: Saisir les données
    motif    = r"Copy of "
    parent   = os.path.realpath("./")
    fichiers = os.listdir(parent)
    inputs   = [motif, parent, fichiers]
    return inputs

def renommer(inputs):
    # Prendre les données et renommer les fichiers avec le motif.
    # Le condition dans re.search(***) est un solution temporarire pour
    # les changements hors l'indexe.
    motif    = inputs[0]
    parent   = inputs[1]
    fichiers = inputs[2]

    for fichier in enumerate(fichiers):
        if re.search(r".pdf",fichier[1]) is not None:
            tempNom = re.split(motif, fichier[1])
            os.rename(os.path.join("./", fichier[1]),\
                    os.path.join("./", tempNom[1]))
            re.purge()
        else:
            pass

main()
