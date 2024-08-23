with open("books/frankenstein.txt", "r") as f:
    
    text = f.read()
    words = text.split()
    
    dictionary = {}

    for word in words:

        for char in word:
            
            char = char.lower()

            if(dictionary.get(char) == None):
                dictionary[char] = 1

            else:
                dictionary[char] += 1

    print("\n--- Begin report for books/frankenstein.txt ---\n")
    print("Words found in Doc = ", len(words), "\n");

    for key in sorted(dictionary.keys()):

        if(key.isalpha()):
            print("The character ", key, "was found ", dictionary[key], "times")

    print("\n--- End report for books/frankenstein.txt ---\n")

