"""
'utf-8'
Preprocess_data.py

-------------------------------------------------------------------------------------------------- xx
Author: Pedro Ruiz
Creation: xx-xx-xxxx
Version: 1.0
-------------------------------------------------------------------------------------------------- xx

This script is in charge of loading and preprocessing the data stored in the /data directory. 
Each pair of files (CSV and JSON) of video metadata, correspond to a different region and are loaded and processed separately. 
The data from each region, after being processed, is merged for each region and stored in data/data_processed under the name XX_processed. 
In addition, all processed data from all regions are concatenated into a single file that is stored in data/data_processed under the name all_data_processed.

Functions:
- load_data: 
            + Loads the data, performs preprocessing and returns a DataFrame.
            + Creates a dictionary to map the category IDs to their names.
            + Convert date columns to datetime.
            + Creates new features from publish_time.
            + Adds a new column with the region of origin of the data.
            + Adds a new column with the category names.
            + Filters new data to exclude those whose video_id is already in the database
    
- preprocess_data: 
            + Loads, preprocesses and saves the data for each region in a separate file. 
            + It also saves all the processed data in a single file.
            
            
Future Improvements:
            - Implement the encoding and translation to English of the columns 'title', 'tags', 'description' using the external online translation API such as Azure, ...,
            - Una vez con la traduccion, podriamos hacer un stopwords con NLTK para extraer los datos mas relevantes de estas categorias, ya dia de hoy stopword no da cobertura a idiomas como el indio, japones o koreano.
            - Implement parallelization and data load preprocessing to improve performance.
"""
import pandas as pd
import json
import os
import shutil




def remove_characters(input_dir, output_dir):
    """
    Recorre todos los archivos CSV en el directorio de entrada, realiza la sustitución en las columnas de cada archivo y guarda los archivos modificados en el directorio de salida. 
    También copia los archivos .json al directorio de salida.

    Parámetros:
        - input_dir: Directorio de entrada
        - output_dir: Directorio de salida
    """
    # Crea el directorio de salida si no existe
    os.makedirs(output_dir, exist_ok=True)

    # Recorre todos los archivos en el directorio de entrada
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            # Ruta al archivo de entrada
            input_path = os.path.join(input_dir, filename)
            # Ruta al archivo de salida
            output_path = os.path.join(output_dir, filename)

            # Intenta leer los datos con pandas en formato 'utf-8'
            try:
                df = pd.read_csv(input_path, encoding='utf-8')
            except UnicodeDecodeError:
                # Si falla, intenta con 'ISO-8859-1'
                df = pd.read_csv(input_path, encoding='ISO-8859-1')

            # Realiza la sustitución en todas las columnas
            df = df.replace('\n', ' ', regex=True).replace('\r', ' ', regex=True)

            # Guarda los datos modificados en el archivo de salida
            df.to_csv(output_path, index=False, encoding='utf-8')
        elif filename.endswith('.json'):
            # Ruta al archivo de entrada
            input_path = os.path.join(input_dir, filename)
            # Ruta al archivo de salida
            output_path = os.path.join(output_dir, filename)

            # Copia el archivo .json al directorio de salida
            shutil.copy(input_path, output_path)


            
            
def load_data(csv_path, json_path, output_path):
    """
    Loads CSV and JSON files, performs preprocessing and returns a DataFrame.

    Parameters:
        - csv_path: Path to the CSV file.
        - json_path: Path to the JSON file.

    Returns:
        - DataFrame with the loaded and preprocessed data.
    """
    
    # load CSV data with different encodings
    data = pd.read_csv(csv_path, encoding='utf-8', quotechar='"', quoting=1)
    
    # transform date
    data['trending_date'] = pd.to_datetime(data['trending_date'], format='%y.%d.%m')
    data['publish_time'] = pd.to_datetime(data['publish_time'])

    # Ahora podemos extraer la hora y el día de la semana
    data['publish_hour'] = data['publish_time'].dt.hour
    data['publish_day_of_week'] = data['publish_time'].dt.dayofweek
    
    # New charatceristics with the abbreviation of the data country
    data['file_prefix'] = os.path.basename(csv_path)[:2]
    
    # Load JSON data
    with open(json_path, 'r', encoding='utf-8') as f:
            categories = json.load(f)['items']

    # Create a dictionary to map the category IDs to their names.
    category_dict = {int(cat['id']): cat['snippet']['title'] for cat in categories}
    
    # Adds a new column with the names of the video categories
    data['category_name'] = data['category_id'].map(category_dict)
    
    # Create a combined column for video_id and trending_date
    data['id_date'] = data['video_id'] + data['trending_date'].astype(str)
    
    # Filter new data to exclude videos that are already in the old data
    if os.path.exists(output_path):
        old_data = pd.read_csv(output_path)
        old_data['id_date'] = old_data['video_id'] + old_data['trending_date'].astype(str)
        new_data = data[~data['id_date'].isin(old_data['id_date'])]
        return pd.concat([old_data, new_data])
    else:
        return data




def preprocess_data(input_dir, output_dir):
    """
    1. Load, preprocess and save the data for each region in a separate file. 
    2. Saves all data in a single file.
    
    Parameters:
            - input_dir: Data directory
            - output_dir: Storage directory of the processed data.
    """
    # Create a list to store all data
    all_data = []
    
    # loop over all files in the data directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            # File upload
            csv_path = os.path.join(input_dir, filename)
            json_path = os.path.join(input_dir, filename[:2] + '_category_id.json')
            output_path = os.path.join(output_dir, filename[:2] + '_processed.csv')
            data = load_data(csv_path, json_path, output_path)
            
            # Create a combined column for video_id and trending_date
            data['id_date'] = data['video_id'] + data['trending_date'].astype(str)
    
            # Filter new data to exclude videos that are already in the old data
            if os.path.exists(output_path):
                old_data = pd.read_csv(output_path)
                old_data['id_date'] = old_data['video_id'] + old_data['trending_date'].astype(str)
                new_data = data[~data['id_date'].isin(old_data['id_date'])]
                data = pd.concat([old_data, new_data])
            
            # Add to list
            all_data.append(data)
            
            # Saves the data in a separate file for each region.
            data.to_csv(output_path, index=False)
    
    # Concatenate all data and save in a single file
    all_data = pd.concat(all_data)
    all_data.to_csv(os.path.join(output_dir, 'ALL_data_processed.csv'), index=False)



    
# Llamamos a la función para eliminar la columna 'comments' de los archivos CSV y copiar los archivos .json
remove_characters('data', 'data/pre_processed')

# We call the function
preprocess_data('data/pre_processed', 'data/processed')