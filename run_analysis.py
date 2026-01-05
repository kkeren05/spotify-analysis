# run_analysis.py

from src.load_data import load_spotify_data
from src.clean_data import clean_spotify_data
from src.analysis import popularity_by_energy, top_tracks, correlation_matrix, tempo_vs_popularity
from src.visualisations import (
    plot_popularity_by_energy,
    plot_top_tracks,
    plot_correlation_heatmap,
    plot_tempo_vs_popularity
)

def main():
    # Loading the data
    df = load_spotify_data(
        "data/raw/SpotifyAudioFeaturesNov2018.csv",
        "data/raw/SpotifyAudioFeaturesApril2019.csv"
    )
    print(f"Initial merged dataset shape: {df.shape}")

    # Cleaning the data
    cleaned_df = clean_spotify_data(df)
    print(f"Cleaned dataset shape: {cleaned_df.shape}")

    # Save cleaned dataset 
    cleaned_df.to_csv("data/processed/spotify_cleaned.csv", index=False)
    print("Processed dataset saved to data/processed/spotify_cleaned.csv")

    # Popularity by energy 
    summary_energy = popularity_by_energy(cleaned_df)
    print("\nAverage popularity by energy group:")
    print(summary_energy)
    plot_popularity_by_energy(summary_energy)

    # Top 10 tracks 
    top10 = top_tracks(cleaned_df, top_n=10)
    print("\nTop 10 Tracks by Popularity:")
    print(top10)
    plot_top_tracks(top10)

    # Correlation matrix 
    corr_df = correlation_matrix(cleaned_df)
    print("\nCorrelation Matrix:")
    print(corr_df)
    plot_correlation_heatmap(corr_df)

    # Tempo vs popularity 
    plot_tempo_vs_popularity(cleaned_df, bins=10)  # bins=10 for smoother, readable line

if __name__ == "__main__":
    main()