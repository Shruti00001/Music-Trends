-- name: genre_share  (window function: share of all tracks)
SELECT primary_genre,
       COUNT(*)                                           AS tracks,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS share_pct,
       ROUND(AVG(popularity), 1)                          AS avg_popularity
FROM tracks
GROUP BY primary_genre
ORDER BY tracks DESC, primary_genre
LIMIT 12;

-- name: platform_summary  (aggregates + RANK window)
SELECT platform,
       COUNT(*)                        AS tracks,
       COUNT(DISTINCT primary_genre)   AS distinct_genres,
       ROUND(AVG(popularity), 1)       AS avg_popularity,
       ROUND(AVG(tempo), 0)            AS avg_tempo,
       RANK() OVER (ORDER BY COUNT(DISTINCT primary_genre) DESC) AS genre_diversity_rank
FROM tracks
GROUP BY platform
ORDER BY genre_diversity_rank;

-- name: tempo_band_popularity  (CASE bucketing)
SELECT CASE WHEN tempo < 90 THEN '1 slow (<90 BPM)'
            WHEN tempo <= 110 THEN '2 mid (90-110 BPM)'
            ELSE '3 fast (>110 BPM)' END AS tempo_band,
       COUNT(*)                  AS tracks,
       ROUND(AVG(popularity), 2) AS avg_popularity
FROM tracks
GROUP BY tempo_band
ORDER BY tempo_band;

-- name: decade_summary
SELECT decade, COUNT(*) AS tracks, ROUND(AVG(popularity), 1) AS avg_popularity
FROM tracks
GROUP BY decade
ORDER BY decade;

-- name: top3_per_platform  (ROW_NUMBER + PARTITION BY, subquery)
SELECT platform, track_name, artist, primary_genre, popularity
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY platform ORDER BY popularity DESC, track_name) AS rn
    FROM tracks
)
WHERE rn <= 3
ORDER BY platform, rn;

-- name: artists_with_3plus_tracks  (HAVING)
SELECT artist, COUNT(*) AS tracks, ROUND(AVG(popularity), 1) AS avg_popularity
FROM tracks
GROUP BY artist
HAVING COUNT(*) >= 3
ORDER BY tracks DESC, avg_popularity DESC;

-- name: above_genre_average  (AVG() OVER partition)
SELECT track_name, primary_genre, popularity,
       ROUND(AVG(popularity) OVER (PARTITION BY primary_genre), 1) AS genre_avg,
       ROUND(popularity - AVG(popularity) OVER (PARTITION BY primary_genre), 1) AS vs_genre_avg
FROM tracks
ORDER BY vs_genre_avg DESC
LIMIT 10;
