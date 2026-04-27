# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Music Meld 1.0

Music Meld 1.0 is a classroom-scale recommender focused on transparent scoring. The goal is to make it easy to see how user preferences translate into ranked song suggestions.

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  


This recommender generates top song suggestions from a small list by comparing each song's features to a user taste profile. It assumes a user can describe their current taste with a favorite genre, favorite mood, and numeric targets like energy, tempo, and valence.

The system is intended for classroom exploration, not real users in production. It is useful for understanding recommendation tradeoffs.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The model gives each song a total score based on how well it matches the profile. Genre and mood get strong boosts for exact matches, while audio features such as energy, tempo, valence, danceability, and acousticness add partial points based on closeness to the user's targets.

After scoring all songs, it sorts them from highest to lowest and returns the top results. Compared with starter behavior, this version uses a multi-feature weighted score rather than simply returning songs in dataset order.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The dataset has 10 songs and includes a few genres and moods, such as pop, lofi, rock, ambient, jazz, synthwave, indie pop, plus moods like happy, chill, intense, focused, relaxed, and moody. This gives enough variety to test profile differences, but it is still a tiny catalog.

Many parts of real musical taste are missing, like language and context like study vs workout. Because of that, recommendations can be directionally correct but still feel shallow for complex listeners.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

The recommender works best for users with clear and consistent preferences, such as high-energy pop or chill lofi profiles. In those cases, the top results usually match expectations across both category features and numeric audio targets.

Another strength is explainability. Each recommendation includes reasons that show which features contributed to the score. That makes the system easier to debug and helps verify whether outputs are valid for each test profile.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

One weakness I found is that the recommender can create a filter bubble by rewarding exact genre and mood matches too strongly. What this means is users who pick lofi or chill keep getting very similar songs instead of a balanced mix that still fits an ovrall taste. 

I also noticed the energy scoring uses one target value, so people with mixed preferences (for example, calm study music sometimes but hype workout music) are not represented well.

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

I tested four profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflicting Sad High-Energy.

Pairwise profile comparisons:

- High-Energy Pop vs Chill Lofi: High-Energy Pop returned faster, higher-energy tracks with stronger danceability, while Chill Lofi shifted toward slower and more acoustic songs. This is as expected.
- High-Energy Pop vs Deep Intense Rock: Both profiles preferred energetic songs, but the pop profile ranked brighter/happier tracks higher, while the rock profile moved toward more intense or low valence. 
- High-Energy Pop vs Conflicting/Sad-High Energy: Both profiles still surfaced some high-energy pop due to genre and energy alignment, but the conflicting profile introduced songs with lower valence when possible. There were some unusual classifications because of the conflict arising and the overlap between the two categories.
- Chill Lofi vs Deep Intense Rock: Chill Lofi had calmer, lower-tempo, higher-acousticness songs, while Deep Intense Rock favored high-tempo, high-energy tracks. 
- Chill Lofi vs Conflicting Sad High-Energy: Chill Lofi produced soft, steady study-style recommendations, while Conflicting Sad High-Energy produced more upbeat-tempo tracks with mixed emotions. This makes sense because one profile is internally consistent and the other mixes competing preferences.
- Deep Intense Rock vs Conflicting Sad High-Energy: Both profiles ranked energetic songs, but Deep Intense Rock stayed closer to intense mood and rock-like features, while Conflicting Sad High-Energy still pulled pop songs from the catalog. 

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

My next improvement would be adding diversity-aware ranking so top results are not too repetitive in genre or mood. I would also allow preference ranges and multi-mode profiles so users can represent different listening contexts instead of one fixed target per feature.

I would also improve explanations by showing feature tradeoffs in plain language, such as when high energy outweighed a weaker mood match. With more time and data, I would add feedback signals so the model can adapt as user taste changes.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

This project helped me understand that recommendation systems are not only about finding the closest match, but also about balancing relevance. I learned how much behavior depends on design choices like feature weights and dataset composition.

What surprised me most was how quickly the model produced filtering behavior when genre and mood matches were weighted heavily. Building it made me think about how the music apps control what you hear and self impose your own taste on you rather than letting you branch out.
