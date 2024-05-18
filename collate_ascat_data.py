from multiprocessing import Pool, cpu_count
import xarray as xr
import numpy as np
import pandas as pd
import os


def make_df(i, fname):
    if not i % 100:
        print(i)
    a = xr.open_dataset(fname)
    df = pd.DataFrame(columns=['time', 'lon', 'lat', 'wind_speed', 'wvc_quality_flag'])
    for col in df.columns:
        df[col] = a[col].values.ravel()
    df = df.dropna()
    df['sat'] = fname.split('/')[-1].split('_')[3]
    return df


if __name__ == "__main__":
    input_folder = '/datasets/work/oa-acs-wp3/work/observational_data/ascat'
    output_folder = os.path.join(input_folder, 'unzip')
    fnames = [os.path.join(output_folder, f) for f in os.listdir(output_folder) if f.endswith('.nc')]
    cpus = cpu_count() - 1
    p = Pool(cpus)
    # df_list = p.imap_unordered(make_df, fnames, chunksize=16)
    df_list = p.starmap(make_df, list(zip(range(len(fnames)), fnames)), chunksize=16)
    p.close()
    for i in np.arange(len(fnames) // 500 + 1):
        master_df = pd.concat(df_list[i * 500:i * 500 + 500], ignore_index=True)
        master_df['sat'] = master_df['sat'].astype('category')
        master_df['wvc_quality_flag'] = master_df['wvc_quality_flag'].astype(int)
        master_df.to_feather(os.path.join(input_folder, 'feather', f'ascat_2016_unscreened_{i:02d}.fth'))
