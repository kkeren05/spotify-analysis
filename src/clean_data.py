import pandas as pd

def clean_spotify_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean Spotify audio features data.
    """
    df = df.copy()

    # Remove duplicate tracks
    df = df.drop_duplicates(subset="track_id")

    # Drop rows with missing key analysis values
    df = df.dropna(subset=[
        "popularity",
        "danceability",
        "energy",
        "tempo",
        "valence"
    ])

    # Ensure popularity is within valid range
    df = df[(df["popularity"] >= 0) & (df["popularity"] <= 100)]

    # Ensure duration is positive
    df = df[df["duration_ms"] > 0]

    return df

import pandas as pd
from src.clean_data import clean_spotify_data

def test_removes_negative_popularity():
    df = pd.DataFrame({
        "track_id": ["1"],
        "popularity": [-10],
        "danceability": [0.5],
        "energy": [0.6],
        "tempo": [120],
        "valence": [0.4],
        "duration_ms": [200000]
    })

    cleaned = clean_spotify_data(df)
    assert cleaned.empty

def test_removes_zero_duration_tracks():
    df = pd.DataFrame({
        "track_id": ["1"],
        "popularity": [50],
        "danceability": [0.5],
        "energy": [0.6],
        "tempo": [120],
        "valence": [0.4],
        "duration_ms": [0]
    })

    cleaned = clean_spotify_data(df)
    assert cleaned.empty