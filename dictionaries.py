print('<<<<< WELCOME TO MY IGBO LANGUAGE DICTIONARY >>>>>')
print("You can translate from English to Igbo or Igbo to English")

# Dictionary with 20 Igbo words and their English meanings
igbo_to_english_dict = {
    "bia": "come",
    "do nana": "sit down",
    "kedu": "how are you",
    "ụtụtụ ọma": "good morning",
    "daalụ": "thank you",
    "ka ọ dị": "goodbye",
    "nnọọ": "welcome",
    "kedu aha gị": "what is your name",
    "aha m bụ": "my name is",
    "mmiri": "water",
    "nri": "food",
    "nwa": "child",
    "nne": "mother",
    "nna": "father",
    "ụlọ": "house",
    "ego": "money",
    "ahịa": "market",
    "biko": "please",
    "ndo": "sorry",
    "ka anyị laa": "let's go"
}

# Create the reverse dictionary for English to Igbo
english_to_igbo_dict = {v: k for k, v in igbo_to_english_dict.items()}

print(f"\n📚 Dictionary contains {len(igbo_to_english_dict)} words/phrases")
print("-" * 50)

while True:
    print("\n" + "=" * 50)
    print("TRANSLATION OPTIONS:")
    print("1. English → Igbo")
    print("2. Igbo → English")
    print("3. Show all words")
    print("4. Quit")
    print("=" * 50)

    choice = input("\nChoose option (1-4): ").strip()

    # QUIT
    if choice == '4':
        print("\nDaalụ! (Thank you!) Ka ọ dị! (Goodbye!)")
        break

    # SHOW ALL WORDS
    elif choice == '3':
        print("\n" + "=" * 50)
        print("ALL WORDS IN DICTIONARY:")
        print("=" * 50)
        print("\nENGLISH → IGBO:")
        print("-" * 30)
        for i, (eng, igbo) in enumerate(sorted(english_to_igbo_dict.items()), 1):
            print(f"{i:2}. {eng:20} → {igbo}")

        print("\nIGBO → ENGLISH:")
        print("-" * 30)
        for i, (igbo, eng) in enumerate(sorted(igbo_to_english_dict.items()), 1):
            print(f"{i:2}. {igbo:20} → {eng}")
        continue

    # ENGLISH TO IGBO
    elif choice == '1':
        word = input("\nEnter English word/phrase: ").strip().lower()
        if word in english_to_igbo_dict:
            print(f"\n✓ Translation: '{word}' → '{english_to_igbo_dict[word]}'")
        else:
            print(f"\n✗ '{word}' not found in dictionary")
            # Show similar words
            suggestions = [w for w in english_to_igbo_dict.keys() if word in w or w.startswith(word[:2])]
            if suggestions:
                print(f"   Did you mean: {', '.join(suggestions[:3])}?")

    # IGBO TO ENGLISH
    elif choice == '2':
        word = input("\nEnter Igbo word/phrase: ").strip().lower()
        if word in igbo_to_english_dict:
            print(f"\n✓ Translation: '{word}' → '{igbo_to_english_dict[word]}'")
        else:
            print(f"\n✗ '{word}' not found in dictionary")
            # Show similar words
            suggestions = [w for w in igbo_to_english_dict.keys() if word in w or w.startswith(word[:2])]
            if suggestions:
                print(f"   Did you mean: {', '.join(suggestions[:3])}?")

    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")