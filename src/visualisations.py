# src/visualisations.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Average popularity by energy 
def plot_popularity_by_energy(summary_df: pd.DataFrame):
    """
    Plot average popularity by energy group.
    """
    plt.figure(figsize=(8,5))
    plt.bar(summary_df["energy_group"], summary_df["popularity"], color='skyblue')
    plt.xlabel("Energy Level")
    plt.ylabel("Average Popularity Score")
    plt.title("Average Spotify Track Popularity by Energy Level")
    plt.tight_layout()
    plt.show()

#  Top 10 tracks by popularity 
def plot_top_tracks(df: pd.DataFrame):
    """
    Plot top N tracks by popularity.
    """
    plt.figure(figsize=(10,6))
    sns.barplot(x='popularity', y='track_name', data=df, palette="viridis")
    plt.xlabel('Popularity')
    plt.ylabel('Track Name')
    plt.title('Top 10 Spotify Tracks by Popularity')
    plt.tight_layout()
    plt.show()

# Correlation matrix 
def plot_correlation_heatmap(corr_df: pd.DataFrame):
    """
    Plot correlation matrix of numeric audio features.
    """
    plt.figure(figsize=(10,8))
    sns.heatmap(corr_df, annot=True, fmt=".2f", cmap='coolwarm', cbar_kws={'shrink':0.8})
    plt.title('Correlation Matrix of Spotify Audio Features')
    plt.tight_layout()
    plt.show()

# Tempo vs popularity (binned averages) 
def plot_tempo_vs_popularity(df: pd.DataFrame, bins=5):
    """
    Plot average popularity vs tempo using binned averages to handle large datasets.
    """
    df_copy = df.copy()
    
    # Bin tempo
    df_copy['tempo_bin'] = pd.cut(df_copy['tempo'], bins=bins)
    
    # Average popularity per bin
    avg_df = df_copy.groupby('tempo_bin')['popularity'].mean().reset_index()
    
    # Plot
    plt.figure(figsize=(10,6))
    plt.plot(
        avg_df['tempo_bin'].apply(lambda x: x.mid),  # mid-point of bin
        avg_df['popularity'],
        marker='o',
        color='dodgerblue',
        linewidth=2
    )
    plt.xlabel('Tempo (BPM)')
    plt.ylabel('Average Popularity')
    plt.title('Tempo vs Popularity of Spotify Tracks (Binned Averages)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#  Distribution histograms 
def plot_feature_distributions(df: pd.DataFrame, features=None):
    """
    Plot histograms for key audio features.
    Default features: energy, danceability, valence, tempo
    """
    if features is None:
        features = ['energy', 'danceability', 'valence', 'tempo']
    
    for feature in features:
        plt.figure(figsize=(8,5))
        sns.histplot(df[feature], bins=30, kde=True, color='purple')
        plt.xlabel(feature.capitalize())
        plt.ylabel('Count')
        plt.title(f'Distribution of {feature.capitalize()}')
        plt.tight_layout()
        plt.show()