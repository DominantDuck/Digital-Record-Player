import serial
import vlc

ser = serial.Serial('/dev/cu.usbmodem14101', 9600) 

music_files = {
    b"1430557522": "file:///Users/ag/Downloads/Drake.mp3",
   
}

instance = vlc.Instance()
player = instance.media_player_new()

try:
    current_song = None

    while True:
        data = ser.read(10)
        
        if data:
            print(data, end='')
            
            if data.strip() in music_files:
                next_song = music_files[data.strip()]
                
                if current_song:
                    player.stop()
                    print("Stopped current song:", current_song)
                
                media = instance.media_new(next_song)
                player.set_media(media)
                player.play()
                current_song = next_song
                
            elif data == b"EOF":
                break

finally:
    ser.close()
