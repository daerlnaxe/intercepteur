#!/usr/bin/python2.7
# -*- coding: utf-8 -*-



"""
        Auteur: Alexandre CODOUL aka Daerlnaxe
        Date de création: 11/08/2017
        Date de modification: 11/08/2017

		Version actuelle: Alpha 1.0

        Redirect to the messages handlers added (unlimited). Work with printwmh.py
        It can work with a message handler i made: herms.py if you don't want to develop it.
        For the moment this script is not published becaue all my project was written in another manner, so
        i must rewrite some parts, even if it work actually.

        Intercept a writing signal, work with a message structured like this messHandler::lvlMess::message
        Your message handler must integrate a module named 'feed'

        Note: you can change the '::' separator by what you want.

        To redirect your output messages to this class you need to use in your code:

        myinterceptobj = intercepteur.Intercepteur()
        myinterceptobj.separateur = '::'        # - Note: '::' is present by default, it's just to explain, you can replace it by something else
        myinterceptobj.add_handler = XXX        # - It's an obj you create to manage your messages

        sys.stdout = myinterceptobj

        At this point, it prefix all the messages that don't use a message handler by "unmanaged" to guide you for the transition

        to back in normal mode, use: sys.stdout = sys.__stdout__


        Well, I think it's all... I'm sorry for my bad english, i'm French and made this without translater or help.
        
"""

import sys


class Intercepteur:

    """
        Stocke les gestionnaires de messages
    """
    @property
    def m_handlers(self): return self._m_handlers

    """
        Indique quels séparateurs on désire utiliser
    """
    @property
    def separateur(self): return self._separateur

    @separateur.setter
    def separateur(self, valeur): self._separateur = valeur


    # obligatoire avec la version de python3
    def flush(self): pass


    def __init__(self):
    #---
        self._m_handlers=[]
    #--- Porte de sortie pour afficher hors manager en cas de soucis
        self.terminal = sys.stdout

    '''
        Ajout le handler passé à la liste pour orienter les messages vers le handler de son choix
    '''
    def add_handler(self, messHandler):
        self._m_handlers.append( messHandler )

    '''
        Fonction intercptant l'écriture et redéfinissant celle ci.
    '''
    def write(self, string):

        def verif_str(valeur):
            if not isinstance( valeur, str):
                valeur = str(valeur)

    # --- Compte les occurences du séparateur dans la chaine
        if not self.separateur: self.separateur == '::'
        occur = string.count( self.separateur )

    # --- Sortie si l'utilisateur n'utlise pas l'handler
        if occur == 0:
            # === retour à la ligne
            if string=='\n' or string == ' ':
                return
        # -- texte normal
            string = f"unmanaged message: '{string}'\n"
            verif_str(string)
            self.terminal.write(string)
            return
    # fin exceptions

    # --- Séparation de la chaine en éléments
        cple = string.split(self.separateur)

        dico={}
        for param in cple:
            param = param.split('=')
            dico[ param[0] ] = param[1]

    # --- Orientation vers le handler choisi
        for handler in self.m_handlers:
            if handler.nom == dico['mHandler']:
                handler.feed(dico)
                break
