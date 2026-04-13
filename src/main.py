"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    user_profiles = {
        "High-Energy Pop": {
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.9,
            "likes_acoustic": False
        },
        "Chill Lofi": {
            "favorite_genre": "lofi",
            "favorite_mood": "chill",
            "target_energy": 0.4,
            "likes_acoustic": True
        },
        "Deep Intense Rock": {
            "favorite_genre": "rock",
            "favorite_mood": "intense",
            "target_energy": 0.95,
            "likes_acoustic": False
        },
        "Conflicting Energy & Mood": {
            "favorite_genre": "jazz",
            "favorite_mood": "sad",
            "target_energy": 0.9,
            "likes_acoustic": True
        }
    }

    for profile_name, user_prefs in user_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n=== Profile: {profile_name} ===")
        print(f"Preferences: {user_prefs}\n")
        for idx, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{idx}. {song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"   Genre: {song['genre']}, Mood: {song['mood']}, Energy: {song['energy']:.2f}, Acousticness: {song['acousticness']:.2f}")
            print(f"   Reason: {explanation}\n")


if __name__ == "__main__":
    main()
