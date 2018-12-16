# coding=utf-8
import unicodedata
from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt


class Competence:
    Version = 2.1

    def __init__(self, nom, desc, util, requis, rattrap, rp, restri, partic):
        self.Nom = nom
        self.Description = desc
        self.Utilisation = util
        self.Requis = requis
        self.Rattrapage = rattrap
        self.RolePlay = rp
        self.Restrictions = restri
        self.Particularite = partic


# Copie des compétences depuis https://www.naheulbeuk.com/jdr-docs/competences-naheulbeuk-jdr.pdf
# http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using%20Python%20to%20Convert%20PDFs%20to%20Text%20Files.php#4
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text


def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "//"  # Si pas de dossier définit, prend le dossier courant
    for pdf in os.listdir(pdfDir):  # Regarde la liste des fichiers présents
        fileExtension = pdf.split(".")[-1]  # Récupère les extensions
        if fileExtension == "pdf":  # Si extension c'est PDF
            pdfFilename = pdfDir + pdf  # Récupère le nom du fichier et le chemin
            if pdf + ".txt" in os.listdir(txtDir):
                print "Fichier déjà convertit : "+pdf + ".txt"
            else:
                text = convert(pdfFilename)  # Récupère le texte du fichier pdf
                textFilename = txtDir + pdf + ".txt"  # Récupère le nom du fichier et le chemin
                textFile = open(textFilename, "w")  # Créé le fichier txt
                textFile.write(text)  # écrit dans le fichier txt
                print "Fichier créé : "+pdf + ".txt"


pdfDir = "./pdf/"
txtDir = "./txt/"
convertMultiple(pdfDir, txtDir)





# def LastCarac(str, list):
#     str = list.split("%s : " % (str))
#     if len(str) == 2:
#         str = str[1].capitalize()
#     else:
#         str = None
#     return str
#
#
# ListCompetence = {}
# for c in cs:
#
#     # Récupération du nom
#     nom = c.split(":")[0][:-1]
#     # Transformation du nom en variable possible???
#     Id = unicodedata.normalize('NFD', unicode(nom, 'utf-8')).encode('ascii', 'ignore').capitalize().split("(")[
#         0].replace(" ", "_")
#     if Id.endswith("_"):
#         Id = Id[:-1]
#     # Récupération et traitement de la description
#     desc = c.split(":", 1)[1][1:-1]
#     if "Utilisation" in desc:
#         desc = desc.split("Utilisation")[0]
#     elif "Requis" in desc:
#         desc = desc.split("Requis")[0]
#     # Récupération et traitement des requis
#     requis = c.split("Requis : ")
#     if len(requis) == 2:
#         requis = requis[1].split("Utilisation")[0].capitalize()
#     else:
#         requis = None
#     # Récupération et traitement de l'utilisation
#     utilisation = c.split("Utilisation : ")
#     if len(utilisation) == 2:
#         if "Restrictions" in utilisation[1]:
#             utilisation = utilisation[1].split("Restrictions")[0].capitalize()
#         elif "Roleplay" in utilisation[1]:
#             utilisation = utilisation[1].split("Roleplay")[0].capitalize()
#         elif "Rattrapage" in utilisation[1]:
#             utilisation = utilisation[1].split("Rattrapage")[0].capitalize()
#         else:
#             utilisation = utilisation[1].capitalize()
#     else:
#         utilisation = None
#     # Récuprération et traitement du rattrapage
#     rattrapage = LastCarac("Rattrapage", c)
#     # Récupération et traitement du roleplay
#     roleplay = LastCarac("Roleplay", c)
#     # Récupérarion et traitement des restrictions
#     restrict = LastCarac("Restrictions", c)
#     # Récupération et traitement de la particularité
#     partic = LastCarac("Particularité", c)
#
#     # Création des instances de la classe Compétence
#
#     ListCompetence[Id] = Competence(nom, desc, utilisation, requis, rattrapage, roleplay, restrict, partic)
#
#     # print nom + " : " + desc
#     # if requis is not None:
#     #     print "Requis : " + requis
#     # if utilisation is not None:
#     #     print "Utilisation : " + utilisation
#     # if rattrapage is not None:
#     #     print "Rattrapage : " + rattrapage
#     # if roleplay is not None:
#     #     print "Roleplay : " + roleplay
#     # if restrict is not None:
#     #     print "Restriction : " + restrict
#     # if partic is not None:
#     #     print "Particularité : " + partic
#     # print
