import json
import datetime
from collections import Counter

# File to store moods
MOOD_FILE = "mood_data.json"

# Load existing mood data
def load_moods():
    try:
        with open(MOOD_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save mood data
def save_moods(data):
    with open(MOOD_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add today's mood with emoji support
def add_mood():
    moods = load_moods()
    print("\n😊 How are you feeling today? Choose one:")
    print("1️⃣ Happy 😊 | 2️⃣ Sad 😢 | 3️⃣ Angry 😡 | 4️⃣ Excited 🤩 | 5️⃣ Tired 😴")
    mood_choices = {"1": "😊", "2": "😢", "3": "😡", "4": "🤩", "5": "😴"}
    
    choice = input("Enter a number (1-5): ").strip()
    mood = mood_choices.get(choice, "😐")  # Default: neutral if wrong input

    note = input("📝 Add a short note (optional): ").strip()

    # Save entry
    entry = {"date": datetime.date.today().isoformat(), "mood": mood, "note": note}
    moods.append(entry)
    save_moods(moods)
    
    print(f"\n✅ Mood saved! Today, you feel: {mood}")

# Show mood history (Last X days)
def show_history(days):
    moods = load_moods()
    cutoff_date = datetime.date.today() - datetime.timedelta(days=days)
    
    print(f"\n📅 Mood History (Last {days} days):")
    for entry in moods:
        entry_date = datetime.date.fromisoformat(entry["date"])
        if entry_date >= cutoff_date:
            print(f"📆 {entry['date']} - Mood: {entry['mood']} - Note: {entry['note']}")
    
    if not moods:
        print("❌ No mood records found.")

# Show mood statistics
def mood_statistics():
    moods = load_moods()
    mood_counts = Counter(entry["mood"] for entry in moods)

    print("\n📊 Mood Statistics:")
    for mood, count in mood_counts.items():
        print(f"{mood}: {count} times")

# Search past moods by date
def search_mood():
    moods = load_moods()
    search_date = input("\n🔍 Enter date to search (YYYY-MM-DD): ").strip()
    
    found = [entry for entry in moods if entry["date"] == search_date]

    if found:
        print("\n📆 Mood on that date:")
        for entry in found:
            print(f"🗓️ {entry['date']} - Mood: {entry['mood']} - Note: {entry['note']}")
    else:
        print("❌ No mood records found for this date.")

# Export mood history to CSV
def export_data():
    moods = load_moods()
    with open("mood_export.csv", "w") as file:
        file.write("Date,Mood,Note\n")
        for entry in moods:
            file.write(f"{entry['date']},{entry['mood']},{entry['note']}\n")
    print("\n✅ Data exported to mood_export.csv")

# Main menu
def menu():
    while True:
        print("\n📖 Mood Tracker Menu:")
        print("1️⃣ Add today's mood")
        print("2️⃣ Show mood history (7 days)")
        print("3️⃣ Show mood history (30 days)")
        print("4️⃣ View mood statistics")
        print("5️⃣ Search past moods")
        print("6️⃣ Export mood history")
        print("7️⃣ Exit")

        choice = input("\n🔹 Choose an option (1-7): ").strip()

        if choice == "1":
            add_mood()
        elif choice == "2":
            show_history(7)
        elif choice == "3":
            show_history(30)
        elif choice == "4":
            mood_statistics()
        elif choice == "5":
            search_mood()
        elif choice == "6":
            export_data()
        elif choice == "7":
            print("\n👋 Goodbye! See you next time!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1-7.")

# Run the menu
if __name__ == "__main__":
    menu()
