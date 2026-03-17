import pandas as pd
import sqlite3
from utils.scraper import ScraperJods
from utils.data_cleaning import DataCleaning

def main():
    
    searches = ["data scientist", "data analyst", "data engineer", "machine learning engineer", "business intelligence analyst"]    
    sites = ["indeed"] 
    results = 1000
    old = 1000
    country = "peru"

    scraper = ScraperJods()
    # Ahora enviamos 'sites' y el scraper debe estar listo para recibirlo
    df_jobs = scraper.scrape_jobs(searches, sites, results, old, country) 

    if df_jobs.empty:
        print("No se encontraron vacantes. Revisa los filtros o términos de búsqueda.")
        return
   
    conn = sqlite3.connect('jobs.db')
    df_jobs.to_sql('jobs_raw_table', conn, if_exists='append', index=False)
    conn.close()

    df_jobs.to_csv('jobs_raw_table.csv', index=False) # Corregido de df a df_jobs

    conn= sqlite3.connect('jobs.db')
    query = "SELECT * FROM jobs_raw_table"
    df = pd.read_sql_query(query, conn)

    datacleaner = DataCleaning()

    df_processed = datacleaner.clean_data_jobs(df)

    df_processed_sql = df_processed[['id','site','job_url','job_url_direct','title','company','date_posted','level','job_group','remote',
                                     'city','state','country','city_state','max_salary','min_salary','mean_salary','skills','experience',
                                     'education','programming_languages','languages']]

    df_processed.to_sql('jobs_cleaned_table', conn, if_exists='replace', index=False)

    df_processed.to_csv('jobs_cleaned_table.csv', index=False)

    conn.close()

if __name__ == "__main__":
    main()
