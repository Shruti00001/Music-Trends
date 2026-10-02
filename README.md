# Music Trends Analysis

Exploratory analysis of **140 popular tracks** across 5 streaming platforms (Spotify, YouTube, Amazon Music,
Apple Music, SoundCloud): data cleaning with pandas, SQL analysis, statistical tests and a Power BI dashboard.

> **Data note:** the 140 tracks were compiled by hand (`csv data.py`). Popularity and tempo values were entered
> manually, not pulled from a streaming API. The list is made of well-known hits, so popularity is high and
> narrow (70 to 98, mean 90.4). Findings describe this dataset only.

## Business question
Which genres and platforms are most represented, and does tempo or release era relate to popularity?

## Stack
Python (pandas, SciPy, Matplotlib), SQL (SQLite: window functions, CTE-style aggregation, ROW_NUMBER, RANK),
Statistics, Power BI

## Dataset
`music_trends_data.csv`: `track_id, track_name, artist, genre, platform, popularity, tempo, year` (140 rows, no missing values).
Release years run from 1801 to 2021; most tracks (111) are from 2000 to 2021.

## Cleaning steps
- Fixed a typo in the last row's year (`2011Load data` became 2011), which would otherwise turn into a missing value.
- Split combined genre labels (`EDM/Pop`, `Hip-Hop/Pop`, `Funk/Pop`) and used the first one as the primary genre (31 labels reduced to 27).
- Added a decade column and tempo bands (slow under 90 BPM, mid 90 to 110, fast over 110).

## Findings (see `analysis_summary.md` for all tables)
- **Genre mix:** Pop is the largest genre (34 tracks, 24.3%), followed by Rock (10.7%), EDM (10.0%) and Rap (9.3%).
- **Platforms:** Spotify has 72 tracks, YouTube 27, Amazon Music 21, Apple Music 19, SoundCloud 1. Spotify and YouTube each cover 15 distinct genres. Average popularity is about the same across platforms (ANOVA p = 0.88), so no platform stands out.
- **Tempo:** mid-tempo tracks (90 to 110 BPM) have slightly **lower** average popularity (89.5) than other tracks (91.0); difference about 1.5 points, t-test p = 0.012. It stays similar after removing the one low-popularity outlier (89.9 vs 91.0, p = 0.015). Correlation between tempo and popularity overall is weak (Spearman rho = 0.08, p = 0.35).
- **Era:** release year is not meaningfully related to popularity (Spearman rho = 0.08, p = 0.34).
- Limits: popularity values are narrow and hand-entered, and the list is a selection of hits, so these results cannot be generalised to all music.

## Files
| File | What it does |
|---|---|
| `csv data.py` | Original script that builds and explores the dataset |
| `music_trends_data.csv` | The 140-track dataset |
| `music_queries.sql` | 7 SQL queries: genre share (window), platform summary (RANK), tempo bands, decades, top 3 per platform (ROW_NUMBER), artists, above-genre-average (AVG OVER) |
| `analysis.py` | Cleaning, SQL, statistical tests and charts; writes result CSVs, PNGs and `analysis_summary.md` |
| `top_genres.png`, `tempo_vs_popularity.png`, `platform_popularity.png` | Charts |

## Run it
```bash
pip install -r requirements.txt
python analysis.py
```

## Dashboard (Power BI)
<!-- paste your dashboard screenshots here -->
