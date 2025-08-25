# Exploratory Data Analysis of TV Series Trends

## 📄 Project Goal

This project delves into the world of television series through the lens of data. Using a dataset compiled from various sources [Kaggle](https://www.kaggle.com/datasets/vandalos/movies-and-tv-shows-from-tmdb), this analysis aims to uncover patterns and trends in what makes a TV show successful and popular.  

The dataset is a snapshot retrieved from The Movie Database (TMDb) API, containing metadata for up to 50 movies and 50 TV shows per genre specifically available on Netflix, Apple TV+, Disney+ and/or Prime Video. After collecting the content by genre and platform, duplicates were removed, resulting in a total of 1,930 unique entries.

The core objective is to answer questions like:
*   Which streaming platforms host the highest-rated content?
*   What are the most dominant genres in the TV landscape?
*   How have TV show characteristics (like runtime or number of seasons) evolved over the years?
*   Is there a correlation between the year of release and viewer ratings?

## ✨ Analysis Highlights & Key Questions Answered

This project is a deep dive into the features that define modern television, showcased through a comprehensive Jupyter Notebook.

*   **Platform Wars:** A comparative analysis of IMDb ratings across major streaming services like Netflix, Prime Video, Disney+, and HBO Max to see who comes out on top for quality content.
*   **Genre Popularity:** Identification of the most prevalent genres and genre combinations. The analysis also explores which genres tend to receive the highest ratings from viewers.
*   **Temporal Trends:** Visualization of how the number of new shows released per year has changed, highlighting the recent explosion of content.
*   **Rating Distribution:** A statistical look at the distribution of IMDb ratings to understand the baseline for a "good" or "great" show.

## 📊 The Dataset

The analysis is based on the `series.csv` dataset, which contains information on TV series. Key features in the dataset include:

*   **Title:** The name of the series.
*   **Year:** The release year of the first season.
*   **IMDb:** The show's rating on IMDb.
*   **Platform:** The primary streaming service where the show is available (e.g., Netflix, Hulu).
*   **Genre:** The genre or genres associated with the show.


**Data Source:** [This data was scraped from IMDb and Sourced from a Kaggle dataset](https://www.kaggle.com/datasets/vandalos/movies-and-tv-shows-from-tmdb)

## 💻 Technologies Used

*   **Language:** Python 3
*   **Libraries:**
    *   Pandas (for data manipulation and analysis)
    *   NumPy (for numerical operations)
    *   Matplotlib & Seaborn (for data visualization)
    *   Jupyter Notebook (for creating the analysis narrative)

## 🚀 Getting Started

### Prerequisites

*   Python 3.8 or newer
*   Jupyter Notebook or a compatible IDE
*   Git

### Installation and Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Kamaranis/TV-Series-Data-Analysis
    cd TV-Series-Data-Analysis
    ```
2.  **Install the required libraries:**
    ```bash
    pip install pandas numpy matplotlib seaborn jupyter
    ```
3.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
4.  **Run the analysis:**
    Open the `Analisis_series.ipynb` file and execute the cells to follow the step-by-step exploration of the TV series data.

## 👤 Author

**Antonio Barrera Mora**

*   **LinkedIn:** https://www.linkedin.com/in/anbamo/
*   **GitHub:** @Kamaranis