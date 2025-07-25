import pandas as pd
from io import StringIO

#DEFINE THE CSV DATA AS A MULTI-LINE STRING CONTAINING 140 ROWS OF MUSIC DATA.
csv_data = """track_id,track_name,artist,genre,platform,popularity,tempo,year
1,Shape of You,Ed Sheeran,Pop,Spotify,95,96,2017
2,Blinding Lights,The Weeknd,Pop,Spotify,93,170,2020
3,Tum Hi Ho,Arijit Singh,Bollywood,YouTube,89,67,2013
4,Gangnam Style,PSY,K-pop,YouTube,92,130,2012
5,God's Plan,Drake,Rap,Spotify,91,77,2018
6,Classical Raga,Ravi Shankar,Indian Classical,Amazon Music,85,60,1970
7,Jai Ho,A. R. Rahman,Bollywood,Spotify,90,105,2008
8,Bad Guy,Billie Eilish,Pop,Spotify,94,135,2019
9,Drop It Like It's Hot,Snoop Dogg,Rap,YouTube,88,92,2004
10,Beatbox Battle,Unknown,Beatboxing,SoundCloud,70,105,2021
11,Rolling in the Deep,Adele,Pop,Spotify,92,104,2010
12,Lose Yourself,Eminem,Rap,Spotify,96,171,2002
13,Bohemian Rhapsody,Queen,Rock,Amazon Music,98,144,1975
14,Imagine,John Lennon,Rock,Spotify,94,75,1971
15,Shape of My Heart,Sting,Rock,Spotify,85,66,1993
16,Chaiyya Chaiyya,Sukhwinder Singh,Bollywood,YouTube,87,110,1998
17,Uptown Funk,Bruno Mars,Funk/Pop,Spotify,95,115,2014
18,Closer,The Chainsmokers,EDM/Pop,Spotify,90,95,2016
19,Thunderstruck,AC/DC,Rock,Amazon Music,88,134,1990
20,Perfect,Ed Sheeran,Pop,Spotify,93,95,2017
21,Counting Stars,OneRepublic,Pop Rock,Spotify,90,122,2013
22,Lean On,Major Lazer,EDM,Spotify,89,98,2015
23,HUMBLE.,Kendrick Lamar,Rap,Spotify,92,150,2017
24,Halo,Beyonce,Pop,Spotify,91,84,2008
25,Bad Romance,Lady Gaga,Pop,Spotify,94,119,2009
26,Smells Like Teen Spirit,Nirvana,Grunge,Apple Music,93,117,1991
27,Lose Control,Missy Elliott,Rap,Spotify,87,134,2005
28,Happy,Pharrell Williams,Pop,Spotify,95,160,2013
29,Taki Taki,DJ Snake,EDM/Reggaeton,Spotify,90,125,2018
30,Zinda,Siddharth Mahadevan,Bollywood,YouTube,86,108,2013
31,New Rules,Dua Lipa,Pop,Spotify,92,116,2017
32,Sunflower,Post Malone,Hip-Hop,Spotify,93,90,2018
33,Believer,Imagine Dragons,Rock,Spotify,91,125,2017
34,Don’t Start Now,Dua Lipa,Pop,Spotify,94,124,2019
35,Shape of You (Remix),Major Lazer,EDM,Spotify,90,100,2017
36,Sugar,Maroon 5,Pop,Spotify,89,120,2014
37,One Dance,Drake,Hip-Hop/Pop,Spotify,92,104,2016
38,Faded,Alan Walker,EDM,Spotify,90,90,2015
39,Closer (Acoustic),The Chainsmokers,Pop,Spotify,87,92,2016
40,Shape (Live),Ed Sheeran,Pop,Apple Music,88,96,2015
41,Summer Vibes,Calvin Harris,EDM,Spotify,90,128,2018
42,City Lights,Dua Lipa,Pop,Spotify,91,120,2019
43,Midnight Drive,The Weeknd,R&B,Apple Music,93,110,2018
44,Echoes of Time,Coldplay,Alternative,Spotify,88,102,2008
45,Rhythm Divine,Enrique Iglesias,Pop,Amazon Music,87,114,1999
46,Infinite Dreams,Lana Del Rey,Indie,YouTube,89,68,2012
47,Electric Pulse,David Guetta,EDM,Spotify,92,125,2014
48,Moonlight Sonata,Beethoven,Classical,Amazon Music,95,60,1801
49,Fire in My Soul,Eminem,Rap,Spotify,94,130,2009
50,Whispers,Adele,Soul,Apple Music,90,75,2015
51,Highway Star,Deep Purple,Rock,Amazon Music,87,112,1972
52,Mystic River,Norah Jones,Jazz,YouTube,85,88,2002
53,Desert Rose,Sting,Pop,Spotify,91,95,1999
54,Galactic Journey,Muse,Alternative,Amazon Music,86,138,2006
55,Euphoria,BTS,K-pop,YouTube,93,102,2019
56,Sunrise,Kygo,EDM,Spotify,88,105,2018
57,Soulful Nights,John Legend,R&B,Apple Music,90,88,2010
58,Wildfire,Imagine Dragons,Rock,Spotify,92,120,2017
59,Vintage Love,Frank Sinatra,Jazz,Amazon Music,89,78,1964
60,Bollywood Beat,AR Rahman,Bollywood,YouTube,94,110,2001
61,Rhythm Nation,Janet Jackson,Pop,Spotify,91,105,1989
62,Street Dreams,Jay-Z,Rap,Apple Music,88,98,2003
63,Blue Horizon,Coldplay,Alternative,Spotify,90,110,2002
64,Golden Era,Missy Elliott,Rap,Spotify,87,120,2005
65,Vibe With Me,Maroon 5,Pop,YouTube,90,115,2014
66,Infinite Love,Ed Sheeran,Pop,Spotify,92,83,2020
67,Rhythmic Soul,Alicia Keys,R&B,Amazon Music,89,97,2010
68,Deep Blue,Sam Smith,Pop,Spotify,88,100,2017
69,Revolution,Green Day,Punk,YouTube,86,180,2004
70,Tenderness,Sade,Soul,Apple Music,93,92,1992
71,Urban Jungle,Travis Scott,Hip-Hop,Spotify,95,134,2018
72,Majestic,Queen,Rock,Amazon Music,91,85,1975
73,Paradise Found,Calvin Harris,EDM,Spotify,90,128,2018
74,Rhythm and Blues,Usher,R&B,Spotify,88,102,2004
75,Mystery,The Weeknd,R&B,YouTube,93,107,2016
76,Indian Rhapsody,Ravi Shankar,Indian Classical,Amazon Music,92,60,1965
77,Bollywood Stars,Lata Mangeshkar,Bollywood,YouTube,91,66,1980
78,Modern Heart,Taylor Swift,Pop,Spotify,95,120,2014
79,Dancing Feet,Lady Gaga,Pop,YouTube,94,118,2009
80,Electric Dreams,Zedd,EDM,Spotify,89,128,2015
81,Dreamscape,Enya,Ambient,Apple Music,90,70,2000
82,Nightfall,The xx,Indie,Spotify,87,95,2017
83,Funky Town,Lipps Inc,Funk,Amazon Music,86,124,1980
84,Rising Sun,Shakira,Pop,Spotify,90,98,2010
85,Cinematic,Hans Zimmer,Classical,Apple Music,94,75,1994
86,Summertime,DJ Snake,EDM,Spotify,89,102,2018
87,Old Town Road,Lil Nas X,Country,YouTube,93,136,2019
88,Electric Heart,P!nk,Pop,Spotify,88,104,2012
89,Free Spirit,Maroon 5,Funk,YouTube,90,121,2011
90,Unforgettable,Nat King Cole,Jazz,Amazon Music,95,80,1960
91,Rise Up,Andra Day,Soul,Spotify,89,92,2015
92,Speed of Light,Avicii,EDM,YouTube,94,126,2013
93,Under Pressure,Queen,Rock,Spotify,97,118,1982
94,Northern Lights,Aurora,Indie,Apple Music,88,75,2016
95,Heartbeat,Childish Gambino,Hip-Hop,Spotify,91,110,2011
96,Wild Ones,Flo Rida,Pop,YouTube,90,128,2011
97,Bliss,Pharrell Williams,Pop,Spotify,87,100,2014
98,New Age,Imagine Dragons,Rock,Amazon Music,89,122,2012
99,Slow Motion,Tame Impala,Alternative,Spotify,88,98,2015
100,Moonlight,Frank Ocean,R&B,Apple Music,93,80,2016
101,Chill Out,Moby,Electronica,Spotify,86,90,1999
102,Golden Lights,Coldplay,Alternative,Amazon Music,90,105,2000
103,Bounce,Pitbull,Hip-Hop,Spotify,89,130,2009
104,Fireworks,Katy Perry,Pop,YouTube,92,124,2010
105,Rewind,Nelly,Rap,Spotify,88,102,2004
106,Wildcard,Snoop Dogg,Rap,Apple Music,87,101,2006
107,Neon Dreams,The Chainsmokers,EDM,Spotify,90,120,2017
108,Rebel,Eminem,Rap,YouTube,92,148,2002
109,Golden Age,The Beatles,Rock,Apple Music,95,110,1968
110,Vibrations,Queen,Rock,Spotify,90,115,1978
111,Retrograde,Daft Punk,Electronic,Amazon Music,92,123,2013
112,Pure Energy,Limp Bizkit,Rap,Spotify,88,138,1997
113,Waves,Mr. Probz,Pop,YouTube,90,89,2013
114,Sunset Boulevard,Oasis,Rock,Apple Music,87,108,1995
115,Spark,Kiiara,EDM,Spotify,89,121,2016
116,Cityscape,Zayn,Pop,Amazon Music,90,102,2018
117,Acoustic Nights,Ed Sheeran,Pop,YouTube,91,100,2014
118,Harmony,Sam Smith,Soul,Spotify,94,83,2017
119,Rollercoaster,Twenty One Pilots,Alternative,YouTube,88,132,2018
120,Wild Heart,Zara Larsson,Pop,Spotify,90,110,2019
121,Eclipse,Linkin Park,Rock,Apple Music,93,125,2001
122,Velvet,The Weeknd,R&B,Spotify,89,102,2016
123,Afterglow,Ed Sheeran,Pop,Amazon Music,92,95,2020
124,Revolutionary,Kendrick Lamar,Rap,Spotify,91,150,2017
125,Voodoo,Marilyn Manson,Metal,YouTube,87,130,2003
126,Northern Star,Norah Jones,Jazz,Apple Music,90,92,2002
127,Bittersweet,Adele,Soul,Spotify,94,84,2015
128,Collide,Howie Day,Alternative,YouTube,88,100,2004
129,Serenade,Michael Bublé,Jazz,Amazon Music,91,82,2003
130,Smooth Sailing,Jack Johnson,Folk,Spotify,90,95,2005
131,Rising Tide,Bon Iver,Indie,Apple Music,87,105,2011
132,Electric Blues,Gary Clark Jr.,Blues,Amazon Music,92,112,2014
133,Whirlwind,Panic! at the Disco,Alternative,Spotify,90,130,2016
134,Echo,Sia,Pop,Apple Music,91,98,2014
135,Mystery Train,Elvis Presley,Rock,YouTube,93,105,1965
136,Celestial,Explosions in the Sky,Post-Rock,Spotify,88,120,2009
137,Revelation,Disturbed,Metal,Amazon Music,89,111,2002
138,Nocturne,Chopin,Classical,YouTube,95,63,1830
139,Sparkle,Miley Cyrus,Pop,Spotify,90,112,2013
140,Dreamer,Foster the People,Indie,Apple Music,92,105,2011Load data
"""
#use stringIO to stimulate reading from a file
csv_file = StringIO(csv_data)

