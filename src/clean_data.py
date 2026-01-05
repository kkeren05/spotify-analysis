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