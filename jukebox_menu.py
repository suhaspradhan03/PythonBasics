from nested_data import albums              # Syntax for Import

# when we import another file, python executes all the code in that file.
# a way to deal with this, make sure that your file contains only
# the data definitions - dont include any code in the data file.
# this is one way to share data between different python files.
# while True:
#     print("Please choose your Album (Invalid choice exits):")
#     for index, (title, artist, year, songs) in enumerate(albums):                           # using a for loop to iterate over the albums
#         print("{}: {}, {}, {}, {}".format(index + 1, title, artist, year, songs))           # enumerate function to get the index of the numbers.

    # print()
    # for index,value in enumerate(albums):
    #     title,artist,year,songs = value                                         # this line is used to unpack the whole tuple to our variables
    #     print(index, title, artist, year, songs)                                # we get the 4 variables printed out

# we only want menu so we remove the extra "{}" - placeholders
SONGS_LIST_INDEX = 3          # the value should always be 3. its a constant which refers to the fourth item in the list.
SONG_TITLE_INDEX = 1

# we want this to represent a fixed value.
# when ever we see a name that is in CAPITALS that means its a CONSTANT.
while True:
    print("Please choose your Album (Invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())                               # we get input from the user and convert it to an integer.
    # our program will crash if the user types anything other than digits.
    if 1 <= choice <= len(albums):                      # check that the value they entered is in the required range.
        # songs_list = albums[choice - 1][3]              # binding a variable to the list of songs for the selected album.
        songs_list = albums[choice - 1][3]
        # we are binding the variable(song_list) to the fourth item in the tuple. using index[3]
    else:
        break
        # print("please chose a valid output: ")
        # print(albums)
    #
    # print(albums)
    # print(songs_list)

# # DISPLAYING THE LIST OF SONGS

    print("please choose your songs:")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
    # else:
    #     break
        print("playing {}".format(title))

    print("=" * 40)

# once again we got 2 levels of indexing. we get the song tuple from songs_list,
# using the users choice as the index.

# we have to sub 1 because indexes are zero based,
# and the users choice starts at 1.
# to get out second item from the tuple, we use our SONG_TITLE_INDEX constant.
# the name of the song is at position 1.
# and if you recall we sent our constant value (song_title_index to 1)