#read the csv data into a dataframe
data = pd.read_csv(csv_file)

# print the first 5 rows to verify the data has been loaded
print("First 5 rows:")
print(data.head())

#print the last 5 rows to verify all 140 rows are included
print("\nLat 5 rows:")
print(data.tail())

#optionally, print the total number of rows to confirm we have 140 enteries
print("\nTotal rows in dataset:", len (data))

# 2. Clean and summarize the data:

#check for missing values in each column
print("\nMissing values in each column:")
print(data.isnull().sum())

#display basic data information
print("\nData information before conversation:")
print(data.info())

#convert selected columns to numeric types(if needed)
data['track_id'] = pd.to_numeric(data['track_id'], errors = 'coerce')
data['popularity'] = pd.to_numeric(data['popularity'], errors = 'coerce')
data['tempo'] = pd.to_numeric(data['tempo'], errors = 'coerce')
data['year'] = pd.to_numeric(data['year'], errors = 'coerce')

#verify conversation by showing the info again
print("\nData information after type conversation:")
print(data.info())

#GENERATE DESCRITIVE STATISTICS FOR NUMERICAL COLUMNS
print("\nDescriptive Stastics for Numerical Coulums:")
print(data.describe())

#frequency count for 'genre' column
print("|nFrequency count for 'genre':")
print(data['genre'].value_counts())

