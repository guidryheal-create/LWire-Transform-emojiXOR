# Emoji Translation Framework (XOR-Based)

An experimental framework that explores emoji “translation” by applying a bitwise XOR operation (`0x20`) to emoji code points.  
The result often produces visually or semantically *reversed* or contrasting symbols, inspired by patterns observed in social media emoji transformations.

## Inspiration

This project is inspired by observations from the following source:

- Instagram Reel:  
  https://www.instagram.com/reel/DJnAEHHyFND/?hl=en

The reel demonstrates a pattern where emojis appear to transform into “opposites” through subtle binary manipulation.

## Core Idea

Unicode emojis are represented by code points (hex values).  
By applying a bitwise XOR with `0x20` to a character’s code point:

```

new_codepoint = original_codepoint ^ 0x20

```

You sometimes get:
- Inverted-looking emojis
- Symbolically opposite emojis
- ASCII-style case flipping behavior (extended concept)

⚠️ **Important note:**  
Most emojis are *not* ASCII. This technique is experimental and works best as a conceptual or artistic transformation rather than a strict reversible cipher.

## How It Works

1. Parse the official `emoji-test.txt` file (from Unicode).
2. Extract:
   - Emoji hex code(s)
   - Rendered emoji character
3. Apply XOR `0x20` to the **first Unicode character** of each emoji.
4. If the transformation results in a meaningful change:
   - Store the transformed emoji and hex value
5. Export the results as a JSON mapping.

## Project Structure

```

.
├── xor_emoji_map.py     # Main script
├── emoji-test.txt       # Unicode emoji list (not included)
├── xor_emoji_map.json   # Generated output
└── README.md

````

## Requirements

- Python 3.8+
- `regex` module (required for grapheme cluster handling)

Install dependencies:

```bash
pip install regex
````

## Usage

1. Download the official Unicode emoji list:

   ```
   https://unicode.org/Public/emoji/latest/emoji-test.txt
   ```

2. Place `emoji-test.txt` in the project root.

3. Run the script:

```bash
python xor_emoji_map.py
```

4. Output:

* `xor_emoji_map.json` — a list of before/after emoji transformations.

Example entry:

```json
{
  "before": { "hex": "1F600", "emoji": "😀" },
  "after":  { "hex": "1F620", "emoji": "😠" }
}
```

*(Results vary depending on Unicode behavior and code point validity.)*

## Limitations & Notes

* XOR is applied only to the **first code point**, not full emoji sequences.
* ZWJ sequences, skin tones, and modifiers are not preserved.
* Some transformations may result in invalid or non-emoji characters.
* This is **not** a secure encoding system — it’s exploratory and artistic.

## Use Cases

* Emoji art & glitch aesthetics
* Experimental encoding / decoding
* Emoji linguistics research
* Fun transformations and curiosities

## License

MIT — do whatever you want, just don’t blame Unicode if it breaks reality.

---

✨ Emoji in, emoji out. Bitwise chaos included.

```
