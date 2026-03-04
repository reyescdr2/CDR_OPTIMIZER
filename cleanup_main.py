
import os

filepath = 'c:/Users/Administrator/Desktop/CDR/main.py'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# We want to remove the lines that start with '            values=[' up to the empty line before '        self.audio_on = False'
# From our previous view_file, these were around index 637-639 (0-indexed).
# Let's be safer and find them by content.

new_lines = []
skip = False
for line in lines:
    if 'values=["Español"' in line:
        skip = True
        continue
    if skip and 'self.audio_on = False' in line:
        skip = False
    
    if not skip:
        # Also fix the weird whitespace/dangling lines if any
        if 'values=' in line and 'Español' in line: # double check
            continue
        new_lines.append(line)

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print("Cleanup successful")
