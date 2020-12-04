from pathlib import Path
import glob
from guessit import guessit
import imdb
import shutil
import os
# add Your movies formats to this list
video_file_formats = [".mp4", ".mkv", ".avi", ".wmv", ".mov", ".webm", ".ts", ".m2ts", ".wmv"]

# entering library info
print("NOTE: This will move you all movies to new folder and organize them")
folder_path = input("Enter Your Movie library path: ")
save_path = input("Where you want to save your Movies: ")


# get_country using Movie name
def get_country(name,year):
    try:
        ia = imdb.IMDb()
        search = ia.search_movie(name)
        movie_id = ""
        for name_imdb in search:
            if str(name_imdb).lower() == str(name).lower() or len(str(name_imdb)) == len(str(name)) or len(str(name_imdb)) == len(str(name))-1 or len(str(name_imdb)) == len(str(name)) +1:
                try:
                    if str(name_imdb["year"]) == str(year):
                        if name_imdb.movieID:
                            movie_id = name_imdb.movieID
                            break
                        else:
                            return "Not Listed"
                except:
                    return "Not Listed"
        if len(movie_id) != 0:
            movie_search = ia.get_movie(movie_id)
            countries = movie_search.data['countries']
            for country in countries:
                return country
                break
        else:
            return "Not Listed"
    except ValueError:
        return "Not Listed"


# scaning your folder for available movies with video_file_formats
movie_paths = []
for format in video_file_formats:
    movie_paths += list(Path(folder_path).glob(f"**/*{format}"))

# main work| Organizing Movies
for movie_path in movie_paths:
    file_name_with_info = str(movie_path)[::-1].replace("\\", "**", 1)[::-1].split("**")[1]
    file_name_with_guessit = guessit(file_name_with_info)
    try:
        movie_name = file_name_with_guessit["title"]
    except:
        continue

    try:
        movie_year = file_name_with_guessit["year"]
    except:
        print(file_name_with_info)
        movie_year = input("Please Enter the Year for this movie: ")
    
    try:
        screen_size = file_name_with_guessit["screen_size"]
    except:
        screen_size = ""

    try:
        source = file_name_with_guessit["source"]
    except:
        source = ""
    
    try:
        video_codec = file_name_with_guessit["video_codec"]
    except:
        video_codec = ""

    country = get_country(movie_name, movie_year)
    folder_name = f"{movie_name} ({movie_year}) {screen_size} {source} {video_codec}"
    new_path = save_path +"\\"+country+"\\"+folder_name+"\\"+file_name_with_info
    os.makedirs(save_path +"\\"+country+"\\"+folder_name, exist_ok=True)
    print(movie_path, "-->", new_path)
    shutil.move(movie_path,new_path)


