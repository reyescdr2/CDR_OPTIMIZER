
import os

filepath = 'c:/Users/Administrator/Desktop/CDR/main.py'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    new_lines.append(line)
    if 'self.save_config()' in line and 'change_lang' in ''.join(lines[max(0, new_lines.index(line)-20):new_lines.index(line)]):
        # Add the closing logic after save_config in change_lang
        indent = line[:line.find('self.save_config()')]
        new_lines.append(f"\n{indent}# Close the picker after selection\n")
        new_lines.append(f"{indent}if hasattr(self, 'lang_picker_frame') and self.lang_picker_frame:\n")
        new_lines.append(f"{indent}    self.lang_picker_frame.destroy()\n")
        new_lines.append(f"{indent}    self.lang_picker_frame = None\n")

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print("Update successful")
