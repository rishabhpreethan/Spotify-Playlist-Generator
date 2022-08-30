import os

from spotifyclient import SpotifyClient


def main():
    # SPOTIFY_AUTHORIZATION_TOKEN='BQCXIP3dUen6NFpsGfhoufHwnS50NOHOxcbMvX1pEB3Rvi9EVNJOO0OqddryP7eTGYucLpKLO81303sVheVBZTD-xgrRBwGNC8SZxHgh27R-yfvdlclxAsmYrk5pVmAXBHSWHaKGRCzhZmLKsbl0HHfyv5XULLwG9LH3AlNb6kS74aXZ80ZjWfNhYKBoeX_mIShlzbs4X8MU'
    # SPOTIFY_USER_ID='8c3sgu4skz19vetw8pz7512r0'

    spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),os.getenv("SPOTIFY_USER_ID"))
    
    # spotify_client = SpotifyClient(SPOTIFY_AUTHORIZATION_TOKEN,SPOTIFY_USER_ID)
    # spotify_client = SpotifyClient('BQCXIP3dUen6NFpsGfhoufHwnS50NOHOxcbMvX1pEB3Rvi9EVNJOO0OqddryP7eTGYucLpKLO81303sVheVBZTD-xgrRBwGNC8SZxHgh27R-yfvdlclxAsmYrk5pVmAXBHSWHaKGRCzhZmLKsbl0HHfyv5XULLwG9LH3AlNb6kS74aXZ80ZjWfNhYKBoeX_mIShlzbs4X8MU','8c3sgu4skz19vetw8pz7512r0')                               

    num_tracks_to_visualise = int(input("How many tracks would you like to visualise? "))
    last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_visualise)

    # print("\nHere are the last ",num_tracks_to_visualise, "tracks you listened to on Spotify:")
    for index, track in enumerate(last_played_tracks):
        print(f"{index+1}- {track}")

    indexes = input("\nEnter a list of up to 5 tracks you'd like to use as seeds. Use indexes separated by a space: ")
    indexes = indexes.split()
    seed_tracks = [last_played_tracks[int(index)-1] for index in indexes]

    recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)
    print("\nHere are the recommended tracks which will be included in your new playlist:")
    for index, track in enumerate(recommended_tracks):
        print(f"{index+1}- {track}")

    playlist_name = input("\nWhat's the playlist name? ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"\nPlaylist '{playlist.name}' was created successfully.")

    spotify_client.populate_playlist(playlist, recommended_tracks)
    print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")


if __name__ == "__main__":
    main()