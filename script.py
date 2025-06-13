from collections import defaultdict
import re

# Read TikTok links from file
with open("tiktoks.txt", "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file if line.strip()]

# Group by username
videos_by_user = defaultdict(list)

# Extract username and video ID from each line
pattern = re.compile(r"tiktok\.com/@([^/]+)/video/(\d+)")

for url in lines:
    match = pattern.search(url)
    if match:
        username = match.group(1)
        video_id = int(match.group(2))
        videos_by_user[username].append((video_id, url))
    else:
        videos_by_user["unknown"].append((0, url))  # fallback for invalid lines

# Write output
with open("sorted_tiktoks.txt", "w", encoding="utf-8") as outfile:
    for user in sorted(videos_by_user.keys()):
        sorted_videos = sorted(videos_by_user[user], key=lambda x: x[0])
        count = len(sorted_videos)
        outfile.write(f"---- @{user} ({count} Videos) ----\n\n")
        for _, url in sorted_videos:
            outfile.write(url + "\n")
        outfile.write("\n")
