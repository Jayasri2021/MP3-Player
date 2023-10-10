import pygame
import os
import tkinter as tk
from tkinter import filedialog


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("MP3 Player")
        self.root.geometry("300x100")
        self.playlist = []

        # Initialize pygame
        pygame.init()
        pygame.mixer.init()

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="MP3 Player")
        self.label.pack()

        self.listbox = tk.Listbox(
            self.root, selectmode=tk.SINGLE, bg="black", fg="white"
        )
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(self.root, text="Add Song", command=self.add_song)
        self.add_button.pack(side=tk.LEFT)

        self.play_button = tk.Button(self.root, text="Play", command=self.play_song)
        self.play_button.pack(side=tk.LEFT)

    def add_song(self):
        song_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if song_path:
            song = os.path.basename(song_path)
            self.playlist.append((song, song_path))
            self.listbox.insert(tk.END, song)

    def play_song(self):
        selected_song_index = self.listbox.curselection()
        if selected_song_index:
            selected_song_index = int(selected_song_index[0])
            song, song_path = self.playlist[selected_song_index]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()


root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
