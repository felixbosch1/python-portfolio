#Felix Bosch
#US Trip planner
#Initiaztion
import random
from PIL import Image
import requests
from io import BytesIO

citylist = ["https://tinyurl.com/yh69wpw3" #NYC
,"https://tinyurl.com/2835fm6x" #Chi
, "https://tinyurl.com/yc8dnmad" #Seattle
, "https://tinyurl.com/4n4639ru" #San Fran
, "https://tinyurl.com/3uhvcwmt" #Miami
]

#Functions
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()
def tripdecidor():
    print("Welcome to yours next trip decider!")
    while True:
        num = random.randint(1,5)
        yesno = input("Are you ready to find out where you're going! (yes or no): ")
        yesno = yesno.lower()
        if yesno == "yes":
            if num == 1:
                open_image(citylist[0])
                print("""You will be traveling to New York City.
A bustling, vibrant metropolis known for its iconic skyline,
diverse culture, and global influence in finance, fashion, and the arts.
With five boroughs—Manhattan, Brooklyn, Queens, the Bronx, and Staten
Island—each offering unique experiences, it’s a city that never sleeps
and attracts millions from around the world.""")
            elif num == 2:
                open_image(citylist[1])
                print("""You will be traveling to Chicago.
A dynamic city located on the shores of Lake Michigan, famous for
its architectural marvels, rich history, and deep-rooted cultural scene.
Known for its diverse neighborhoods, world-class museums,
and iconic food like deep-dish pizza,
Chicago blends Midwestern charm with urban sophistication.""")
            elif num == 3:
                open_image(citylist[2])
                print("""You will be traveling to Seattle.
A tech-driven city nestled between the Puget Sound and
the Cascade Mountains, renowned for its coffee culture,
innovative spirit, and stunning natural scenery.
With landmarks like the Space Needle and Pike Place Market,
it blends a laid-back vibe with a thriving arts scene and
a strong connection to the outdoors.""")
            elif num == 4:
                open_image(citylist[3])
                print("""You will be traveling to San Francisco.
A picturesque city known for its iconic Golden Gate Bridge,
steep hills, and eclectic mix of cultures. With its vibrant
tech industry, historic neighborhoods, and diverse culinary scene,
it offers a unique blend of innovation and tradition
set against stunning bay views.""")
            elif num == 5:
                open_image(citylist[4])
                print("""You will be traveling to Miami.
A vibrant, sun-soaked city famous for its stunning beaches,
lively nightlife, and Latin-influenced culture.
With its colorful art deco architecture, thriving arts scene,
and diverse culinary offerings, Miami blends relaxation
with excitement in a tropical paradise setting.""")
        else:
            print("Thank you for trying to decide")
            break


#Main
tripdecidor()




#Citations
#New york city: (2024). Istockphoto.com. https://www.istockphoto.com/photos/skyline-dusk
#Chicago: Unsplash. (n.d.). 1000+ Chicago Skyline Pictures | Download Free Images on Unsplash. Unsplash.com. https://unsplash.com/s/photos/chicago-skyline
#Seattle: Murray, J. (2019). Jeffrey Murray Photography - Limited Edition Photography by Jeffrey Murray. Jeffrey Murray Photography - Limited Edition Photography by Jeffrey Murray. https://www.jeffreymurrayphotography.com/urban/seattle-skyline
#San Fransisco: California, F. (2025). San Francisco Skyline Images – Browse 85,615 Stock Photos, Vectors, and Video. Adobe Stock. https://stock.adobe.com/search?k=san+francisco+skyline
#Miami: Downtown Miami Skyline Stock Photos, Pictures & Royalty-Free Images - iStock. (2024). Istockphoto.com. https://www.istockphoto.com/photos/downtown-miami-skyline
