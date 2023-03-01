import spotipy,requests,os
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

CLIENT_ID = "45aa08e753344469b1ee9a4f764c9317"
CLIENT_SECRET="4108caba823f4597b0f13ed07eb954a2"
SCOPE = "playlist-modify-private"
REDIRECT_URL = "http://example.com"

# desired_date = input ("Which year do you want to travel to? Enter date in this format: YYYY-MM-DD: ")
# url = f"https://www.billboard.com/charts/hot-100/{desired_date}/"

# response = requests.get (url=url)
# billboard_web_page = response.content
#
# soup = BeautifulSoup (billboard_web_page, "html.parser")
# song_titles = soup.select (selector="div li h3#title-of-a-story")  # Scraping all h3 with song titles
# song_list = [title.getText ().strip () for title in song_titles]
# artists = soup.select (selector="div li.lrv-u-width-100p span")
# artist_list = [artist.getText ().strip () for artist in artists if not artist.getText ().strip ().isdigit () if
#                "-" not in artist.getText ().strip ()]  # Scraping artists with all spans

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.find_all(name = "h3", id="title-of-a-story")
song_names = [song.getText().strip("\n") for song in song_names_spans[3:103]]

sp = spotipy.Spotify (auth_manager=SpotifyOAuth(
    client_id= CLIENT_ID,
    client_secret= CLIENT_SECRET,
    redirect_uri= REDIRECT_URL,
    scope=SCOPE,
    cache_path="token.txt",
    show_dialog=True
))

user_id = sp.current_user()["id"]
print(user_id)

#PART2

song_uris = []

for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", limit=1, type="track",market="US")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        pass
    else:
        song_uris.append(uri)


#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)