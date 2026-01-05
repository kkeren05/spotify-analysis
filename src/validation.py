import pandas as pd

REQUIRED_COLUMNS = [
    "track_id", "popularity", "danceability",
    "energy", "tempo", "valence", "duration_ms"
]

def validate_schema(df: pd.DataFrame) -> None:
    """
    Validate that the dataset contains all required columns.
    Raises ValueError if validation fails.
    """
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

def validate_ranges(df: pd.DataFrame) -> None:
    """
    Validate that key numerical columns fall within expected ranges.
    """
    if not df["popularity"].between(0, 100).all():
        raise ValueError("Popularity values out of range")

    if not df["energy"].between(0, 1).all():
        raise ValueError("Energy values out of range")