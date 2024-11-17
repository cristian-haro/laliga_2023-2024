# Scrapper Estadisticas Jugadores

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
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Generales.xlsx")

        print('Creado el fichero Standard')

    ## Porteros
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'goalkeeping', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Porteros.xlsx")

        print('Creado el fichero Porteros')

    ## advanced goalkeeping
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'advanced goalkeeping', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Porteros Avanzado.xlsx")

        print('Creado el fichero advanced goalkeeping')

    ## shooting
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'shooting', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Tiros.xlsx")

        print('Creado el fichero shooting')

    ## passing
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'passing', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Pases.xlsx")

        print('Creado el fichero passing')

    ## pass types
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'pass types', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Tipos de pases.xlsx")

        print('Creado el fichero pass types')

    ## goal and shot creation
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'goal and shot creation', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Creacion de goles y tiros.xlsx")

        print('Creado el fichero goal and shot creation')

    ## defensive
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'defensive', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Defensivo.xlsx")

        print('Creado el fichero defensive')

    ## possession
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'possession', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Posesion.xlsx")

        print('Creado el fichero possession')

    ## playing time
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'playing time', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Tiempo de juego.xlsx")

        print('Creado el fichero playing time')

    ## misc
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats(2023, 'La Liga', 'misc', normalize=False)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("../Archivos/Estadisticas Jugadores Diversas.xlsx")

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