# Bibliomap
Application designed to view the availability of IE University's libraries

# Table of Contents
1. [Introduction](#introduction)
2. [Installation of the project](#installation-of-the-project)
3. [Usage](#usage)
4. [Further improvements](#further-improvements)
5. [Credits](#credits)

---

# Introduction
BIBLIOMAP is a web app built to help university students in Madrid quickly find and reserve library study seats in real time. Instead of wasting time walking to a full library, students can check live availability, pick a time slot and seat type, and confirm a reservation, directly from their phone or laptop. Libraries benefit from smoother demand management and simple usage insights. To achieve this, the algorithm uses `Seat`, `Library` and `BibliomapApp` range as Classes for determining the ideal output.

## User Journey 

**Overview**

The user opens the Bibliomap web app and is presented with a list of available libraries. After selecting a library, the system displays a seating map with rows and columns that indicate seat availability.

Legend:
`O` = Available
`X` = Occupied

The user can then choose one of the available actions from the main options menu (5):

**1. Book a Seat**

The system prompts for a Seat ID (e.g., A3) and the number of hours the student plans to study.

Then, a confirmation message appears. If the seat ID is invalid, the system shows a warning.

After booking (or error handling), the system offers the following options:
- Cancel a seat
- Finish studying (make a seat available again)
- Exit Bibliomap
- Continue

**2. Cancel a Seat**

The system asks for the Seat ID to cancel.

Upon confirmation, the system releases the seat and displays a message confirming that the seat has been successfully canceled.

**3. Finish Studying**

The system asks for the Seat ID.

Once confirmed, the system updates the seating map to mark the seat as available again (O).

**4. View the Map Again**

The user can select “View the Map Again” to see the seating map again.

**5. Go Back to Library List**

Returns to the initial screen showing the list of all libraries.
From there, they can select a different library to view its seating arrangement or exit the app.

## Why it’s useful
- **Save time:** Know availability before you go.  
- **Peace of mind:** Guaranteed spot with reminders reduces stress.  
- **Better operations:** Libraries use insights to balance demand and improve experience.

## Limitations
- **Library cooperation:** Real libraries may not share data or allow integrations.  
- **Adoption by students:** Even if the system works, habit change can be slow.  
- **Infrastructure limits:** Wi-Fi, server outages, or app-store policies could block usage.
  
# Installation of the project

This project is supposed to be ran on the terminal of the computer

#### Preliminary phase:

Download python (if not installed already)

```bash

https://www.python.org/downloads/release/python-3139/  

```

#### 1. Clone the repository
```bash
git clone https://github.com/Fmendez18/Bibliomap.git
```
```bash
cd Bibliomap
```
```bash
python3 -m venv ./venv
```
```bash
source ./venv/bin/activate   # macOS/Linux
venv\Scripts\activate        # Windows
```

# Usage
```bash
python booking_main.py
```

# Further improvements
1. Create a user identification option, so that the user cannot book multiple seats per day.
2. Limit the amount of hours the user can book per day.
3. Add function that, after the study-time desired has passed, liberates the seat that user had booked, without them having to visit the app again to state they have left.

# Credits
This project was created for our **Algorithms and Data Structures** course at **IE University**.  
The project was created by:

- Karim Junadi
- Santiago Landínez
- Carolina Leyenda
- Zoe Mekin
- Federico Méndez
- Carla Palmés
- Sofía Paparo
- Candela Muñoz
