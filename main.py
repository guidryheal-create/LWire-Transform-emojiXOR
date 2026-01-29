# xor_emoji_map.py

import regex
import json

XOR_KEY = 0x20

# Regex to capture:
# 1. The hex code(s) at the start
# 2. The actual emoji in the comment
pattern = regex.compile(r"^(?P<hex>[0-9A-F ]+)\s*;.*#\s*(?P<emoji>\X)")

# Load emoji-test.txt and build initial emoji map
emoji_map = {}
with open("emoji-test.txt", encoding="utf-8") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            hex_code = match.group("hex").strip()
            emoji_char = match.group("emoji")
            emoji_map[hex_code] = emoji_char

# XOR function (works on single characters)
def xor_0x20(char: str) -> str:
    code = ord(char)
    
    return chr(code ^ XOR_KEY)

# Transform the emoji map into a before/after JSON
xor_emoji_list = []

for hex_code, emoji_char in emoji_map.items():
    # For demonstration, XOR on the **first character of emoji** if it's in ASCII range
    first_char = emoji_char[0]
    transformed_char = xor_0x20(first_char)

    # Reconstruct after emoji:
    # If XOR didn't change the character (non-ASCII), leave as original
    after_emoji = transformed_char if transformed_char != first_char else emoji_char
    after_hex = f"{ord(after_emoji):X}" if after_emoji != emoji_char else hex_code

    xor_emoji_list.append({
        "before": {"hex": hex_code, "emoji": emoji_char},
        "after": {"hex": after_hex, "emoji": after_emoji}
    })

# Save JSON
with open("xor_emoji_map.json", "w", encoding="utf-8") as out_file:
    json.dump(xor_emoji_list, out_file, ensure_ascii=False, indent=2)

print(f"✅ XOR emoji map JSON created with {len(xor_emoji_list)} entries.")
