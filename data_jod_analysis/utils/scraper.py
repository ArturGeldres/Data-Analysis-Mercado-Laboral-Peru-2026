import pandas as pd
from jobspy import scrape_jobs

class ScraperJods:
    def __init__(self):
        pass

    # ASEGÚRATE DE QUE 'sites' ESTÉ EN LOS ARGUMENTOS
    def scrape_jobs(self, searches, sites, results, old, country):
        df = pd.DataFrame()
        for search in searches:
           jods = scrape_jobs(
               site_name=sites, # Aquí usamos la variable que envías desde main.py
               search_term=search,
               results_wanted=results,
               hours_old=old,
               country_indeed=country,
           )
           print(f"Encontrados {len(jods)} empleos para: {search}")

           if len(jods) > 0:
               df_search = pd.DataFrame(jods)
               df = pd.concat([df, df_search], ignore_index=True)
    
        if not df.empty:
            df = df.drop_duplicates(subset=['id'])
        return df