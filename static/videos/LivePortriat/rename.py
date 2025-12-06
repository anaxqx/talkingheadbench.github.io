import os

def rename_mp4_files_with_hallo():
    for filename in os.listdir('.'):
        if filename.endswith('.mp4') and not filename.endswith('_Hallo.mp4'):
            base, ext = os.path.splitext(filename)
            new_name = f"{base}_LivePortrait{ext}"
            os.rename(filename, new_name)
            print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    rename_mp4_files_with_hallo()
