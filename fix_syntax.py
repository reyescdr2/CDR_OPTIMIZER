import os

target_file = r"c:\Users\Administrator\Desktop\CDR\main.py"
with open(target_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Line 1379 from view_file (index 1378)
if 'elif choice == "Ð' in lines[1378]:
    del lines[1378]
    with open(target_file, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("Syntax error fixed.")
else:
    print(f"Line 1378 was not what we expected: {repr(lines[1378])}")
