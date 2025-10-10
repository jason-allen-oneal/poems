import json
import os

INPUT_FILE = "darkforum_full.jsonl"
OUTPUT_DIR = "parsed_entries"

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(INPUT_FILE, "r", encoding="utf-8") as infile:
        for i, line in enumerate(infile, start=1):
            try:
                entry = json.loads(line.strip())
            except json.JSONDecodeError as e:
                print(f"[!] Skipping invalid JSON line {i}: {e}")
                continue

            # Build readable text output
            content = []
            for key, value in entry.items():
                content.append(f"{key.upper()}:\n{value}\n")

            # Create an output file (001.txt, 002.txt, etc.)
            filename = os.path.join(OUTPUT_DIR, f"entry_{i:04d}.txt")
            with open(filename, "w", encoding="utf-8") as outfile:
                outfile.write("\n".join(content))

            print(f"[+] Wrote {filename}")

    print(f"\nAll done. Files saved to: {os.path.abspath(OUTPUT_DIR)}")

if __name__ == "__main__":
    main()
