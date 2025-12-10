# booking_main.py
# BIBLIOMAP – Hash Table + Object-Oriented Programming + Greedy Group Booking
# DEPANCHIS Group Project

class Seat:
    def __init__(self, seat_id):
        self.seat_id = seat_id
        self.occupied = False
        self.study_time = None

    def not_empty(self, study_time):
        self.occupied = True
        self.study_time = study_time

    def make_available(self):
        self.occupied = False
        self.study_time = None

    def __str__(self):
        return " X " if self.occupied else " O "


class Library:
    def __init__(self, name, rows, cols):
        self.name = name
        self.rows = rows
        self.cols = cols
        self.seats = {}
        for r in range(rows):
            for c in range(cols):
                seat_id = f"{chr(65 + r)}{c + 1}"
                self.seats[seat_id] = Seat(seat_id)

    def display_map(self):
        print(f"\n🗺️  {self.name} – Seating Arrangement:\n")

        header = "     " + "".join([f" {str(c+1).rjust(2)} " for c in range(self.cols)])
        print(header)
        print("    " + "-" * (len(header) - 4))

        for r in range(self.rows):
            row_display = ""
            for c in range(self.cols):
                seat_id = f"{chr(65 + r)}{c + 1}"
                row_display += str(self.seats[seat_id])
            print(f"Row {chr(65 + r)} |{row_display}|")

        print("\nLegend: O = Available   X = Occupied\n")

    def book_seat(self, seat_id, study_time):
        seat_id = seat_id.upper().strip()
        if seat_id not in self.seats:
            return f"⚠️ '{seat_id}' is not a valid seat ID."
        seat = self.seats[seat_id]
        if seat.occupied:
            return f"❌ Seat {seat_id} is already taken."
        seat.not_empty(study_time)
        return f"✅ Seat {seat_id} successfully booked for {study_time} hours!"

    def cancel_seat(self, seat_id):
        seat_id = seat_id.upper().strip()
        if seat_id not in self.seats:
            return "⚠️ Invalid seat ID."
        seat = self.seats[seat_id]
        if not seat.occupied:
            return f"⚠️ Seat {seat_id} is not currently booked."
        seat.make_available()
        return f"🪑 Seat {seat_id} booking has been cancelled."

    def finish_study(self, seat_id):
        seat_id = seat_id.upper().strip()
        if seat_id not in self.seats:
            return "⚠️ Invalid seat ID."
        seat = self.seats[seat_id]
        if not seat.occupied:
            return f"⚠️ Seat {seat_id} is already free."
        seat.make_available()
        return f"✅ Seat {seat_id} is now available again."

    # New Addition: Greedy Algorithm
    def greedy_group_booking(self, group_size, study_time):
        available = [s for s in self.seats.values() if not s.occupied]

        if len(available) < group_size:
            return "⚠️ Not enough available seats for your group."

        chosen = []

        for _ in range(group_size):
            best = None
            best_value = None

            for seat in available:
                # Seats with no study_time get a large default value
                time_val = 999 if seat.study_time is None else int(seat.study_time)

                if best_value is None or time_val < best_value:
                    best_value = time_val
                    best = seat

            chosen.append(best)
            available.remove(best)

        # Book all chosen seats
        booked_ids = []
        for seat in chosen:
            seat.not_empty(study_time)
            booked_ids.append(seat.seat_id)

        return f"🎉 Group seats booked: {', '.join(booked_ids)}"


class BibliomapApp:
    def __init__(self):
        self.libraries = {
            "1": Library("Biblioteca IE María de Molina Hub", 3, 4),
            "2": Library("Biblioteca María de Zambrano", 4, 5),
            "3": Library("Biblioteca del Senado", 3, 5),
            "4": Library("Biblioteca Centro de Documentación del Museo Reina Sofía", 2, 6),
            "5": Library("Biblioteca Benito Pérez Galdós", 4, 4),
            "6": Library("Biblioteca Ana María Matute", 3, 6),
            "7": Library("Biblioteca Escuelas Pías", 3, 5),
            "8": Library("Biblioteca del Ateneo", 4, 3),
            "9": Library("Biblioteca Regional de Madrid Joaquín Leguina", 5, 5),
            "10": Library("Biblioteca Carlos III Campus Leganés", 3, 4)
        }

    def start(self):
        print("📚 Welcome to BIBLIOMAP – Library Seat Booking System")
        print("-----------------------------------------------------")

        while True:
            print("\n🏛️ Choose a library:")
            for key, lib in self.libraries.items():
                print(f" {key}. {lib.name}")
            print(" 11. Exit")

            choice = input("Enter your choice: ").strip()

            if choice in self.libraries:
                self.manage_library(self.libraries[choice])
            elif choice == "11":
                print("👋 Goodbye!")
                break
            else:
                print("⚠️ Invalid choice.")

    def manage_library(self, library):
        while True:
            library.display_map()
            print(f"📍 {library.name}")
            print("Options:")
            print(" 1. Book (Individual or Group)")
            print(" 2. Cancel a seat")
            print(" 3. Finish studying")
            print(" 4. View map again")
            print(" 5. Back")

            action = input("Enter your choice: ").strip()

            if action == "1":
                print("\nDo you want to book:")
                print(" 1. An individual seat")
                print(" 2. A group of seats")
                mode = input("Choose 1 or 2: ").strip()

                if mode == "1":
                    seat_id = input("Enter the seat ID (e.g., A1): ")
                    t = input("How many hours?: ")
                    print(library.book_seat(seat_id, t))

                elif mode == "2":
                    group_size = int(input("Group size: "))
                    t = input("How many hours?: ")
                    print(library.greedy_group_booking(group_size, t))

                else:
                    print("⚠️ Invalid option.")

            elif action == "2":
                seat_id = input("Seat to cancel: ")
                print(library.cancel_seat(seat_id))

            elif action == "3":
                seat_id = input("Seat ID you finished using: ")
                print(library.finish_study(seat_id))

            elif action == "4":
                continue

            elif action == "5":
                print("↩️ Returning...")
                break

            else:
                print("⚠️ Invalid choice.")


# Entry point
if __name__ == "__main__":
    app = BibliomapApp()
    app.start()