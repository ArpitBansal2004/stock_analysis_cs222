# Required Libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA, FastICA
from sklearn.preprocessing import StandardScaler

# ---------------- Data Collection using Yahoo Finance API ---------------- #

# Define the ticker symbol
TICKER = 'AAPL'  # This is for Apple Inc. You can replace it with any valid ticker symbol.

# Fetch historical data for the ticker
df = yf.download(TICKER, start="2020-01-01", end="2023-01-01")

# ---------------- Preliminary Analysis ---------------- #

# Fourier Transform to identify potential periodic patterns
frequencies = np.fft.fftfreq(len(df['Close']))
positive_frequencies = frequencies[frequencies > 0]
powers = np.abs(np.fft.fft(df['Close']))[frequencies > 0]

plt.plot(positive_frequencies, powers)
plt.title('Fourier Transform of Closing Prices')
plt.xlabel('Frequency')
plt.ylabel('Power')
plt.show()

# Generate a correlation matrix
correlation_matrix = df.corr()
print(correlation_matrix)

# Visualize the correlation matrix
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Financial Indicators')
plt.show()

# ---------------- PCA Analysis ---------------- #

# Standardize the data
scaler = StandardScaler()
scaled_df = scaler.fit_transform(df.dropna())

# Apply PCA
pca = PCA()
principalComponents = pca.fit_transform(scaled_df)
explained_variance = pca.explained_variance_ratio_

# Visualize explained variance for each principal component
plt.bar(range(len(explained_variance)), explained_variance, alpha=0.5, align='center', label='Individual explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.title('PCA Explained Variance')
plt.show()

# ---------------- ICA Analysis ---------------- #

# Apply ICA - assuming 5 components as an example
ica = FastICA(n_components=5)
ICs = ica.fit_transform(scaled_df)

# Visualize independent components
for i in range(ICs.shape[1]):
    plt.plot(ICs[:, i])
    plt.title(f'Independent Component {i+1}')
    plt.show()
