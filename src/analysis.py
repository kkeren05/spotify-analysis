# src/analysis.py
import pandas as pd

def popularity_by_energy(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["energy_group"] = pd.cut(
        df["energy"],
        bins=[0, 0.3, 0.6, 1.0],
        labels=["Low energy", "Medium energy", "High energy"]
    )
    summary = df.groupby("energy_group", observed=False)["popularity"].mean().reset_index()
    return summary

def top_tracks(df: pd.DataFrame, top_n=10) -> pd.DataFrame:
    """
    Return the top N tracks by popularity.
    """
    return df[['artist_name', 'track_name', 'popularity']].sort_values(
        by='popularity', ascending=False
    ).head(top_n)

def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = ['acousticness','danceability','duration_ms','energy',
                    'instrumentalness','liveness','loudness','speechiness',
                    'tempo','valence','popularity']
    return df[numeric_cols].corr()

def tempo_vs_popularity(df: pd.DataFrame) -> pd.DataFrame:
    return df[['tempo','popularity']]