# 3. Visualization of data by using pandas:


import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Enable interactive mode so that plt.show() does not block the entire script
plt.ion()

#DEFINE THE CSV DATA AS A MULTI-LINE STRING CONTAINING 140 ROWS OF MUSIC DATA.
csv_data = """track_id,track_name,artist,genre,platform,popularity,tempo,year
1,Shape of You,Ed Sheeran,Pop,Spotify,95,96,2017
2,Blinding Lights,The Weeknd,Pop,Spotify,93,170,2020
3,Tum Hi Ho,Arijit Singh,Bollywood,YouTube,89,67,2013
4,Gangnam Style,PSY,K-pop,YouTube,92,130,2012
5,God's Plan,Drake,Rap,Spotify,91,77,2018
6,Classical Raga,Ravi Shankar,Indian Classical,Amazon Music,85,60,1970
7,Jai Ho,A. R. Rahman,Bollywood,Spotify,90,105,2008
8,Bad Guy,Billie Eilish,Pop,Spotify,94,135,2019
9,Drop It Like It's Hot,Snoop Dogg,Rap,YouTube,88,92,2004
10,Beatbox Battle,Unknown,Beatboxing,SoundCloud,70,105,2021
11,Rolling in the Deep,Adele,Pop,Spotify,92,104,2010
12,Lose Yourself,Eminem,Rap,Spotify,96,171,2002
13,Bohemian Rhapsody,Queen,Rock,Amazon Music,98,144,1975
14,Imagine,John Lennon,Rock,Spotify,94,75,1971
15,Shape of My Heart,Sting,Rock,Spotify,85,66,1993
16,Chaiyya Chaiyya,Sukhwinder Singh,Bollywood,YouTube,87,110,1998
17,Uptown Funk,Bruno Mars,Funk/Pop,Spotify,95,115,2014
18,Closer,The Chainsmokers,EDM/Pop,Spotify,90,95,2016
19,Thunderstruck,AC/DC,Rock,Amazon Music,88,134,1990
20,Perfect,Ed Sheeran,Pop,Spotify,93,95,2017
21,Counting Stars,OneRepublic,Pop Rock,Spotify,90,122,2013
22,Lean On,Major Lazer,EDM,Spotify,89,98,2015
23,HUMBLE.,Kendrick Lamar,Rap,Spotify,92,150,2017
24,Halo,Beyonce,Pop,Spotify,91,84,2008
25,Bad Romance,Lady Gaga,Pop,Spotify,94,119,2009
26,Smells Like Teen Spirit,Nirvana,Grunge,Apple Music,93,117,1991
27,Lose Control,Missy Elliott,Rap,Spotify,87,134,2005
28,Happy,Pharrell Williams,Pop,Spotify,95,160,2013
29,Taki Taki,DJ Snake,EDM/Reggaeton,Spotify,90,125,2018
30,Zinda,Siddharth Mahadevan,Bollywood,YouTube,86,108,2013
31,New Rules,Dua Lipa,Pop,Spotify,92,116,2017
32,Sunflower,Post Malone,Hip-Hop,Spotify,93,90,2018
33,Believer,Imagine Dragons,Rock,Spotify,91,125,2017
34,Don’t Start Now,Dua Lipa,Pop,Spotify,94,124,2019
35,Shape of You (Remix),Major Lazer,EDM,Spotify,90,100,2017
36,Sugar,Maroon 5,Pop,Spotify,89,120,2014
37,One Dance,Drake,Hip-Hop/Pop,Spotify,92,104,2016
38,Faded,Alan Walker,EDM,Spotify,90,90,2015
39,Closer (Acoustic),The Chainsmokers,Pop,Spotify,87,92,2016
40,Shape (Live),Ed Sheeran,Pop,Apple Music,88,96,2015
41,Summer Vibes,Calvin Harris,EDM,Spotify,90,128,2018
42,City Lights,Dua Lipa,Pop,Spotify,91,120,2019
43,Midnight Drive,The Weeknd,R&B,Apple Music,93,110,2018
44,Echoes of Time,Coldplay,Alternative,Spotify,88,102,2008
45,Rhythm Divine,Enrique Iglesias,Pop,Amazon Music,87,114,1999
46,Infinite Dreams,Lana Del Rey,Indie,YouTube,89,68,2012
47,Electric Pulse,David Guetta,EDM,Spotify,92,125,2014
48,Moonlight Sonata,Beethoven,Classical,Amazon Music,95,60,1801
49,Fire in My Soul,Eminem,Rap,Spotify,94,130,2009
50,Whispers,Adele,Soul,Apple Music,90,75,2015
51,Highway Star,Deep Purple,Rock,Amazon Music,87,112,1972
52,Mystic River,Norah Jones,Jazz,YouTube,85,88,2002
53,Desert Rose,Sting,Pop,Spotify,91,95,1999
54,Galactic Journey,Muse,Alternative,Amazon Music,86,138,2006
55,Euphoria,BTS,K-pop,YouTube,93,102,2019
56,Sunrise,Kygo,EDM,Spotify,88,105,2018
57,Soulful Nights,John Legend,R&B,Apple Music,90,88,2010
58,Wildfire,Imagine Dragons,Rock,Spotify,92,120,2017
59,Vintage Love,Frank Sinatra,Jazz,Amazon Music,89,78,1964
60,Bollywood Beat,AR Rahman,Bollywood,YouTube,94,110,2001
61,Rhythm Nation,Janet Jackson,Pop,Spotify,91,105,1989
62,Street Dreams,Jay-Z,Rap,Apple Music,88,98,2003
63,Blue Horizon,Coldplay,Alternative,Spotify,90,110,2002
64,Golden Era,Missy Elliott,Rap,Spotify,87,120,2005
65,Vibe With Me,Maroon 5,Pop,YouTube,90,115,2014
66,Infinite Love,Ed Sheeran,Pop,Spotify,92,83,2020
67,Rhythmic Soul,Alicia Keys,R&B,Amazon Music,89,97,2010
68,Deep Blue,Sam Smith,Pop,Spotify,88,100,2017
69,Revolution,Green Day,Punk,YouTube,86,180,2004
70,Tenderness,Sade,Soul,Apple Music,93,92,1992
71,Urban Jungle,Travis Scott,Hip-Hop,Spotify,95,134,2018
72,Majestic,Queen,Rock,Amazon Music,91,85,1975
73,Paradise Found,Calvin Harris,EDM,Spotify,90,128,2018
74,Rhythm and Blues,Usher,R&B,Spotify,88,102,2004
75,Mystery,The Weeknd,R&B,YouTube,93,107,2016
76,Indian Rhapsody,Ravi Shankar,Indian Classical,Amazon Music,92,60,1965
77,Bollywood Stars,Lata Mangeshkar,Bollywood,YouTube,91,66,1980
78,Modern Heart,Taylor Swift,Pop,Spotify,95,120,2014
79,Dancing Feet,Lady Gaga,Pop,YouTube,94,118,2009
80,Electric Dreams,Zedd,EDM,Spotify,89,128,2015
81,Dreamscape,Enya,Ambient,Apple Music,90,70,2000
82,Nightfall,The xx,Indie,Spotify,87,95,2017
83,Funky Town,Lipps Inc,Funk,Amazon Music,86,124,1980
84,Rising Sun,Shakira,Pop,Spotify,90,98,2010
85,Cinematic,Hans Zimmer,Classical,Apple Music,94,75,1994
86,Summertime,DJ Snake,EDM,Spotify,89,102,2018
87,Old Town Road,Lil Nas X,Country,YouTube,93,136,2019
88,Electric Heart,P!nk,Pop,Spotify,88,104,2012
89,Free Spirit,Maroon 5,Funk,YouTube,90,121,2011
90,Unforgettable,Nat King Cole,Jazz,Amazon Music,95,80,1960
91,Rise Up,Andra Day,Soul,Spotify,89,92,2015
92,Speed of Light,Avicii,EDM,YouTube,94,126,2013
93,Under Pressure,Queen,Rock,Spotify,97,118,1982
94,Northern Lights,Aurora,Indie,Apple Music,88,75,2016
95,Heartbeat,Childish Gambino,Hip-Hop,Spotify,91,110,2011
96,Wild Ones,Flo Rida,Pop,YouTube,90,128,2011
97,Bliss,Pharrell Williams,Pop,Spotify,87,100,2014
98,New Age,Imagine Dragons,Rock,Amazon Music,89,122,2012
99,Slow Motion,Tame Impala,Alternative,Spotify,88,98,2015
100,Moonlight,Frank Ocean,R&B,Apple Music,93,80,2016
101,Chill Out,Moby,Electronica,Spotify,86,90,1999
102,Golden Lights,Coldplay,Alternative,Amazon Music,90,105,2000
103,Bounce,Pitbull,Hip-Hop,Spotify,89,130,2009
104,Fireworks,Katy Perry,Pop,YouTube,92,124,2010
105,Rewind,Nelly,Rap,Spotify,88,102,2004
106,Wildcard,Snoop Dogg,Rap,Apple Music,87,101,2006
107,Neon Dreams,The Chainsmokers,EDM,Spotify,90,120,2017
108,Rebel,Eminem,Rap,YouTube,92,148,2002
109,Golden Age,The Beatles,Rock,Apple Music,95,110,1968
110,Vibrations,Queen,Rock,Spotify,90,115,1978
111,Retrograde,Daft Punk,Electronic,Amazon Music,92,123,2013
112,Pure Energy,Limp Bizkit,Rap,Spotify,88,138,1997
113,Waves,Mr. Probz,Pop,YouTube,90,89,2013
114,Sunset Boulevard,Oasis,Rock,Apple Music,87,108,1995
115,Spark,Kiiara,EDM,Spotify,89,121,2016
116,Cityscape,Zayn,Pop,Amazon Music,90,102,2018
117,Acoustic Nights,Ed Sheeran,Pop,YouTube,91,100,2014
118,Harmony,Sam Smith,Soul,Spotify,94,83,2017
119,Rollercoaster,Twenty One Pilots,Alternative,YouTube,88,132,2018
120,Wild Heart,Zara Larsson,Pop,Spotify,90,110,2019
121,Eclipse,Linkin Park,Rock,Apple Music,93,125,2001
122,Velvet,The Weeknd,R&B,Spotify,89,102,2016
123,Afterglow,Ed Sheeran,Pop,Amazon Music,92,95,2020
124,Revolutionary,Kendrick Lamar,Rap,Spotify,91,150,2017
125,Voodoo,Marilyn Manson,Metal,YouTube,87,130,2003
126,Northern Star,Norah Jones,Jazz,Apple Music,90,92,2002
127,Bittersweet,Adele,Soul,Spotify,94,84,2015
128,Collide,Howie Day,Alternative,YouTube,88,100,2004
129,Serenade,Michael Bublé,Jazz,Amazon Music,91,82,2003
130,Smooth Sailing,Jack Johnson,Folk,Spotify,90,95,2005
131,Rising Tide,Bon Iver,Indie,Apple Music,87,105,2011
132,Electric Blues,Gary Clark Jr.,Blues,Amazon Music,92,112,2014
133,Whirlwind,Panic! at the Disco,Alternative,Spotify,90,130,2016
134,Echo,Sia,Pop,Apple Music,91,98,2014
135,Mystery Train,Elvis Presley,Rock,YouTube,93,105,1965
136,Celestial,Explosions in the Sky,Post-Rock,Spotify,88,120,2009
137,Revelation,Disturbed,Metal,Amazon Music,89,111,2002
138,Nocturne,Chopin,Classical,YouTube,95,63,1830
139,Sparkle,Miley Cyrus,Pop,Spotify,90,112,2013
140,Dreamer,Foster the People,Indie,Apple Music,92,105,2011Load data
"""
csv_file = StringIO (csv_data)
data = pd.read_csv(csv_file)

