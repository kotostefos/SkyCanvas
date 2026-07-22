from datetime import datetime
from skyfield.api import load, Topos


def get_sky_position():
    print("🌌 SkyCanvas Sky Engine started")

    # Location: Brussels
    latitude = 50.8503
    longitude = 4.3517

    print(f"Location: Brussels")
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")

    now = datetime.now()

    print(f"Date and time: {now}")

    print("Astronomy engine ready!")


if __name__ == "__main__":
    get_sky_position()