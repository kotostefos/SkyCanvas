from datetime import datetime, timezone

from skyfield.api import load, wgs84
from config import LOCATION_NAME, LATITUDE, LONGITUDE

def get_sky_position():

    print("🌌 SkyCanvas Sky Engine")

    latitude = LATITUDE
    longitude = LONGITUDE

    print("\nLocation:")
    print(LOCATION_NAME)

    print("\nLoading astronomical database...")

    planets = load('de421.bsp')
    earth = planets['earth']
    moon = planets['moon']

    # Current time
    ts = load.timescale()
    now = ts.now()

    # Observer location
    observer = earth + wgs84.latlon(
        latitude,
        longitude
    )

    # Moon position
    moon_position = observer.at(now).observe(moon)

    altitude, azimuth, distance = moon_position.apparent().altaz()

    print("\nMoon 🌙")
    print(f"Altitude: {altitude.degrees:.2f}°")
    print(f"Azimuth: {azimuth.degrees:.2f}°")
    print(f"Distance: {distance.km:.0f} km")

    # Sun position
    sun = planets['sun']

    sun_position = observer.at(now).observe(sun)

    sun_altitude, sun_azimuth, sun_distance = (
        sun_position.apparent().altaz()
    )

    print("\nSun ☀️")
    print(f"Altitude: {sun_altitude.degrees:.2f}°")
    print(f"Azimuth: {sun_azimuth.degrees:.2f}°")

    if sun_altitude.degrees > 0:
        print("Status: Daylight")
    else:
        print("Status: Night")

        # Planet positions
    print("\nPlanets 🪐")

    planet_names = [
        "mercury",
        "venus",
        "mars",
        "jupiter barycenter",
        "saturn barycenter"
    ]

    for planet_name in planet_names:
        planet = planets[planet_name]

        planet_position = observer.at(now).observe(planet)

        altitude, azimuth, distance = (
            planet_position.apparent().altaz()
        )

        print(f"\n{planet_name.title()}")
        print(f"Altitude: {altitude.degrees:.2f}°")
        print(f"Azimuth: {azimuth.degrees:.2f}°")

if __name__ == "__main__":
    get_sky_position()