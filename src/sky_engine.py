from datetime import datetime, timezone

from skyfield.api import load, wgs84


def get_sky_position():

    print("🌌 SkyCanvas Sky Engine")

    # Brussels coordinates
    latitude = 50.8503
    longitude = 4.3517

    print("\nLocation:")
    print("Brussels, Belgium")

    # Load astronomy data
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


if __name__ == "__main__":
    get_sky_position()