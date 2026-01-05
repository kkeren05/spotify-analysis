# src/load_data.py
import pandas as pd

def load_spotify_data(file1: str, file2: str) -> pd.DataFrame:
    """
    Load and merge two Spotify audio features CSV files into a single DataFrame.
    """
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df = pd.concat([df1, df2], ignore_index=True)
    df.reset_index(drop=True, inplace=True)
    return df

if __name__ == "__main__":
    df = load_spotify_data(
        "../data/raw/SpotifyAudioFeaturesNov2018.csv",
        "../data/raw/SpotifyAudioFeaturesApril2019.csv"
    )
    print(df.head())