import os
import pandas as pd
import imdb_scraper, model_training, preprocessing, crop_script

# Directory containing the Friends episodes scripts
scripts_dir = 'data/friends'
series_name = os.path.basename(scripts_dir)
processed_data_file = f'data_processed/{series_name}_processed.csv'

# Check if the processed data file exists
if os.path.exists(processed_data_file):
    # Load the processed data
    df = pd.read_csv(processed_data_file)
else:
    # Ensure the directory exists
    if not os.path.exists('data_processed'):
        os.makedirs('data_processed')
    # Generate descriptions and save the processed data
    df = imdb_scraper.descriptions_from_scripts(scripts_dir)
    df.to_csv(processed_data_file, index=False)

# Preprocess the data
preprocessed_data = preprocessing.preprocess(df)

print(crop_script.climax_scene(preprocessed_data['Scenes'].iloc(0)))