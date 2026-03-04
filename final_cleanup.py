import os

target_file = r"c:\Users\Administrator\Desktop\CDR\main.py"
with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if 'elif choice == "Ð\xa0ÑƒÑ\xa0Ñ\x81\xa0ÐºÐ¸Ð¹":' in line:
        continue
    if 'corner_radius=15, border_width=2,' in line and 'fg_color="#0d0d0d",' in line:
        line = line.replace('corner_radius=15, border_width=2,', 'bg_color="transparent", corner_radius=15, border_width=2,')
    new_lines.append(line)

with open(target_file, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("Final cleanup complete.")
