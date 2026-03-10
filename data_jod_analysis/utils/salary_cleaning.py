import pandas as pd
import numpy as np # Importamos numpy para manejar NaNs
from config import INTERVAL_FACTORS

class SalaryProcessor:

    def __init__(self):
        self.interval_factors = INTERVAL_FACTORS

    def transform_salary(self, row):
        # Asignamos los valores originales
        min_val = row.get('min_amount')
        max_val = row.get('max_amount')

        # Si ambos son nulos, no hay nada que calcular
        if pd.isna(min_val) and pd.isna(max_val):
            row['min_salary'] = np.nan
            row['max_salary'] = np.nan
            return row

        # Obtenemos el factor (por defecto 1 si el intervalo no existe)
        factor = self.interval_factors.get(row.get('interval'), 1)

        # Solo multiplicamos si el valor NO es nulo
        row['min_salary'] = min_val * factor if pd.notna(min_val) else np.nan
        row['max_salary'] = max_val * factor if pd.notna(max_val) else np.nan

        # Lógica de corrección para cifras excesivas (millones)
        if pd.notna(row['min_salary']) and row['min_salary'] > 1000000:
            row['min_salary'] /= 1000
        if pd.notna(row['max_salary']) and row['max_salary'] > 1000000:
            row['max_salary'] /= 1000
        
        return row
    
    def clean_salaries(self, df):
        # Aplicamos la transformación fila por fila
        df = df.apply(self.transform_salary, axis=1)
        
        # Calculamos el promedio solo donde ambos valores existen
        # Usamos fillna(0) temporalmente o manejamos el error de suma de NaNs
        df['mean_salary'] = (df['min_salary'] + df['max_salary']) / 2

        return df