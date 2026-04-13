# Reflection on Recommendation Outputs

- High-Energy Pop vs Chill Lofi: The high-energy profile prefers fast, non-acoustic songs with strong energy scores, while the chill profile shifts toward mellow acoustic lofi tracks. This makes sense because the model now weights energy more strongly, so the energy gap plays a bigger role in ranking.

- High-Energy Pop vs Deep Intense Rock: Both profiles favor songs with very high energy, but the rock profile also demands intense mood and a rock genre match. As a result, Storm Runner tops the rock list while pop songs like Sunrise City still appear high in the pop list due to genre and mood alignment.

- Chill Lofi vs Conflicting Energy & Mood: Chill Lofi gets good matches because the dataset contains several lofi chill songs, while the conflicting profile struggles because there are no sad, high-energy acoustic songs in this catalog. This shows a limitation: rare preference combinations are hard to satisfy in a small dataset.

- Deep Intense Rock vs Conflicting Energy & Mood: The rock profile still finds a clear best match in a true rock/intense song, but the conflicting profile ends up choosing acoustic jazz and folk songs mostly on acousticness rather than mood or energy. That reveals how dataset sparsity can skew recommendations when one preference is uncommon.
