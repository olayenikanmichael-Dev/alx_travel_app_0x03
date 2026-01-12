from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        listings_data = [
            {
                "title": "Luxury Beach Resort",
                "description": "A beautiful beach resort with ocean views.",
                "location": "Lagos, Nigeria",
                "price_per_night": 150.00,
            },
            {
                "title": "Mountain Cabin Retreat",
                "description": "A peaceful cabin in the mountains.",
                "location": "Jos, Nigeria",
                "price_per_night": 90.00,
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the city center.",
                "location": "Abuja, Nigeria",
                "price_per_night": 120.00,
            },
        ]

        for data in listings_data:
            Listing.objects.create(**data)

        self.stdout.write(
            self.style.SUCCESS("Database seeded successfully!")
        )
