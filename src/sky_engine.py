from datetime import datetime, timezone

from skyfield.api import load, wgs84, Star
from skyfield.data import hipparcos
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

    # Load star catalogue ⭐

    with load.open(hipparcos.URL) as f:
        stars = hipparcos.load_dataframe(f)

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

    moon_altitude, moon_azimuth, moon_distance = (
    moon_position.apparent().altaz()
)
    print("\nMoon 🌙")
    print(f"Altitude: {moon_altitude.degrees:.2f}°")
    print(f"Azimuth: {moon_azimuth.degrees:.2f}°")
    print(f"Distance: {moon_distance.km:.0f} km")

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

    # Star positions ⭐

    print("\nStars ⭐")

    bright_stars = {
        "Sirius": 32349,
        "Betelgeuse": 27989,
        "Rigel": 24436,
        "Vega": 91262,
        "Polaris": 11767
    }

    star_positions = []

    for star_name, hip_id in bright_stars.items():

        star_data = stars.loc[hip_id]

        star = Star(
        ra_hours=star_data["ra_hours"],
        dec_degrees=star_data["dec_degrees"]
        )

        star_position = observer.at(now).observe(star)

        altitude, azimuth, distance = (
            star_position.apparent().altaz()
        )

        print(f"\n{star_name}")
        print(f"Altitude: {altitude.degrees:.2f}°")
        print(f"Azimuth: {azimuth.degrees:.2f}°")


        star_positions.append(
            {
                "name": star_name,
                "altitude": float(altitude.degrees),
                "azimuth": float(azimuth.degrees)
            }
        )

    # Planet positions
    print("\nPlanets 🪐")

    planet_positions = []

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
        planet_positions.append(
        {
        "name": planet_name,
        "altitude": float(altitude.degrees),
        "azimuth": float(azimuth.degrees)
        }
    )

    return {
    "moon_altitude": float(moon_altitude.degrees),
    "moon_azimuth": float(moon_azimuth.degrees),

    "sun_altitude": float(sun_altitude.degrees),
    "sun_azimuth": float(sun_azimuth.degrees),

    "planets": planet_positions,
    "stars": star_positions
}

if __name__ == "__main__":
    sky = get_sky_position()
    print(sky)