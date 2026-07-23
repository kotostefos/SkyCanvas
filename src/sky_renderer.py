from PIL import Image, ImageDraw
from sky_engine import get_sky_position


def create_sky_image():

    width = 1200
    height = 800

    # Get astronomy data 🌌

    sky = get_sky_position()


    # Create sky gradient

    image = Image.new(
        "RGB",
        (width, height)
    )

    pixels = image.load()

    for y in range(height):

        ratio = y / height

        # Sky colours
        r = int(15 + ratio * 100)
        g = int(30 + ratio * 70)
        b = int(90 + ratio * 80)

        for x in range(width):
            pixels[x, y] = (r, g, b)


    draw = ImageDraw.Draw(image)


    # Horizon

    horizon = height * 0.75

    draw.line(
        (0, horizon, width, horizon),
        fill=(120, 120, 140),
        width=2
    )


    # Real stars ⭐

    stars = sky["stars"]

    for star in stars:

        altitude = star["altitude"]
        azimuth = star["azimuth"]

        print(
            f"Star {star['name']}: "
            f"Altitude {altitude:.2f}° "
            f"Azimuth {azimuth:.2f}°"
        )

        # Only draw stars above horizon

        if altitude > 0:

            x = (azimuth / 360) * width

            y = height - (
                (altitude + 90) / 180
            ) * height

            draw.ellipse(
                (
                    x-3,
                    y-3,
                    x+3,
                    y+3
                ),
                fill="white"
            )


    # Real Moon position 🌙

    moon_altitude = sky["moon_altitude"]
    moon_azimuth = sky["moon_azimuth"]

    print("Renderer Moon altitude:", moon_altitude)
    print("Renderer Moon azimuth:", moon_azimuth)


    # Convert Moon coordinates to image coordinates

    x = (moon_azimuth / 360) * width

    y = height - (
        (moon_altitude + 90) / 180
    ) * height


    if moon_altitude > 0:

        # Moon glow layers

        draw.ellipse(
            (x-60, y-60, x+60, y+60),
            fill=(180, 180, 200)
        )

        draw.ellipse(
            (x-40, y-40, x+40, y+40),
            fill=(220, 220, 230)
        )

        draw.ellipse(
            (x-20, y-20, x+20, y+20),
            fill="white"
        )

    else:
        print("Moon is below horizon")


    # Save image

    image.save(
        "assets/skycanvas_test.png"
    )

    print("🌌 Sky image created!")


if __name__ == "__main__":
    create_sky_image()