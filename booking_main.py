# booking_main.py
# BIBLIOMAP – Hash Table + Object-Oriented Programming (Final Version)
# DEPANCHIS Group Project

class Seat:
    """Represents an individual seat in the library."""
    def __init__(self, seat_id):
        self.seat_id = seat_id
        self.occupied = False

    def not_empty(self):
        """Marks the seat as occupied."""
        self.occupied = True

    def make_available(self):
        """Marks the seat as available again."""
        self.occupied = False

    def __str__(self):
        """Visual representation for the map."""
        return " X " if self.occupied else " O "


class Library:
    """Represents a library and its seating map using a hash table."""
    def __init__(self, name, rows, cols):
        self.name = name
        self.rows = rows
        self.cols = cols
        self.seats = {}
        for r in range(rows):
            for c in range(cols):
                seat_id = f"{chr(65 + r)}{c + 1}"  # e.g., A1, A2, B1...
                self.seats[seat_id] = Seat(seat_id)

    def display_map(self):
        """Displays a simple seating map."""
        print(f"\n🗺️  {self.name} – Seating Arrangement:\n")
        for r in range(self.rows):
            row_display = ""
            for c in range(self.cols):
                seat_id = f"{chr(65 + r)}{c + 1}"
                row_display += str(self.seats[seat_id])
            print(f"Row {chr(65 + r)} |{row_display}|")
        print("\nLegend: O = Available   X = Occupied\n")

    def book_seat(self, seat_id):
        """Books a seat if available."""
        seat_id = seat_id.upper().strip()
        if seat_id not in self.seats:
            return f"⚠️ '{seat_id}' is not a valid seat ID. Please check the map and try again."
        seat = self.seats[seat_id]
        if seat.occupied:
            return f"❌ Seat {seat_id} is already taken. Choose another one."
        seat.not_empty()
        return f"✅ Seat {seat_id} successfully booked!"

    def cancel_seat(self, seat_id):
        """Cancels a booked seat (makes it available again)."""
        seat_id = seat_id.upper().strip()
        if seat_id not in self.seats:
            return f"⚠️ '{seat_id}' is not a valid seat ID."
        seat = self.seats[seat_id]
        if not seat.occupied:
            return f"⚠️ Seat {seat_id} is not currently booked."
        seat.make_available()
        return f"🪑 Seat {seat_id} booking has been cancelled."

    def finish_study(self, seat_id):
        """Marks a seat as free again when the user finishes studying."""
        seat_id = seat_id.upper().strip()
        if seat_id not in self.seats:
            return f"⚠️ '{seat_id}' is not a valid seat ID."
        seat = self.seats[seat_id]
        if not seat.occupied:
            return f"⚠️ Seat {seat_id} is already available."
        seat.make_available()
        return f"✅ Seat {seat_id} is now available again. See you next time!"


class BibliomapApp:
    """Main app that manages multiple libraries."""
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
        """Main program loop."""
        print("📚 Welcome to BIBLIOMAP – Library Seat Booking System")
        print("-----------------------------------------------------")

        while True:
            print("\n🏛️  Choose a library:")
            for key, lib in self.libraries.items():
                print(f" {key}. {lib.name}")
            print(" 11. Exit")

            choice = input("Enter the number of the library you want to access (1–11): ").strip()

            if choice in self.libraries:
                self.manage_library(self.libraries[choice])
            elif choice == "11":
                print("👋 Thank you for using Bibliomap! Have a productive study session.")
                break
            else:
                print("⚠️ Invalid option. Please type a number from 1 to 11.")

    def manage_library(self, library):
        """Handles seat booking, cancelling, and finishing study."""
        while True:
            library.display_map()
            print(f"📍 You are now in {library.name}")
            print("Options:")
            print(" 1. Book a seat")
            print(" 2. Cancel a seat")
            print(" 3. Finish studying (make a seat available again)")
            print(" 4. View the map again")
            print(" 5. Go back to library list")

            action = input("Enter your choice (1–5): ").strip()

            if action == "1":
                seat_id = input("Enter the seat ID to book (e.g., A3): ")
                print(library.book_seat(seat_id))
                next_action = input(
                    "\nWould you like to (1) Cancel a seat, (2) Finish studying, or (3) Continue? "
                )
                if next_action == "1":
                    seat_to_cancel = input("Enter the seat ID to cancel: ")
                    print(library.cancel_seat(seat_to_cancel))
                elif next_action == "2":
                    seat_to_free = input("Enter the seat ID of the seat you're freeing: ")
                    print(library.finish_study(seat_to_free))
                input("\nPress Enter to continue...")

            elif action == "2":
                seat_id = input("Enter the seat ID to cancel (e.g., B2): ")
                print(library.cancel_seat(seat_id))
                input("\nPress Enter to continue...")

            elif action == "3":
                seat_id = input("Enter the seat ID of the seat you finished using: ")
                print(library.finish_study(seat_id))
                input("\nPress Enter to continue...")

            elif action == "4":
                continue

            elif action == "5":
                print("↩️  Returning to the library selection...")
                break

            else:
                print("⚠️ Invalid choice. Please type a number between 1 and 5.")


# ✅ Program entry point
if __name__ == "__main__":
    app = BibliomapApp()
    app.start()
