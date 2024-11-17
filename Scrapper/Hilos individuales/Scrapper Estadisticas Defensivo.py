# Scrapper Estadisticas Defensivo

import ScraperFC as sfc
import traceback
import csv
import numpy as np
import pandas as pd
import os

# -*- coding: utf-8 -*-

scraper = sfc.FBref()  # initialize the FBRef scraper

try:

    ## defensive
        # Indicamos la función de la libreria ScrapperFC que necesitamos
        lg_table = scraper.scrape_stats("2023-2024", 'La Liga', 'defensive')

        # Verificar y crear el directorio si no existe
        output_dir = "../../Archivos"
        os.makedirs(output_dir, exist_ok=True)

        # Guardar el archivo Excel en el directorio existente
        output_path = os.path.join(output_dir, "Estadisticas Jugadores Defensivo.xlsx")
        lg_table[2].to_excel(output_path)

        # Indicando la posición 2 de la tupla, elegimos el dataframe de las estadisticas de jugadores
        #lg_table[2].to_excel("././Archivos/Estadisticas Jugadores Defensivo.xlsx")

        print('Creado el fichero defensive')

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