import os
from tqdm import tqdm
import pandas as pd
from src.omni.functions import save_pickle



def load_to_dataframe(base_dir):
    # File locations
    locations = [base_dir + '/raw/' + x for x in ['training', 'training_setB']]

    # Ready to store and concat
    data = []

    # Make dataframe with
    id = 0
    hospital = 1
    for loc in tqdm(locations):
        for file in tqdm(os.listdir(loc)):
            id_df = pd.read_csv(loc + '/' + file, sep='|')
            id_df['id'] = id  # Give a unique id
            id_df['hospital'] = hospital  # Note the hospital
            data.append(id_df)
            id += 1
        hospital += 1

    # Concat for df
    df = pd.concat(data)

    # Sort index and reorder columns
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'time'}, inplace=True)
    df = df[['id', 'time'] + [x for x in df.columns if x not in ['id', 'time', 'SepsisLabel']] + ['SepsisLabel']]

    return df


if __name__ == '__main__':
    DATA_DIR = '../../../data/sepsis'
    df = load_to_dataframe(DATA_DIR)

    save_pickle(df, DATA_DIR + '/interim/df.pkl')