genre_counts=data['genre'].value_counts()
ax = genre_counts.plot(kind='pie', autopct= '%1.1f%%', figsize = (8,8), title = "Genre Distribution (Pandas)")
plt.ylabel('') # remove default ylabel
plt.show()  # close the figures to continue

# b. Histogram: distribution of track tempos using pandas plot

data['tempo'].plot(kind='hist', bins=15, color='skyblue', edgecolor='black', figsize=(8,5), title="Distribution of Track Tempos")
plt.xlabel("Tempo")
plt.show()

# c. line plot: average popularity over years(all data)
popularity_by_year = data.groupby('year')['popularity'].mean()
popularity_by_year.plot(kind='line',marker='1',figsize=(20,10),title="Average Popularity Over years(All Genres)")
plt.xlabel("year")
plt.ylabel("Average Poplarity")
plt.grid(True)
plt.show()

data['year'] = pd.to_numeric(data['year'], errors = 'coerce')
data['decade'] = (data['year'] //10) * 10

# filter for Indian msic: Bolywood and Indian classical
Indian_music = data[data['genre'].isin(['Bollywood', 'Indian Claaical'])]

 #Calculate average popularity per decade for these genres, then plot

popularity_by_decade = Indian_music.groupby(['decade','genre'])['popularity'].mean().unstack()
popularity_by_decade.plot(kind='line', marker='1', figsize=(20,10), title="Indian Music Popularity Trend by Decade")
plt.xlabel("Decade")
plt.ylabel("Average Popularity")
plt.grid(True)
plt.legend(title="Genre")
plt.show()

# e. Bar chart: records count by decade and genre
records_by_decade = data.groupby(['decade', 'genre']).size().unstack(fill_value=0)
records_by_decade.plot(kind='bar', figsize= (12,7), title= " Music Records Count by Decade and Genre")
plt.xlabel("Decade")
plt.ylabel("Record Count")
plt.legend(title="Genre", bbox_to_anchor= (1.05, 1))
plt.show
