import csv
from typing import List, Dict, Tuple
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
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"].strip().lower(),
                    "mood": row["mood"].strip().lower(),
                    "energy": float(row["energy"]),
                    "tempo_bpm": float(row["tempo_bpm"]),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)

    score = 0.0
    reasons = []

    # Genre match (weight: 2.0)
    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append(f"Genre match (+2.0)")

    # Mood match (weight: 1.5)
    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.5
        reasons.append(f"Mood match (+1.5)")

    # Energy (weight: 1.0)
    energy_diff = abs(song["energy"] - user_prefs["target_energy"])
    energy_score = 1.0 * (1 - energy_diff)
    score += energy_score
    reasons.append(f"Energy match (+{energy_score:.2f})")

    # Tempo (weight: 0.8)
    tempo_diff = abs(song["tempo_bpm"] - user_prefs["target_tempo_bpm"]) / 100
    tempo_score = 0.8 * (1 - tempo_diff)
    score += tempo_score
    reasons.append(f"Tempo match (+{tempo_score:.2f})")

    # Valence (weight: 0.7)
    valence_diff = abs(song["valence"] - user_prefs["target_valence"])
    valence_score = 0.7 * (1 - valence_diff)
    score += valence_score
    reasons.append(f"Valence match (+{valence_score:.2f})")

    # Danceability (weight: 0.6)
    dance_diff = abs(song["danceability"] - user_prefs["target_danceability"])
    dance_score = 0.6 * (1 - dance_diff)
    score += dance_score
    reasons.append(f"Danceability match (+{dance_score:.2f})")

    # Acousticness (weight: 0.5)
    acoustic_diff = abs(song["acousticness"] - user_prefs["target_acousticness"])
    acoustic_score = 0.5 * (1 - acoustic_diff)
    score += acoustic_score
    reasons.append(f"Acousticness match (+{acoustic_score:.2f})")

    return (score, reasons)

    # Danceability (weight: 0.6)
    dance_diff = abs(song["danceability"] - user_prefs["target_danceability"])
    dance_score = 0.6 * (1 - dance_diff)
    score += dance_score
    reasons.append(f"Danceability match (+{dance_score:.2f})")

    # Acousticness (weight: 0.5)
    acoustic_diff = abs(song["acousticness"] - user_prefs["target_acousticness"])
    acoustic_score = 0.5 * (1 - acoustic_diff)
    score += acoustic_score
    reasons.append(f"Acousticness match (+{acoustic_score:.2f})")

    return (score, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    Recommend the top k songs based on user preferences.
    This function scores all available songs against the user's preferences,
    ranks them by score in descending order, and returns the top k recommendations.
    Args:
        user_prefs (Dict): A dictionary containing user preference data used for scoring.
        songs (List[Dict]): A list of song dictionaries to be evaluated and ranked.
        k (int, optional): The number of top recommendations to return. Defaults to 5.
    Returns:
        List[Tuple[Dict, float, str]]: A list of tuples, each containing:
            - song (Dict): The song dictionary
            - score (float): The recommendation score for the song
            - reasons (str): A pipe-separated string of reasons explaining the recommendation
    Note:
        Songs are scored using the score_song function and sorted by score in descending order.
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # Score all songs using list comprehension, then sort by score (descending), then format results
    scored_songs = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    
    top_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)[:k]
    
    return [
        (song, score, " | ".join(reasons))
        for song, score, reasons in top_songs
    ]
