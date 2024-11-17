# Scrapper Estadisticas Equipos

import ScraperFC as sfc
import traceback
import csv
import numpy as np
import pandas as pd

# -*- coding: utf-8 -*-

scraper = sfc.FBRef()  # initialize the FBRef scraper

try:
    
    ## Standard
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'standard', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos Equipos Standard.xlsx")

        print('Creado el fichero Standard')

    ## Porteros
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'goalkeeping', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos goalkeeping.xlsx")

        print('Creado el fichero Porteros')

    ## advanced goalkeeping
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'advanced goalkeeping', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos advanced goalkeeping.xlsx")

        print('Creado el fichero advanced goalkeeping')

    ## shooting
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'shooting', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos shooting.xlsx")

        print('Creado el fichero shooting')

    ## passing
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'passing', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos passing.xlsx")

        print('Creado el fichero passing')

    ## pass types
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'pass types', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos pass types.xlsx")

        print('Creado el fichero pass types')

    ## goal and shot creation
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'goal and shot creation', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos goal and shot creation.xlsx")

        print('Creado el fichero goal and shot creation')

    ## defensive
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'defensive', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos defensive.xlsx")

        print('Creado el fichero defensive')

    ## possession
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'possession', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos possession.xlsx")

        print('Creado el fichero possession')

    ## playing time
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'playing time', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos playing time.xlsx")

        print('Creado el fichero playing time')

    ## misc
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'misc', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[0].to_excel("../Archivos/Estadisticas Equipos misc.xlsx")

        print('Creado el fichero misc')

except:
    """ Catch and print any exceptions. This allows us to still close
    the scraper below, even if an exception occurs.
    """
    traceback.print_exc()

""" It's important to close the scraper when you're done with it.
Otherwise, you'll have a bunch of webdrivers open and running in
the background.
"""
scraper.close()