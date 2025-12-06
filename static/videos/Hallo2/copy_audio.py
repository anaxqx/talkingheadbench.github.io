import os
import subprocess

video_dir = "/playpen-nas-ssd3/anaxxq/GitHub/user_study_subset/Hallo2"
audio_dir = "/playpen-nas-ssd4/dataset/CelebV-HQ/audio"
output_dir = "/playpen-nas-ssd3/anaxxq/GitHub/user_study_subset/Hallo2_with_audio"
os.makedirs(output_dir, exist_ok=True)

for fname in os.listdir(video_dir):
    if not fname.endswith(".mp4"):
        continue
    
    stem = fname.split(".mp4")[0]
    try:
        audio_id = stem.split("---")[1].split("_H")[0]
    except:
        print("skip", fname)
        continue

    audio_path = os.path.join(audio_dir, f"{audio_id}.wav")
    video_path = os.path.join(video_dir, fname)
    out_path = os.path.join(output_dir, fname)

    if not os.path.exists(audio_path):
        print("Missing audio:", audio_path)
        continue
    
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",     # no re-encode
        "-c:a", "aac",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-shortest",
        out_path
    ]
    
    subprocess.run(cmd)
