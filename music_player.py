import pygame

pygame.init()

song = "your_song.mp3"
pygame.mixer.init()

pygame.mixer.music.load(song)

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.quit()
