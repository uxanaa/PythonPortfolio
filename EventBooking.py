class EventBooking:
    """A class representing a standard event booking."""
    
    def __init__(self, base_price, attendees, venue_name):
        """Initialisation of an EventBooking class, requiring a base_price (float), attendees (int/float), and venue_name (string)."""
        if base_price <= 0 or attendees <= 0:
            raise ValueError("Price and attendees must be positive")
        
        self.base_price = float(base_price)
        self.attendees = float(attendees)
        self.venue_name = venue_name

    def total_cost(self):
        """Calculate the total cost of the booking."""
        return self.base_price * self.attendees

    def update_price(self, new_price):
        """Update the base price per attendee."""
        if new_price <= 0:
            raise ValueError("New price must be positive")
        self.base_price = float(new_price)

# Implement the CorporateEvent class here
class CorporateEvent(EventBooking):
    """A subclass of EventBooking that adds corporate-specific features."""

    def __init__(self, base_price, attendees, venue_name, catering_fee=300.0):
        super().__init__(base_price, attendees, venue_name)

        if catering_fee < 0:
            raise ValueError("Catering fee must be non-negative")

        self.catering_fee = float(catering_fee)

    def apply_member_discount(self, rate):
        """Apply a discount to the base price per attendee."""
        if rate < 0:
            raise ValueError("Discount rate cannot be negative")

        # Reduce the stored base price, but never below zero
        self.base_price = max(0.0, self.base_price * (1 - rate))

    def total_cost(self):
        """Calculate total cost including catering."""
        base_cost = super().total_cost()
        return float(base_cost + self.catering_fee)

if __name__ == "__main__":
    # Some tests for yourself, just for you to check the output!
    # These are not graded as part of your output.

    # 1. Test Base Class (EventBooking)
    booking = EventBooking(base_price=50, attendees=10, venue_name="Venue A")
    print(booking.total_cost())  # Expected: 50 * 10 = 500.0

    # 2. Test Subclass Init & Base Cost
    corp_event = CorporateEvent(base_price=100, attendees=5, venue_name="Venue B", catering_fee=50)
    # Expected: (100 * 5) + 50 = 550.0
    print(corp_event.total_cost())

    # 3. Test Discount Application
    corp_event.apply_member_discount(0.2) # Base price changes from 100 to 80
    # Expected: (80 * 5) + 50 = 450.0
    print(corp_event.total_cost())

    # 4. Test Price Update
    corp_event.update_price(120) # Base price changes from 80 to 120
    # Expected: (120 * 5) + 50 = 650.0
    print(corp_event.total_cost())