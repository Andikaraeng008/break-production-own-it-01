import os

TEXT = "I replaced the production config with my test config. It worked perfectly \u2014 in test."

def main():
    assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "gate: 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
