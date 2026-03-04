import os

target_file = r"c:\Users\Administrator\Desktop\CDR\main.py"
with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if 'elif choice == "Ð\xa0ÑƒÑ\xa0Ñ\x81\xa0ÐºÐ¸Ð¹":' in line or 'i18n.set_lang("ru")' in line:
        continue
    new_lines.append(line)

with open(target_file, "w", encoding="utf-8") as f:
    f.writelines(new_lines)
print("Cleanup complete.")
