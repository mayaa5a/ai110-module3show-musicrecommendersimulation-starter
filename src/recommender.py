from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    print(f"Loading songs from {csv_path}...")
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert numerical fields to appropriate types
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness'])
            }
            songs.append(song)
    print(f"Loaded songs: {len(songs)}")
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Recommends top k songs based on user preferences."""
    def explain_score(song: Dict, user_prefs: Dict) -> str:
        reasons = []
        if song['genre'] == user_prefs['favorite_genre']:
            reasons.append("genre match")
        if song['mood'] == user_prefs['favorite_mood']:
            reasons.append("mood match")
        energy_diff = abs(song['energy'] - user_prefs['target_energy'])
        if energy_diff < 0.2:
            reasons.append("energy close")
        if user_prefs['likes_acoustic'] and song['acousticness'] > 0.5:
            reasons.append("acoustic match")
        elif not user_prefs['likes_acoustic'] and song['acousticness'] < 0.3:
            reasons.append("non-acoustic match")
        return ", ".join(reasons) if reasons else "no strong matches"
    
    # Score all songs and create tuples
    scored_songs = [
        (song, score_song(user_prefs, song), explain_score(song, user_prefs))
        for song in songs
    ]
    
    # Sort by score descending and take top k
    top_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
    
    return top_songs


def score_song(user_prefs: Dict, song: Dict) -> float:
    """Scores a single song based on user preferences."""
    score = 0.0
    
    # Genre match: reduced importance for this experiment
    if song['genre'] == user_prefs['favorite_genre']:
        score += 1.0
    
    # Mood match: unchanged importance
    if song['mood'] == user_prefs['favorite_mood']:
        score += 1.0
    
    # Energy similarity: doubled importance for the small data experiment
    energy_diff = abs(song['energy'] - user_prefs['target_energy'])
    energy_similarity = (1.0 - energy_diff) * 1.0
    score += energy_similarity
    
    # Acoustic preference
    if user_prefs['likes_acoustic']:
        if song['acousticness'] > 0.5:
            score += 0.5
        elif song['acousticness'] < 0.3:
            score -= 0.5
    else:
        if song['acousticness'] > 0.5:
            score -= 0.5
        elif song['acousticness'] < 0.3:
            score += 0.5
    
    return score
