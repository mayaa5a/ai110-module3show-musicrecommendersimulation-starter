# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Goal / Task

This recommender tries to suggest 3 to 5 songs from a small catalog based on a user's favorite genre, mood, target energy, and acoustic preference.

It predicts which songs are most likely to match a simple taste profile and ranks them by score.

---

## 3. Intended Use

This system is designed for classroom exploration and learning about recommendation logic.

It is not meant for real music streaming or actual product use.

---

## 4. How the Model Works

The model compares each song to the user's profile and adds points for matches.

It awards score for matching genre and mood, gives more points when the song energy is close to the target energy, and adjusts for whether the user likes acoustic songs.

Then it sorts songs by total score and returns the top results.

---

## 5. Data Used

The model uses 17 songs from `data/songs.csv`.

Each song includes genre, mood, energy, tempo, valence, danceability, and acousticness.

The catalog is small and misses many genres, moods, and listener behavior patterns.

---

## 6. Observed Behavior / Biases

The system tends to favor common genres like pop and lofi because those appear most often in the dataset.

It can also overvalue acoustic preference since acousticness is treated as a binary on/off rule.

Rare combinations such as high energy with sad mood have few matching songs, which makes the model less reliable for those users.

---

## 7. Evaluation Process

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflicting Energy & Mood.

I compared outputs before and after changing the score weights to make energy more important and genre less important.

I looked for whether recommendations matched my intuition for strong profiles and whether unusual profiles exposed problems.

---

## 8. Ideas for Improvement

- Add more songs and more variety in genre and mood.
- Use smoother acoustic scoring instead of a single threshold.
- Add tempo or valence to the ranking to improve recommendation diversity.

---

## 9. Personal Reflection

My biggest learning moment was seeing how a small change in weights can change the top recommendations significantly.

The AI tool helped generate ideas and wording, but I needed to verify the actual scoring math and dataset behavior myself.

I was surprised that a simple weighted scoring algorithm can still produce plausible recommendations for clear profiles.

If I extended this project, I would add more song features and try to make the top list more diverse rather than dominated by one genre.
