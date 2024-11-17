# Scrapper de tabla de clasificacion

import ScraperFC as sfc
import traceback
import csv
import numpy as np
import pandas as pd
import os

# -*- coding: utf-8 -*-

scraper = sfc.FBref() # initialize the FBRef scraper

try:

    # Indicamos la función de la libreria ScrapperFC que necesitamos
    lg_table = scraper.scrape_league_table("2023-2024", 'La Liga')

    # Si lg_table es una lista y contiene elementos
    if isinstance(lg_table, list) and len(lg_table) > 0:

        # Selecciona el primer DataFrame encontrado (ajusta si es necesario)
        df = lg_table[0]  # Cambia el índice si otro elemento es el correcto

        # Verifica y crea el directorio de salida
        output_dir = "../Archivos"
        os.makedirs(output_dir, exist_ok=True)

        # Guarda el DataFrame en un archivo Excel
        output_path = os.path.join(output_dir, "Tabla Clasificacion.xlsx")
        df.to_excel(output_path, sheet_name="Hoja1", index=False)

        print("Clasificación exportada correctamente.")
    else:
        print("Error: `lg_table` no tiene el formato esperado o está vacío.")

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