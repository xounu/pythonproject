calendar = {
    "S3": {},
    "S5": {},
    "S7": {}
}
def add_event():
    semester = input("Enter semester (S3/S5/S7): ").upper()
    if semester not in calendar:
        print(" Invalid semester. Please enter S3, S5, or S7.")
        return

    month = input("Enter the month (e.g., August): ").title()
    date = input("Enter the date (e.g., 24): ")
    event = input("Enter the event name (e.g., Midterm Exam): ")

    if month not in calendar[semester]:
     calendar[semester][month] = []

    calendar[semester][month].append({"date": date, "event": event})
    print(f" Event added to {semester}: {event} on {date} {month}")

def show_calendar():
    print("\n Semester Calendar:")
    for semester in calendar:
        print(f"\n🎓 {semester}")
        for month in calendar[semester]:
            print(f" {month}:")
            for entry in sorted(calendar[semester][month], key=lambda x: int(x['date'])):
                print(f"    - {entry['date']}: {entry['event']}")

def load_predefined_events():
    calendar["S3"] = {
        "July": [
           {"date": "01", "event": "Commencement of classes"},
            {"date": "07", "event": "Semester Enrollment Begins"},
            {"date": "14", "event": "Semester Enrollment ends"},
            {"date": "16", "event": "First Advisory Meeting Deadline"},
            {"date": "18", "event": "Course Selection Begins"},
            {"date": "30", "event": "Course Selection Ends"}
        ],
        "August": [
           {"date": "23", "event": "First Series Exam Completion"},
            {"date": "25", "event": "Mid Term Survey"}
        ],
        "September": [
            {"date": "09", "event": "Second Advisory Meeting Deadline"},
            {"date": "11", "event": "First Internal Audit Completion"}
        ],
        "October": [
            {"date": "15", "event": "Second Series Test Completion"},
            {"date": "16", "event": "KTU Survey (2)"},
            {"date": "18", "event": "Annual Sports Meet"},
            {"date": "21", "event": "End Semester Feedback"},
            {"date": "23", "event": "Class Ends & IA Marks Published"},
            {"date": "24", "event": "Attendance Entry Deadline"},
            {"date": "27", "event": "Lab Exams Begin"},
            {"date": "29", "event": "Internal Marks Entry Deadline"}
        ],
        "November": [
            {"date": "03", "event": "Correction Deadline (No Fine)"},
            {"date": "12", "event": "End Semester Exam Begins"},
            {"date": "19", "event": "University Valuation Camp Starts"}
        ]
    }

    calendar["S5"] = calendar["S3"].copy()
    calendar["S7"] = calendar["S3"].copy()
load_predefined_events()
while True:
    print("\nChoose an option:")
    print("1. Add an event")
    print("2. Show calendar")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_event()
    elif choice == "2":
        show_calendar()
    elif choice == "3":
        print(" Exiting. Good luck with your semester!")
        break
    else:
        print(" Invalid choice. Try again.")