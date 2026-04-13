# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Real-world recommenders compare a user’s profile to item attributes and score each item by how well it matches. They usually combine exact matches for categorical traits like genre or mood with similarity-based scoring for numerical traits like energy or tempo. My version will prioritize songs that fit the user’s preferred genre and mood first, then reward songs whose energy and acousticness are closer to the user’s taste.

Features Used in This Simulation
Song

id
title
artist
genre
mood
energy
tempo_bpm
valence
danceability
acousticness
UserProfile

favorite_genre
favorite_mood
target_energy
likes_acoustic

---

## How The System Works

My music recommender system loads songs from a CSV file and scores each one against a user profile by awarding +2.0 points for matching genre, +1.0 for matching mood, adding energy similarity (scaled by 0.5), and adjusting for acoustic preference, then ranks the top K songs for recommendations. This approach prioritizes categorical matches for style and emotion while rewarding numerical closeness, but potential biases include over-prioritizing genre (e.g., favoring pop songs even if they don't match mood), ignoring great mood-matched songs in underrepresented genres, and assuming rigid numerical preferences that don't account for user flexibility or context.

Each song in the catalog includes genre, mood, energy, tempo, valence, danceability, and acousticness. The user profile stores favorite genre, favorite mood, target energy, and whether the user likes acoustic tracks.

The recommender computes a score for every song by checking genre and mood matches, measuring how close the song's energy is to the requested energy, and then adding or subtracting points based on acousticness and the user's preference. The system then sorts all songs by that score and returns the top results.

This means the final recommendations are chosen by the best overall match to the profile, not just one feature alone.

---

## Screenshots 
![alt text](<Screenshot 2026-04-10 at 11.10.50 AM.png>)

![alt text](<Screenshot 2026-04-13 at 12.50.15 AM.png>)

![alt text](<Screenshot 2026-04-13 at 12.50.21 AM.png>)

![alt text](<Screenshot 2026-04-13 at 12.50.31 AM.png>)

![alt text](<Screenshot 2026-04-13 at 12.50.36 AM.png>)

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python3 -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

### Summary of the experiment in this repository
- I tested four user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflicting Energy & Mood.
- I modified the scoring logic to reduce genre importance and increase energy importance, which caused the top recommendations to favor songs with energy closer to the target values.
- This change made the model more sensitive to energy alignment, especially for high-energy profiles, while exposing dataset bias for rare combinations like high energy plus sad mood.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

