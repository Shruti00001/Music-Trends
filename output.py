Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/shrut/OneDrive/Documents/csv data.py
First 5 rows:
   track_id       track_name        artist  ... popularity tempo  year
0         1     Shape of You    Ed Sheeran  ...         95    96  2017
1         2  Blinding Lights    The Weeknd  ...         93   170  2020
2         3        Tum Hi Ho  Arijit Singh  ...         89    67  2013
3         4    Gangnam Style           PSY  ...         92   130  2012
4         5       God's Plan         Drake  ...         91    77  2018

[5 rows x 8 columns]

Lat 5 rows:
     track_id  track_name  ... tempo           year
135       136   Celestial  ...   120           2009
136       137  Revelation  ...   111           2002
137       138    Nocturne  ...    63           1830
138       139     Sparkle  ...   112           2013
139       140     Dreamer  ...   105  2011Load data

[5 rows x 8 columns]

Total rows in dataset: 140

Missing values in each column:
track_id      0
track_name    0
artist        0
genre         0
platform      0
popularity    0
tempo         0
year          0
dtype: int64

Data information before conversation:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 140 entries, 0 to 139
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype 
---  ------      --------------  ----- 
 0   track_id    140 non-null    int64 
 1   track_name  140 non-null    object
 2   artist      140 non-null    object
 3   genre       140 non-null    object
 4   platform    140 non-null    object
 5   popularity  140 non-null    int64 
 6   tempo       140 non-null    int64 
 7   year        140 non-null    object
dtypes: int64(3), object(5)
memory usage: 8.9+ KB
None

Data information after type conversation:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 140 entries, 0 to 139
Data columns (total 8 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   track_id    140 non-null    int64  
 1   track_name  140 non-null    object 
 2   artist      140 non-null    object 
 3   genre       140 non-null    object 
 4   platform    140 non-null    object 
 5   popularity  140 non-null    int64  
 6   tempo       140 non-null    int64  
 7   year        139 non-null    float64
dtypes: float64(1), int64(3), object(4)
memory usage: 8.9+ KB
None

Descriptive Stastics for Numerical Coulums:
       track_id  popularity       tempo         year
count  140.0000  140.000000  140.000000   139.000000
mean    70.5000   90.371429  107.550000  2003.913669
std     40.5586    3.232797   22.702114    26.799438
min      1.0000   70.000000   60.000000  1801.000000
25%     35.7500   88.000000   95.000000  2002.000000
50%     70.5000   90.000000  105.000000  2012.000000
75%    105.2500   92.250000  122.000000  2016.000000
max    140.0000   98.000000  180.000000  2021.000000
|nFrequency count for 'genre':
genre
Pop                 34
Rock                15
Rap                 13
EDM                 12
Alternative          8
R&B                  7
Bollywood            6
Soul                 5
Indie                5
Jazz                 5
Hip-Hop              4
Classical            3
Metal                2
Indian Classical     2
K-pop                2
Funk                 2
Hip-Hop/Pop          1
Grunge               1
EDM/Reggaeton        1
Funk/Pop             1
EDM/Pop              1
Beatboxing           1
Pop Rock             1
Ambient              1
Punk                 1
Electronica          1
Country              1
Electronic           1
Folk                 1
Blues                1
Post-Rock            1
Name: count, dtype: int64
