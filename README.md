# 🎵 Spotify Playlist Tournament

A Python tool that helps you **rank songs in your Spotify playlist** using a **tournament-style** ranking system. Instead of manually sorting your playlist, this script lets you **compare songs head-to-head** in a series of matchups until you determine your favorites. Once the tournament is complete, the script will **automatically reorder your Spotify playlist** based on your rankings.

---

## 🚀 Features
- **Tournament-Style Ranking:** Compare two songs at a time until a winner is determined.
- **Round Progress Updates:** Displays the current round number, remaining songs, and matchups.
- **Automatic Playlist Sorting:** Once you've ranked the songs, the script reorders your playlist accordingly.
- **Spotify API Integration:** Fetches and updates your playlist automatically.

---

## 🛠 Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/spotify-playlist-tournament.git
   cd spotify-playlist-tournament
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up your Spotify API credentials:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create a new app
   - Get your **Client ID** and **Client Secret**
   - Set the **Redirect URI** to:
     ```
     http://localhost:8888/callback
     ```
   - Replace `your_client_id` and `your_client_secret` in the script.

---

## 🎮 How It Works
1. **Run the script** and enter your Spotify playlist ID:
   ```sh
   python run.py
   ```

2. The script will **randomly pair songs** and ask you to **choose your favorite** in each matchup.

3. The tournament continues until **all songs are ranked**.

4. **Final ranking** is displayed, and you can choose to **reorder your playlist** on Spotify.

---

## 📌 Example Usage
```
Enter your Spotify playlist ID: 5Y7OYMn7YLCaaRqCovfWrG
Loaded 54 songs. Let's begin the tournament!

Round 1: 54 songs remaining, 27 matchups
1: Live Forever - Oasis
2: Save Me - Ed Sheeran
Choose (1 or 2): 1

Round 2: 27 songs remaining, 13 matchups
...

🎉 The best song in your playlist is: Live Forever - Oasis

Do you want to reorder your playlist based on rankings? (yes/no): yes
✅ Playlist reordered successfully!

Final ranked order:
1. Live Forever - Oasis
2. Save Me - Ed Sheeran
3. ...
```

---

## 🔧 Troubleshooting
- If you get **INVALID_CLIENT** errors:
  - Ensure your **Client ID and Secret** are correct.
  - Make sure your **Redirect URI** is set to `http://localhost:8888/callback` in your Spotify Developer settings.

- If the script **fails to reorder your playlist**:
  - You may have hit **Spotify's rate limit**. Wait a minute and try again.

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

## 🌟 Contributing
If you’d like to **improve** the project, feel free to fork it and submit a **pull request**!

---

Enjoy sorting your playlists the fun way! 🎶🔥

