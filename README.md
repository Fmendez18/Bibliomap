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
BIBLIOMAP is a web app built to help university students in Madrid quickly find and reserve library study seats in real time. Instead of wasting time walking to a full library, students can check live availability, pick a time slot and seat type, and confirm a reservation, directly from their phone or laptop. Libraries benefit from smoother demand management and simple usage insights. So far, the algorithm uses `Seat`, Safety and Price range as attributes for determining the ideal neighbourhood.

## User Journey 
1. **Access & Preferences:** The student opens the web app, selects a library, and desired time window.
2. **Availability & Ranking:** BIBLIOMAP fetches **real-time seat availability** surfacing the **best options first**.
3. **Reserve & Confirm:** The student chooses a seat and confirms; the system **books the seat** and shows confirmation details.
4. **Use the Seat → Cancel/Release on Exit:** When the student finishes early or leaves, they **tap “Cancel/Release”** to free the seat immediately for others. 
5. **Manage & Iterate:** Users can modify/cancel reservations and **re-run the search** to get new matches.
6. **Premium (optional):** Students can **upgrade** to unlock premium features (e.g., priority booking windows, multi-slot reservations, advanced filters).

## Why it’s useful
- **Save time:** Know availability before you go.  
- **Peace of mind:** Guaranteed spot with reminders reduces stress.  
- **Better operations:** Libraries use insights to balance demand and improve experience.

## Limitations
- **Library cooperation:** Real libraries may not share data or allow integrations.  
- **Adoption by students:** Even if the system works, habit change can be slow.  
- **Infrastructure limits:** Wi-Fi, server outages, or app-store policies could block usage.
- 
# Installation of the project

This project is supposed to be ran on the terminal of the computer

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
python code_bibliomap.py
```

# Further improvements
1. Create a user identification option, so that the user can not book multiple seats per day.
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
