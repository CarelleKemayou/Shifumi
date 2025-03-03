#!/usr/bin/env python3
import random as rd
Game=True
Choix=["Pierre","Feuille","Ciseau"]
while Game==True:
	Choix_adv=str(input("Entrez votre choix"))
	option=rd.randint(0,2)
	option_val=Choix[option]
	if option_val=="Pierre" and Choix_adv=="Ciseau":
		print("	La machine a joué:",option_val)
		print("Victoire de  la machine")
	elif option_val=="Feuille" and Choix_adv=="Pierre":
		print(" La machine a joué:",option_val)
		print("Victoire de  la machine")
	elif option_val=="Ciseau" and Choix_adv=="Feuille":
		print(" La machine a joué:",option_val)
		print("Victoire de  la machine")
	elif Choix_adv=="Pierre" and option_val=="Ciseau":
		print(" La machine a joué:",option_val)
		print("Victoire de  l'humain")
	elif Choix_adv=="Feuille" and option_val=="Pierre":
		print(" La machine a joué:",option_val)
		print("Victoire de  l'homme")
	elif Choix_adv=="Ciseau" and option_val=="Feuille":
		print(" La machine a joué:",option_val)
		print("Victoire de  l'homme")
	else :
		print("La machine a  joué :",option_val)
		print("Match nul")
	Choix_Game=str(input("Voulez vous continuer?[Y/N]"))
	if  Choix_Game=="Y":
		continue
	else:
		break

