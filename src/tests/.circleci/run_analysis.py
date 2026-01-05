# run_analysis.py
from src.load_data import load_spotify_data
from src.clean_data import clean_spotify_data
from src.analysis import popularity_by_energy, top_tracks, correlation_matrix, tempo_vs_popularity
from src.visualisations import (
    plot_popularity_by_energy,
    plot_top_tracks,
    plot_correlation_heatmap,
    plot_tempo_vs_popularity,
    plot_feature_distributions
)

def main():
    # Loads the data 
    df = load_spotify_data(
        "data/raw/SpotifyAudioFeaturesNov2018.csv",
        "data/raw/SpotifyAudioFeaturesApril2019.csv"
    )
    print(f"Initial merged dataset shape: {df.shape}")

    # Cleans the data 
    cleaned_df = clean_spotify_data(df)
    print(f"Cleaned dataset shape: {cleaned_df.shape}")

    # Save cleaned dataset
    cleaned_df.to_csv("data/processed/spotify_cleaned.csv", index=False)
    print("Processed dataset saved to data/processed/spotify_cleaned.csv")

    # Analysis

    # 3a. Popularity by energy
    summary_energy = popularity_by_energy(cleaned_df)
    print("\nAverage popularity by energy group:")
    print(summary_energy)
    plot_popularity_by_energy(summary_energy)

    # 3b. Top 10 tracks
    top10 = top_tracks(cleaned_df, top_n=10)
    print("\nTop 10 tracks by popularity:")
    print(top10)
    plot_top_tracks(top10)

    # 3c. Correlation matrix
    corr_df = correlation_matrix(cleaned_df)
    print("\nCorrelation matrix (numeric features):")
    print(corr_df)
    plot_correlation_heatmap(corr_df)

    # 3d. Tempo vs popularity (binned averages)
    plot_tempo_vs_popularity(cleaned_df)

    # 3e. Feature distributions
    plot_feature_distributions(cleaned_df)

if __name__ == "__main__":
    main()