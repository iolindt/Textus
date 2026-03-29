print("Hello! This is a sample project: Text Analyzer")
print("1 - Count words")
print("2 - Uppercase")
choice = input("Choose: ")

text = input("Enter text: ")

if choice == "1":
    print("Words:", len(text.split()))
elif choice == "2":
    print(text.upper())
