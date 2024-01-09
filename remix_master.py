from music import PLAYLIST, SONGS

# Constants for punctuations
PUNCTUATIONS = (".", "?", "!", ":", ",")

def strip_punctuations(line: str) -> str:
    for punctuation in PUNCTUATIONS:
        line = line.replace(punctuation, "")
    return line

def substitute(song: list, old_word: str, new_word: str) -> bool:
    is_modified = False
    for idx, line in enumerate(song):
        words = line.split()
        for i, word in enumerate(words):
            stripped_word = strip_punctuations(word)
            if stripped_word.lower() == old_word.lower():
                words[i] = word.replace(stripped_word, new_word, 1)
                is_modified = True
        song[idx] = ' '.join(words)

    if is_modified:
        song[:] = [strip_punctuations(line) for line in song]
    return is_modified

def reverse_it(song: list) -> list:
    reversed_song = [' '.join(line.split()[::-1]) for line in song]
    reversed_song = [strip_punctuations(line) for line in reversed_song]
    return reversed_song


def load_song(selection: int) -> list:
    if 1 <= selection <= len(PLAYLIST):
        return [SONGS[selection -1].copy(), PLAYLIST[selection - 1], selection - 1]
    return []

# Helper functions for the main functionality
def remix_master():
    print("\nRemix-Master:")
    print("L: Load a different song")
    print("T: Title of current song")
    print("S: Substitute a word")
    print("P: Playback your song")
    print("R: Reverse it")
    print("X: Reset to original song")
    print("Q: Quit?")

#
def handle_load_song():
    print("\nSongs in playlist:")
    for idx, title in enumerate(PLAYLIST, start = 1):
        print(f"{idx}. {title}")
    try:
        selection = int(input("Enter song number: "))
        return load_song(selection)
    except ValueError:
        print("Please enter a valid song number!")
        return None

def handle_substitution(song):
    old_word = input("What word do you want to replace in the existing song?").lower()
    new_word = input("What new word do you want to use for the song?").lower()
    is_modified = substitute(song, old_word, new_word)
    if not is_modified:
        print(f"Sorry, I didn't find '{old_word}' in the existing song.")

def handle_reverse(song):
    reverse_it(song)

def print_modified_song(song):
    song_lines = '\n'.join([str(line) for line in song])
    print(f"\nTurn up the 808's and drop the beat! Here's your remix:\n{song_lines}\n🎵🎶-🎵🎶-🎵🎶-🎵🎶")

# Main loop
def main():
    current_song, current_title, current_idx = None, None, None

    while True:
        remix_master()
        choice = input("Your choice: ").upper()

        if choice == 'L':
            loaded_data = handle_load_song()
            if loaded_data:
                current_song, current_title, current_idx = loaded_data
        elif choice == 'S' and current_song:
            handle_substitution(current_song)
        elif choice == 'R' and current_song:
            handle_reverse(current_song)
        elif choice == 'P' and current_song:
            print_modified_song(current_song)
        elif choice == 'T' and current_title:
            print(f"🎵🎶-🎵🎶-🎵🎶-🎵🎶\nYou are mixing the song: {current_title}")
        elif choice == 'X' and current_song:
            current_song[:] = SONGS[current_idx].copy()
            print("Song has been reset to original!")
        elif choice == 'Q':
            print("Bravo! Your Grammy Award is being shipped to you now!")
            break
        else:
            print("This is not an option. Please try again.")

if __name__ == "__main__":
    main()