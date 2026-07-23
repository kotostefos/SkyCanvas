import urllib.request
import json

from config import (
    LOCATION_NAME,
    LATITUDE,
    LONGITUDE
)


def get_location():

    print("📍 Detecting location...")


    try:

        # Internet location service

        url = "https://ipapi.co/json/"

        response = urllib.request.urlopen(
            url,
            timeout=5
        )

        data = json.loads(
            response.read()
        )


        city = data.get(
            "city",
            LOCATION_NAME
        )

        latitude = data.get(
            "latitude",
            LATITUDE
        )

        longitude = data.get(
            "longitude",
            LONGITUDE
        )


        print("\n📡 Internet location found:")
        print("Location:", city)
        print("Latitude:", latitude)
        print("Longitude:", longitude)


        return {
            "name": city,
            "latitude": latitude,
            "longitude": longitude
        }


    except Exception as error:

        print("\n⚠️ No internet location available")
        print("Reason:", error)

        print("\nUsing default location:")
        print("Location:", LOCATION_NAME)
        print("Latitude:", LATITUDE)
        print("Longitude:", LONGITUDE)


        return {
            "name": LOCATION_NAME,
            "latitude": LATITUDE,
            "longitude": LONGITUDE
        }



if __name__ == "__main__":

    location = get_location()

    print("\n🌍 Final location used:")
    print(location)