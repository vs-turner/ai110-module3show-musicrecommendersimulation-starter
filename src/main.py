"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    print(f"Loaded songs: {len(songs)}")

    # Distinct test profiles for quick experimentation.
    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.92,
            "target_tempo_bpm": 132,
            "target_valence": 0.83,
            "target_danceability": 0.86,
            "target_acousticness": 0.15,
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "calm",
            "target_energy": 0.28,
            "target_tempo_bpm": 82,
            "target_valence": 0.44,
            "target_danceability": 0.48,
            "target_acousticness": 0.78,
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.88,
            "target_tempo_bpm": 146,
            "target_valence": 0.35,
            "target_danceability": 0.42,
            "target_acousticness": 0.12,
        },
        "Conflicting Sad High-Energy": {
            "favorite_genre": "pop",
            "favorite_mood": "sad",
            "target_energy": 0.9,
            "target_tempo_bpm": 128,
            "target_valence": 0.15,
            "target_danceability": 0.8,
            "target_acousticness": 0.2,
        },
    }

    active_profile_name = "Conflicting Sad High-Energy"
    user_prefs = profiles[active_profile_name]

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"User Profile: {active_profile_name}")
    print("User Preferences:")
    for key, value in user_prefs.items():
        print(f"  {key}: {value}")

    print("\nTop recommendations:\n")
    for rec in recommendations:
        # You decide the structure of each returned item.
        # A common pattern is: (song, score, explanation)
        song, score, explanation = rec
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


if __name__ == "__main__":
    main()
