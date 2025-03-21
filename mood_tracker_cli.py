import json
import os
from datetime import datetime, timedelta

MOOD_FILE = "mood_data.json"

def load_data():
    if not os.path.exists(MOOD_FILE):
        return []
    with open(MOOD_FILE, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(MOOD_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_mood():
    mood = input("How are you feeling today? ").strip()
    note = input("Any note you'd like to add? (press Enter to skip): ").strip()
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "mood": mood,
        "note": note
    }
    data = load_data()
    data.append(entry)
    save_data(data)
    print("Mood saved successfully!")

def show_history(days=7):
    data = load_data()
    if not data:
        print("No mood data available.")
        return

    print(f"\\nMood History (last {days} days):")
    cutoff = datetime.now() - timedelta(days=days)
    for entry in data:
        entry_date = datetime.strptime(entry['date'], "%Y-%m-%d")
        if entry_date >= cutoff:
            print(f"{entry['date']} - {entry['mood']} - {entry['note']}")

def export_data():
    data = load_data()
    with open("mood_export.csv", 'w') as file:
        file.write("Date,Mood,Note\\n")
        for entry in data:
            file.write(f"{entry['date']},{entry['mood']},{entry['note']}\\n")
    print("Data exported to mood_export.csv")

def menu():
    while True:
        print("\\nMood Tracker")
        print("1. Add today's mood")
        print("2. Show mood history (7 days)")
        print("3. Show mood history (30 days)")
        print("4. Export mood history")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            add_mood()
        elif choice == '2':
            show_history(7)
        elif choice == '3':
            show_history(30)
        elif choice == '4':
            export_data()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    menu()
