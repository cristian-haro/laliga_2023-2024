# Scrapper Estadisticas Jugadores

import ScraperFC as sfc
import traceback
import csv
import numpy as np
import pandas as pd
from datetime import datetime

# timestamp
ts = 1617295943.17321

# convert to datetime
dt = datetime.fromtimestamp(ts)

# output 2021-04-01 22:22:23.173210


scraper = sfc.FBref()  # initialize the FBRef scraper

try:
    
    ## Standard
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats("2023-2024", 'La Liga', 'standard')

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        lg_table[2].to_excel("./Archivos/Estadisticas Standard.xlsx")

    # ## Porteros
    #     # Indicamos la función de la libreria ScrapperFC que necesitamos
    #     lg_table = scraper.scrape_stats(2023, 'La Liga', 'goalkeeping', normalize=False)

    #     # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
    #     lg_table[2].to_excel("../Archivos/Estadisticas goalkeeping.xlsx")

    # ## advanced goalkeeping
    #     # Indicamos la función de la libreria ScrapperFC que necesitamos
    #     lg_table = scraper.scrape_stats(2023, 'La Liga', 'advanced goalkeeping', normalize=False)

    #     # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
    #     lg_table[2].to_excel("../Archivos/Estadisticas advanced goalkeeping.xlsx")

    # ## shooting
    #     # Indicamos la función de la libreria ScrapperFC que necesitamos
    #     lg_table = scraper.scrape_stats(2023, 'La Liga', 'shooting', normalize=False)

    #     # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
    #     lg_table[2].to_excel("../Archivos/Estadisticas shooting.xlsx")

    # ## passing
    #     # Indicamos la función de la libreria ScrapperFC que necesitamos
    #     lg_table = scraper.scrape_stats(2023, 'La Liga', 'passing', normalize=False)

    #     # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
    #     lg_table[2].to_excel("../Archivos/Estadisticas passing.xlsx")

    # ## pass types
    #     # Indicamos la función de la libreria ScrapperFC que necesitamos
    #     lg_table = scraper.scrape_stats(2023, 'La Liga', 'pass types', normalize=False)

    #     # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
    #     lg_table[2].to_excel("../Archivos/Estadisticas pass types.xlsx")

    # ## goal and shot creation
    #     # Indicamos la función de la libreria ScrapperFC que necesitamos
    #     lg_table = scraper.scrape_stats(2023, 'La Liga', 'goal and shot creation', normalize=False)

    #     # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
    #     lg_table[2].to_excel("../Archivos/Estadisticas goal and shot creation.xlsx")

    # ## defensive
    #     # Indicamos la función de la libreria ScrapperFC que necesitamos
    #     lg_table = scraper.scrape_stats(2023, 'La Liga', 'defensive', normalize=False)

    #     # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
    #     lg_table[2].to_excel("../Archivos/Estadisticas defensive.xlsx")

    # ## possession
    #     # Indicamos la función de la libreria ScrapperFC que necesitamos
    #     lg_table = scraper.scrape_stats(2023, 'La Liga', 'possession', normalize=False)

    #     # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
    #     lg_table[2].to_excel("../Archivos/Estadisticas possession.xlsx")

    # ## playing time
    #     # Indicamos la función de la libreria ScrapperFC que necesitamos
    #     lg_table = scraper.scrape_stats(2023, 'La Liga', 'playing time', normalize=False)

    #     # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
    #     lg_table[2].to_excel("../Archivos/Estadisticas playing time.xlsx")

    # ## misc
    #     # Indicamos la función de la libreria ScrapperFC que necesitamos
    #     lg_table = scraper.scrape_stats(2023, 'La Liga', 'misc', normalize=False)

    #     # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
    #     lg_table[2].to_excel("../Archivos/Estadisticas misc.xlsx")

except:
    """ Catch and print any exceptions. This allows us to still close
    the scraper below, even if an exception occurs.
    """
    traceback.print_exc()

""" It's important to close the scraper when you're done with it.
Otherwise, you'll have a bunch of webdrivers open and running in
the background.
"""
#scraper.close()