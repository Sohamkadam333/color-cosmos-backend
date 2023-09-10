from pymongo import MongoClient

# Replace the connection string with your MongoDB Atlas connection string
connection_string = "mongodb+srv://sohamkadam58:gWaUPTqfXyZp6iXC@cluster0.epoajue.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client["color-cosmos"]
collection = db["palates"]

# Insert the data
data = [
    {
        "name": "Vibrant Hues",
        "colors": [
            { "name": "Electric Blue", "hex": "#00bfff" },
            { "name": "Fiery Red", "hex": "#ff4500" },
            { "name": "Sunny Yellow", "hex": "#ffff00" },
            { "name": "Emerald Green", "hex": "#008000" },
            { "name": "Purple Majesty", "hex": "#800080" }
        ],
        "id": "1c74a6bf-3ed5-4f9d-974d-94e126303c58"
    },
    {
        "name": "Pastel Paradise",
        "colors": [
            { "name": "Soft Pink", "hex": "#ffc0cb" },
            { "name": "Lilac Lavender", "hex": "#c8a2c8" },
            { "name": "Mint Green", "hex": "#98ff98" },
            { "name": "Baby Blue", "hex": "#a6caf0" },
            { "name": "Buttercream Yellow", "hex": "#fffacd" }
        ],
        "id": "8f286d31-918e-488d-a9da-709ff3ccf808"
    },
    {
        "name": "Sunset Serenity",
        "colors": [
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Calm Pink", "hex": "#ffc0cb" },
            { "name": "Golden Glow", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" },
            { "name": "Horizon Blue", "hex": "#4682b4" }
        ],
        "id": "d27158f1-624d-43f7-8c29-7c3f20f73d23"
    },
    {
        "name": "Nature's Beauty",
        "colors": [
            { "name": "Forest Green", "hex": "#228b22" },
            { "name": "Sky Blue", "hex": "#87ceeb" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Sunflower Yellow", "hex": "#ffd700" },
            { "name": "Earthy Brown", "hex": "#8b4513" }
        ],
        "id": "9df4e3c1-2c05-46be-9f1e-b1471167f99d"
    },
    {
        "name": "Mystic Dreams",
        "colors": [
            { "name": "Mystic Purple", "hex": "#9a32cd" },
            { "name": "Midnight Black", "hex": "#191970" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" },
            { "name": "Enchanted Blue", "hex": "#104e8b" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "0e06c8ef-262d-4ea6-a4f7-6aef262d4ea6"
    },
    {
        "name": "Cozy Comfort",
        "colors": [
            { "name": "Warm Red", "hex": "#ff4500" },
            { "name": "Cocoa Brown", "hex": "#d2691e" },
            { "name": "Chestnut Brown", "hex": "#8b4513" },
            { "name": "Creamy Beige", "hex": "#fff5ee" },
            { "name": "Soft Gray", "hex": "#d3d3d3" }
        ],
        "id": "7b7f62df-9b5b-4a10-9f62-df9b5b4a107f"
    },
    {
        "name": "Ocean Breeze",
        "colors": [
            { "name": "Ocean Blue", "hex": "#0077b6" },
            { "name": "Aqua Teal", "hex": "#00ced1" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Seashell Pink", "hex": "#fff5ee" },
            { "name": "Deep Sea Green", "hex": "#005a52" }
        ],
        "id": "c9c34de5-37ab-4a76-b34d-e537ab4a76bd"
    },
    {
        "name": "Elegant Affair",
        "colors": [
            { "name": "Elegant Gray", "hex": "#808080" },
            { "name": "Sleek Black", "hex": "#000000" },
            { "name": "Ivory White", "hex": "#fffff0" },
            { "name": "Rustic Red", "hex": "#8b0000" },
            { "name": "Antique Gold", "hex": "#856d4d" }
        ],
        "id": "46e6b70f-ae7e-4b23-a6b7-0fae7e4b2386"
    },
    {
        "name": "Tropical Getaway",
        "colors": [
            { "name": "Tropical Turquoise", "hex": "#00ced1" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Palm Tree Green", "hex": "#8fbc8f" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Golden Sun", "hex": "#ffd700" }
        ],
        "id": "bb758b2a-e16e-4a03-958b-2ae16e4a0395"
    },
    {
        "name": "Cozy Cabin",
        "colors": [
            { "name": "Warm Wood Brown", "hex": "#8b4513" },
            { "name": "Cabin Red", "hex": "#cd853f" },
            { "name": "Log Cabin Brown", "hex": "#8b7765" },
            { "name": "Frosty White", "hex": "#e0ffff" },
            { "name": "Snowy Gray", "hex": "#c0c0c0" }
        ],
        "id": "82634ea1-24f2-4e69-834e-a124f24e6993"
    },
    {
        "name": "Misty Mountains",
        "colors": [
            { "name": "Mountain Gray", "hex": "#818181" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Heather Purple", "hex": "#a29acf" },
            { "name": "Foggy White", "hex": "#f0f0f0" },
            { "name": "Slate Black", "hex": "#2f4f4f" }
        ],
        "id": "dc1b8aef-700b-4975-9da7-80fc58c3c7f6"
    },
    {
        "name": "Serene Seaside",
        "colors": [
            { "name": "Seaside Blue", "hex": "#00ced1" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Calm Coral", "hex": "#ff6b6b" },
            { "name": "Shell White", "hex": "#fff5ee" },
            { "name": "Ocean Wave Gray", "hex": "#717171" }
        ],
        "id": "14e3f6a1-991c-45bf-9b23-e0084d95767e"
    },
    {
        "name": "Retro Vibes",
        "colors": [
            { "name": "Retro Red", "hex": "#ff5050" },
            { "name": "Funky Green", "hex": "#7fff00" },
            { "name": "Disco Purple", "hex": "#9400d3" },
            { "name": "Groovy Orange", "hex": "#ff6600" },
            { "name": "Cool Blue", "hex": "#3399ff" }
        ],
        "id": "89a79a36-5932-4dbd-9a79-a3659324dbd5"
    },
    {
        "name": "Enchanted Garden",
        "colors": [
            { "name": "Mystic Green", "hex": "#1f5c21" },
            { "name": "Floral Pink", "hex": "#ff6b6b" },
            { "name": "Sunlit Yellow", "hex": "#ffdb58" },
            { "name": "Woodland Brown", "hex": "#8b4513" },
            { "name": "Magic Purple", "hex": "#da70d6" }
        ],
        "id": "dc1b8aef-700b-4975-9da7-80fc58c3c7f6"
    },
    {
        "name": "Autumn Splendor",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Harvest Gold", "hex": "#daa520" }
        ],
        "id": "6dd1f38b-941f-41a1-b1f3-8b941f41a1d6"
    },
    {
        "name": "Pastel Dreams",
        "colors": [
            { "name": "Pastel Pink", "hex": "#ffb6c1" },
            { "name": "Lavender Mist", "hex": "#e6e6fa" },
            { "name": "Minty Green", "hex": "#98ff98" },
            { "name": "Baby Blue", "hex": "#a6caf0" },
            { "name": "Soft Peach", "hex": "#ffcc99" }
        ],
        "id": "9f4bb3e0-c20f-47bf-8bb3-e0c20f47bf2f"
    },
    {
        "name": "Industrial Vibes",
        "colors": [
            { "name": "Steel Gray", "hex": "#808080" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Concrete Gray", "hex": "#f2f2f2" },
            { "name": "Slate Black", "hex": "#2f4f4f" },
            { "name": "Metallic Silver", "hex": "#c0c0c0" }
        ],
        "id": "a33a932b-91bb-41b9-93a9-32b91bb41b9c"
    },
    {
        "name": "Eternal Spring",
        "colors": [
            { "name": "Spring Green", "hex": "#00ff7f" },
            { "name": "Cherry Blossom Pink", "hex": "#ffc0cb" },
            { "name": "Daffodil Yellow", "hex": "#ffff31" },
            { "name": "Azure Blue", "hex": "#007fff" },
            { "name": "Fresh White", "hex": "#ffffff" }
        ],
        "id": "dc1b8aef-700b-4975-9da7-80fc58c3c7f6"
    },
    {
        "name": "Desert Oasis",
        "colors": [
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Cactus Green", "hex": "#5f9ea0" },
            { "name": "Terracotta Red", "hex": "#d2735b" },
            { "name": "Sahara Yellow", "hex": "#f0e68c" },
            { "name": "Dune Brown", "hex": "#967117" }
        ],
        "id": "ea2c1e1c-8bb2-4f5b-bc1e-1c8bb24f5b39"
    },
    {
        "name": "Royal Elegance",
        "colors": [
            { "name": "Royal Blue", "hex": "#4169e1" },
            { "name": "Regal Purple", "hex": "#800080" },
            { "name": "Velvet Red", "hex": "#b22222" },
            { "name": "Golden Crown", "hex": "#ffd700" },
            { "name": "Ivory White", "hex": "#fffff0" }
        ],
        "id": "d8d7f8a1-710a-4f54-8d7f-8a1710a4f54b"
    },
    {
        "name": "Summer Bliss",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#ffff00" },
            { "name": "Beach Sand", "hex": "#f5deb3" },
            { "name": "Ocean Blue", "hex": "#0077b6" },
            { "name": "Palm Tree Green", "hex": "#8fbc8f" },
            { "name": "Tropical Sunset Orange", "hex": "#ff6b6b" }
        ],
        "id": "78ce5595-d2b7-4b5a-8e55-95d2b74b5a54"
    },
    {
        "name": "Classic Neutrals",
        "colors": [
            { "name": "Warm Gray", "hex": "#808069" },
            { "name": "Neutral Beige", "hex": "#d2b48c" },
            { "name": "Crisp White", "hex": "#ffffff" },
            { "name": "Cool Charcoal", "hex": "#36454f" },
            { "name": "Earthy Brown", "hex": "#8b4513" }
        ],
        "id": "aef07e0e-40b1-4833-b07e-0e40b14833fc"
    },
    {
        "name": "Golden Hour",
        "colors": [
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Warm Red", "hex": "#ff6347" },
            { "name": "Amber Gold", "hex": "#ffbf00" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "34e3dd12-d2be-4301-83dd-12d2be4301f2"
    },
    {
        "name": "Tranquil Waters",
        "colors": [
            { "name": "Calm Blue", "hex": "#add8e6" },
            { "name": "Turquoise Teal", "hex": "#40e0d0" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Seafoam Green", "hex": "#2e8b57" },
            { "name": "Misty Gray", "hex": "#bdbdbd" }
        ],
        "id": "b88ea2e5-9f1b-4751-8ea2-e59f1b4751d1"
    },
    {
        "name": "Vintage Glamour",
        "colors": [
            { "name": "Vintage Red", "hex": "#9b111e" },
            { "name": "Glamorous Gold", "hex": "#ffd700" },
            { "name": "Pearl White", "hex": "#f2f2f2" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Classic Gray", "hex": "#808080" }
        ],
        "id": "d06c0a9e-8d1d-4c87-9c0a-9e8d1d4c877c"
    },
    {
        "name": "Spring Awakening",
        "colors": [
            { "name": "Fresh Green", "hex": "#00ff00" },
            { "name": "Cherry Blossom Pink", "hex": "#ffc0cb" },
            { "name": "Daffodil Yellow", "hex": "#ffff31" },
            { "name": "Sky Blue", "hex": "#87ceeb" },
            { "name": "Lilac Purple", "hex": "#c8a2c8" }
        ],
        "id": "53663462-136d-4415-9634-62136d4415d1"
    },
    {
        "name": "Autumn Glow",
        "colors": [
            { "name": "Harvest Orange", "hex": "#d9534f" },
            { "name": "Autumn Red", "hex": "#ff4500" },
            { "name": "Golden Brown", "hex": "#8b4513" },
            { "name": "Rustic Gold", "hex": "#b8860b" },
            { "name": "Fallen Leaf Brown", "hex": "#966f33" }
        ],
        "id": "451f7c31-9a87-498b-9f7c-319a87498b15"
    },
    {
        "name": "Candy Crush",
        "colors": [
            { "name": "Bubblegum Pink", "hex": "#ff69b4" },
            { "name": "Lollipop Purple", "hex": "#9400d3" },
            { "name": "Lemon Yellow", "hex": "#fff44f" },
            { "name": "Minty Green", "hex": "#98ff98" },
            { "name": "Blue Raspberry", "hex": "#4169e1" }
        ],
        "id": "7591b525-5c5b-4c5d-91b5-255c5b4c5d61"
    },
    {
        "name": "Urban Jungle",
        "colors": [
            { "name": "Concrete Gray", "hex": "#f2f2f2" },
            { "name": "Jungle Green", "hex": "#29ab87" },
            { "name": "Brick Red", "hex": "#b22222" },
            { "name": "Steel Gray", "hex": "#4b4b4b" },
            { "name": "Asphalt Black", "hex": "#130f0e" }
        ],
        "id": "e465d3e0-27bd-4e82-b65d-3e027bd4e82e"
    },
    {
        "name": "Winter Wonderland",
        "colors": [
            { "name": "Snowy White", "hex": "#fffafa" },
            { "name": "Ice Blue", "hex": "#b0e0e6" },
            { "name": "Frosty Gray", "hex": "#d3d3d3" },
            { "name": "Icy Silver", "hex": "#c0c0c0" },
            { "name": "Midnight Black", "hex": "#000000" }
        ],
        "id": "c6dabf45-ec67-442f-adab-f45ec67442f3"
    },
    {
        "name": "Golden Moments",
        "colors": [
            { "name": "Goldenrod Yellow", "hex": "#daa520" },
            { "name": "Glistening Gold", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Royal Purple", "hex": "#6a0dad" },
            { "name": "Shimmering Champagne", "hex": "#ffd700" }
        ],
        "id": "e2c997a3-935a-4e92-8997-a3935a4e928e"
    },
    {
        "name": "Minimalist Chic",
        "colors": [
            { "name": "Sleek Black", "hex": "#000000" },
            { "name": "Pure White", "hex": "#ffffff" },
            { "name": "Elegant Gray", "hex": "#808080" },
            { "name": "Neutral Beige", "hex": "#d2b48c" },
            { "name": "Sophisticated Silver", "hex": "#c0c0c0" }
        ],
        "id": "d548af4b-0cd4-43f3-88af-4b0cd443f386"
    },
    {
        "name": "Tropical Paradise",
        "colors": [
            { "name": "Tropical Turquoise", "hex": "#00ced1" },
            { "name": "Palm Tree Green", "hex": "#8fbc8f" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Golden Sun", "hex": "#ffd700" }
        ],
        "id": "0a09fd92-73fa-4a53-a09f-d9273fa4a538"
    },
    {
        "name": "Mystical Forest",
        "colors": [
            { "name": "Forest Green", "hex": "#228b22" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Wandering White", "hex": "#ffffff" },
            { "name": "Sorcerer's Blue", "hex": "#1e90ff" }
        ],
        "id": "b76bb8f0-c25a-494b-96bb-8f0c25a494bc"
    },
    {
        "name": "Summer Sorbet",
        "colors": [
            { "name": "Sorbet Orange", "hex": "#ff6b6b" },
            { "name": "Lemon Sorbet Yellow", "hex": "#fff44f" },
            { "name": "Berry Sorbet Pink", "hex": "#ff6b6b" },
            { "name": "Cool Mint Sorbet", "hex": "#98ff98" },
            { "name": "Tropical Sorbet Blue", "hex": "#00ced1" }
        ],
        "id": "be84fe4b-511c-4f3f-84fe-4b511c4f3fd2"
    },
    {
        "name": "Summer Fun",
        "colors": [
            { "name": "Beachy Blue", "hex": "#87ceeb" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Lively Orange", "hex": "#ff6600" },
            { "name": "Sunshine Yellow", "hex": "#fff44f" },
            { "name": "Tropical Green", "hex": "#00ff7f" }
        ],
        "id": "b6f130bd-6793-4e29-9130-bd67934e2917"
    },
    {
        "name": "Autumn Delight",
        "colors": [
            { "name": "Autumn Red", "hex": "#ff4500" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Harvest Orange", "hex": "#d9534f" },
            { "name": "Fallen Leaf Brown", "hex": "#966f33" }
        ],
        "id": "fcd5cc8d-b979-4b15-d5cc-8db9794b153e"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Antique Rose", "hex": "#d3a096" },
            { "name": "Elegant Gray", "hex": "#808080" },
            { "name": "Sleek Black", "hex": "#000000" },
            { "name": "Classic Ivory", "hex": "#fffff0" },
            { "name": "Royal Purple", "hex": "#6a0dad" }
        ],
        "id": "d706020f-3d67-42c9-8602-0f3d6742c930"
    },
    {
        "name": "Oceanic Escape",
        "colors": [
            { "name": "Ocean Blue", "hex": "#0077b6" },
            { "name": "Aqua Teal", "hex": "#00ced1" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Seashell Pink", "hex": "#fff5ee" },
            { "name": "Deep Sea Green", "hex": "#005a52" }
        ],
        "id": "e0f6716e-8ea2-4a53-f671-6e8ea24a53e3"
    },
    {
        "name": "Vintage Romance",
        "colors": [
            { "name": "Romantic Red", "hex": "#e60000" },
            { "name": "Antique Pink", "hex": "#f4c2c2" },
            { "name": "Elegant Gray", "hex": "#808080" },
            { "name": "Slate Black", "hex": "#2f4f4f" },
            { "name": "Vintage Gold", "hex": "#85754d" }
        ],
        "id": "7f5623ac-bbd7-4751-5623-acbbd747513d"
    },
    {
        "name": "Mystical Night",
        "colors": [
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "c8b9f5bd-df29-473a-b9f5-bddf29473a73"
    },
    {
        "name": "Pastel Serenity",
        "colors": [
            { "name": "Pastel Pink", "hex": "#ffb6c1" },
            { "name": "Lavender Mist", "hex": "#e6e6fa" },
            { "name": "Minty Green", "hex": "#98ff98" },
            { "name": "Baby Blue", "hex": "#a6caf0" },
            { "name": "Soft Peach", "hex": "#ffcc99" }
        ],
        "id": "c8b9f5bd-df29-473a-b9f5-bddf29473a73"
    },
    {
        "name": "Enchanted Forest",
        "colors": [
            { "name": "Mystic Green", "hex": "#1f5c21" },
            { "name": "Woodland Brown", "hex": "#8b4513" },
            { "name": "Magic Purple", "hex": "#da70d6" },
            { "name": "Enchanted Blue", "hex": "#104e8b" },
            { "name": "Mysterious Black", "hex": "#000000" }
        ],
        "id": "6fd6eb08-d2fe-4f4a-d6eb-08d2fe4f4a4d"
    },
    {
        "name": "Tropical Sunset",
        "colors": [
            { "name": "Tropical Orange", "hex": "#ff6b6b" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Palm Tree Green", "hex": "#8fbc8f" },
            { "name": "Ocean Blue", "hex": "#0077b6" },
            { "name": "Golden Sun", "hex": "#ffd700" }
        ],
        "id": "b7299394-46d4-40f9-9939-9446d440f9f0"
    },
    {
        "name": "Mystic Moonlight",
        "colors": [
            { "name": "Moonlit Silver", "hex": "#c0c0c0" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "272a3214-dad5-46e3-a321-4dad546e3a32"
    },
    {
        "name": "Rustic Retreat",
        "colors": [
            { "name": "Rustic Red", "hex": "#8b0000" },
            { "name": "Cozy Brown", "hex": "#964b00" },
            { "name": "Log Cabin Brown", "hex": "#8b7765" },
            { "name": "Crisp White", "hex": "#ffffff" },
            { "name": "Earthy Green", "hex": "#228b22" }
        ],
        "id": "c4ec64a6-886d-4ac5-ec64-a6886d4ac58e"
    },
    {
        "name": "Summer Sunsets",
        "colors": [
            { "name": "Sunkissed Orange", "hex": "#ff4500" },
            { "name": "Tropical Pink", "hex": "#ff6b6b" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Beachy Blue", "hex": "#87ceeb" },
            { "name": "Sandy Beige", "hex": "#f4a460" }
        ],
        "id": "c6c3fcda-ef36-45b5-c3fc-daef3645b528"
    },
    {
        "name": "Retro Revival",
        "colors": [
            { "name": "Retro Red", "hex": "#ff5050" },
            { "name": "Funky Green", "hex": "#7fff00" },
            { "name": "Disco Purple", "hex": "#9400d3" },
            { "name": "Groovy Orange", "hex": "#ff6600" },
            { "name": "Cool Blue", "hex": "#3399ff" }
        ],
        "id": "f0b30801-169e-4e07-b308-01169e4e07a5"
    },
    {
        "name": "Vintage Vibes",
        "colors": [
            { "name": "Retro Red", "hex": "#ff5050" },
            { "name": "Rusty Orange", "hex": "#d2691e" },
            { "name": "Olive Green", "hex": "#556b2f" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Creamy White", "hex": "#fffacd" }
        ],
        "id": "5bf3d6ea-95fc-48c5-f3d6-ea95fc48c5fa"
    },
    {
        "name": "Ocean Breeze",
        "colors": [
            { "name": "Ocean Blue", "hex": "#0077b6" },
            { "name": "Seafoam Green", "hex": "#2e8b57" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Seashell Pink", "hex": "#fff5ee" },
            { "name": "Driftwood Brown", "hex": "#a0522d" }
        ],
        "id": "4e508421-0040-4322-8508-42100404322a"
    },
    {
        "name": "Serenity Blue",
        "colors": [
            { "name": "Serenity Blue", "hex": "#6d9bf1" },
            { "name": "Crisp White", "hex": "#ffffff" },
            { "name": "Tranquil Gray", "hex": "#c0c0c0" },
            { "name": "Slate Black", "hex": "#2f4f4f" },
            { "name": "Ocean Wave Green", "hex": "#008000" }
        ],
        "id": "b2e849d3-9cf9-424e-849d-39cf9424e849"
    },
    {
        "name": "Autumn Harvest",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Harvest Red", "hex": "#d32f2f" },
            { "name": "Autumn Green", "hex": "#228b22" }
        ],
        "id": "56a046e2-28f2-4d77-a046-e228f24d77e0"
    },
    {
        "name": "Urban Chic",
        "colors": [
            { "name": "Sleek Black", "hex": "#000000" },
            { "name": "Sophisticated Gray", "hex": "#808080" },
            { "name": "Modern White", "hex": "#ffffff" },
            { "name": "Metallic Silver", "hex": "#c0c0c0" },
            { "name": "City Skyline Blue", "hex": "#8db6cd" }
        ],
        "id": "dd82f2f3-1ad5-43cb-82f2-f31ad543cb16"
    },
    {
        "name": "Vintage Elegance",
        "colors": [
            { "name": "Classic Ivory", "hex": "#fffff0" },
            { "name": "Antique Rose", "hex": "#d3a096" },
            { "name": "Elegant Gray", "hex": "#808080" },
            { "name": "Deep Plum", "hex": "#9b111e" },
            { "name": "Regal Gold", "hex": "#ffd700" }
        ],
        "id": "7b370c4e-9351-43eb-b370-c4e935143eb0"
    },
    {
        "name": "Mystical Twilight",
        "colors": [
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Enchanted Black", "hex": "#1a1a1a" }
        ],
        "id": "45e12828-1f6d-4c98-e128-281f6d4c98e1"
    },
    {
        "name": "Summer Fiesta",
        "colors": [
            { "name": "Fiesta Red", "hex": "#ff6347" },
            { "name": "Sunny Yellow", "hex": "#ffff00" },
            { "name": "Tropical Orange", "hex": "#ff6b6b" },
            { "name": "Lively Green", "hex": "#00ff7f" },
            { "name": "Vibrant Blue", "hex": "#0000ff" }
        ],
        "id": "b81f4ed6-8f18-4a61-81f4-ed68f184a61b"
    },
    {
        "name": "Autumn Splendor",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Harvest Gold", "hex": "#daa520" }
        ],
        "id": "be7a7e3d-bf7e-44bb-a7e3-dbf7e44bba7d"
    },
    {
        "name": "Mystic Forest",
        "colors": [
            { "name": "Forest Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "06e15c67-4095-48b7-e15c-67409548b7c9"
    },
    {
        "name": "Cotton Candy",
        "colors": [
            { "name": "Cotton Candy Pink", "hex": "#ffb6c1" },
            { "name": "Blue Cotton Candy", "hex": "#a2cffe" },
            { "name": "Lavender Cotton Candy", "hex": "#f0a6ca" },
            { "name": "Minty Cotton Candy", "hex": "#98ff98" },
            { "name": "Strawberry Cotton Candy", "hex": "#ffabab" }
        ],
        "id": "ea5f1f7e-7b7b-48dd-9f1f-7e7b7b48dd55"
    },
    {
        "name": "Coastal Retreat",
        "colors": [
            { "name": "Beachy Blue", "hex": "#87ceeb" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Seafoam Green", "hex": "#2e8b57" },
            { "name": "Nautical Navy", "hex": "#000080" },
            { "name": "Driftwood Brown", "hex": "#a0522d" }
        ],
        "id": "c8c0c0c0-c0c0-c8c0-c0c0c0c0c0c0"
    },
    {
        "name": "Mystic Dreams",
        "colors": [
            { "name": "Dreamy Blue", "hex": "#4682b4" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "bfc02b95-16b1-4d4c-902b-9516b14d4c9d"
    },
    {
        "name": "Retro Cool",
        "colors": [
            { "name": "Retro Red", "hex": "#ff5050" },
            { "name": "Groovy Green", "hex": "#00ff00" },
            { "name": "Disco Purple", "hex": "#9400d3" },
            { "name": "Funky Orange", "hex": "#ff6600" },
            { "name": "Cool Blue", "hex": "#3399ff" }
        ],
        "id": "e84c8e14-e84c-48b7-8c8e-14e84c48b7d5"
    },
    {
        "name": "Country Cottage",
        "colors": [
            { "name": "Country Red", "hex": "#ff4d4d" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Meadow Green", "hex": "#3cb371" },
            { "name": "Sky Blue", "hex": "#87ceeb" },
            { "name": "Creamy White", "hex": "#fffacd" }
        ],
        "id": "1a0c570a-1a0c-48a2-0c57-0a1a0c48a2a8"
    },
    {
        "name": "Mystical Magic",
        "colors": [
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "f7dd7c8b-0975-4da7-dd7c-8b09754da7b7"
    },
    {
        "name": "Summer Bliss",
        "colors": [
            { "name": "Sunshine Yellow", "hex": "#fff44f" },
            { "name": "Sorbet Orange", "hex": "#ff6b6b" },
            { "name": "Tropical Green", "hex": "#00ff7f" },
            { "name": "Beachy Blue", "hex": "#87ceeb" },
            { "name": "Sandy Beige", "hex": "#f4a460" }
        ],
        "id": "c6e385e2-0e30-4e29-9855-e20e304e2985"
    },
    {
        "name": "Retro Vibes",
        "colors": [
            { "name": "Retro Red", "hex": "#ff5050" },
            { "name": "Funky Green", "hex": "#7fff00" },
            { "name": "Disco Purple", "hex": "#9400d3" },
            { "name": "Groovy Orange", "hex": "#ff6600" },
            { "name": "Cool Blue", "hex": "#3399ff" }
        ],
        "id": "09ea3bc5-ea3b-437a-9ea3-bc5ea3b437a0"
    },
    {
        "name": "Country Charm",
        "colors": [
            { "name": "Country Red", "hex": "#ff4d4d" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Meadow Green", "hex": "#3cb371" },
            { "name": "Sky Blue", "hex": "#87ceeb" },
            { "name": "Creamy White", "hex": "#fffacd" }
        ],
        "id": "d287a587-0e76-4523-87a5-870e764523d6"
    },
    {
        "name": "Mystical Mornings",
        "colors": [
            { "name": "Morning Mist Gray", "hex": "#e0e0e0" },
            { "name": "Dawn Pink", "hex": "#f3c2c2" },
            { "name": "Sky Blue", "hex": "#87ceeb" },
            { "name": "Sunrise Orange", "hex": "#ff6600" },
            { "name": "Mystic Purple", "hex": "#800080" }
        ],
        "id": "6f68ac31-9f94-4640-8ac3-19946408ac31"
    },
    {
        "name": "Rustic Elegance",
        "colors": [
            { "name": "Rustic Red", "hex": "#8b0000" },
            { "name": "Crimson Velvet", "hex": "#7e354d" },
            { "name": "Elegant Gray", "hex": "#808080" },
            { "name": "Golden Harvest", "hex": "#daa520" },
            { "name": "Antique Ivory", "hex": "#f5deb3" }
        ],
        "id": "12b7a0ea-b7a0-4c1d-b7a0-ea12b7a04c1d"
    },
    {
        "name": "Sunset Glow",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "0ebef6ec-bde8-467a-bef6-ecbde8467a8b"
    },
    {
        "name": "Desert Oasis",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Cactus Green", "hex": "#5f9ea0" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "c37ac3b3-7ac3-47d5-ac3b-37ac3b37d5e9"
    },
    {
        "name": "Autumn Glow",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "d0eb5a67-0b29-4a14-eb5a-670b294a14b6"
    },
    {
        "name": "Vintage Glam",
        "colors": [
            { "name": "Glamorous Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "db5dd777-bd77-4e9c-5dd7-77bd774e9c50"
    },
    {
        "name": "Mystical Waters",
        "colors": [
            { "name": "Deep Blue", "hex": "#00008b" },
            { "name": "Aqua Teal", "hex": "#00ced1" },
            { "name": "Turquoise Waters", "hex": "#40e0d0" },
            { "name": "Seafoam Green", "hex": "#2e8b57" },
            { "name": "Mystic Blue", "hex": "#4682b4" }
        ],
        "id": "4a93e39d-3af3-464a-93e3-9d3af3464a97"
    },
    {
        "name": "Safari Adventure",
        "colors": [
            { "name": "Safari Khaki", "hex": "#bdbc7a" },
            { "name": "Lion's Mane Brown", "hex": "#d2b48c" },
            { "name": "Savannah Green", "hex": "#5f9ea0" },
            { "name": "Safari Sunset Orange", "hex": "#ff4500" },
            { "name": "Elephant Gray", "hex": "#808080" }
        ],
        "id": "56cd5f04-cd5f-47e1-8d5f-04cd5f47e1c9"
    },
    {
        "name": "Mystic Galaxy",
        "colors": [
            { "name": "Galactic Black", "hex": "#000000" },
            { "name": "Nebula Blue", "hex": "#000080" },
            { "name": "Astronomical Teal", "hex": "#008080" },
            { "name": "Starlight Silver", "hex": "#c0c0c0" },
            { "name": "Cosmic White", "hex": "#ffffff" }
        ],
        "id": "e3df6fbf-8af6-44eb-df6f-bf8af644ebfe"
    },
    {
        "name": "Tropical Dreams",
        "colors": [
            { "name": "Dreamy Blue", "hex": "#4682b4" },
            { "name": "Palm Tree Green", "hex": "#8fbc8f" },
            { "name": "Tropical Orange", "hex": "#ff6b6b" },
            { "name": "Sandy Beach", "hex": "#f4a460" },
            { "name": "Golden Sun", "hex": "#ffd700" }
        ],
        "id": "36ef8853-4cc6-4885-ef88-534cc64885e1"
    },
    {
        "name": "Mystic Hues",
        "colors": [
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "8b49091f-b3dd-46e4-9091-fb3dd46e4a4f"
    },
    {
        "name": "Sunset Serenity",
        "colors": [
            { "name": "Serenity Blue", "hex": "#6d9bf1" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "5b0b9a37-1e37-4b0b-b9a3-71e374b0b9a3"
    },
    {
        "name": "Desert Dreams",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Cactus Green", "hex": "#5f9ea0" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "d0109c50-63f4-44c0-109c-5063f444c017"
    },
    {
        "name": "Autumn Serenade",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Harvest Gold", "hex": "#daa520" }
        ],
        "id": "cc5bfa33-6f78-4a3b-5bfa-336f784a3b8f"
    },
    {
        "name": "Vintage Essence",
        "colors": [
            { "name": "Classic Ivory", "hex": "#fffff0" },
            { "name": "Antique Rose", "hex": "#d3a096" },
            { "name": "Elegant Gray", "hex": "#808080" },
            { "name": "Deep Plum", "hex": "#9b111e" },
            { "name": "Regal Gold", "hex": "#ffd700" }
        ],
        "id": "fcab0de0-8511-47e0-ab0d-e0851147e0c5"
    },
    {
        "name": "Mystic Dusk",
        "colors": [
            { "name": "Dusky Gray", "hex": "#6c757d" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "da8e281a-4c43-43d4-8e28-1a4c4343d48e"
    },
    {
        "name": "Summer Delight",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Tropical Pink", "hex": "#ff6b6b" },
            { "name": "Ocean Blue", "hex": "#0077b6" },
            { "name": "Lively Green", "hex": "#00ff7f" },
            { "name": "Beachy Blue", "hex": "#87ceeb" }
        ],
        "id": "e7ad408a-0b8e-41dd-ad40-8a0b8e41dddb"
    },
    {
        "name": "Retro Chic",
        "colors": [
            { "name": "Retro Red", "hex": "#ff5050" },
            { "name": "Funky Green", "hex": "#7fff00" },
            { "name": "Disco Purple", "hex": "#9400d3" },
            { "name": "Groovy Orange", "hex": "#ff6600" },
            { "name": "Cool Blue", "hex": "#3399ff" }
        ],
        "id": "2679f965-67f9-42bd-79f9-6567f942bd79"
    },
    {
        "name": "Country Comfort",
        "colors": [
            { "name": "Country Red", "hex": "#ff4d4d" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Meadow Green", "hex": "#3cb371" },
            { "name": "Sky Blue", "hex": "#87ceeb" },
            { "name": "Creamy White", "hex": "#fffacd" }
        ],
        "id": "4c1d49a4-c1d4-42ab-1d49-a4c1d42ab1d4"
    },
    {
        "name": "Mystical Whispers",
        "colors": [
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "3ff1a22d-f1a2-4a7d-f1a2-2d3ff1a22d3f"
    },
    {
        "name": "Sunset Radiance",
        "colors": [
            { "name": "Radiant Red", "hex": "#ff355e" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Beachy Blue", "hex": "#87ceeb" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "a3eb832e-986f-4526-eb83-2e986f4526b0"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Cactus Green", "hex": "#5f9ea0" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "a7fb1e63-3d0b-44a1-fb1e-633d0b44a1f9"
    },
    {
        "name": "Autumn Whispers",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Harvest Gold", "hex": "#daa520" }
        ],
        "id": "22ef8bd0-0ef8-4a13-ef8b-d00ef84a13e7"
    },
    {
        "name": "Vintage Luxe",
        "colors": [
            { "name": "Luxurious Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "dfe534ab-fe53-44bc-934a-bfe534abfe53"
    },
    {
        "name": "Mystic Oasis",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Calm Oasis Blue", "hex": "#5baccf" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Palm Tree Green", "hex": "#8fbc8f" },
            { "name": "Golden Sun", "hex": "#ffd700" }
        ],
        "id": "5b38f3f7-798c-41fc-8f3f-7798c41fc8f3"
    },
    {
        "name": "Sunset Splendor",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "4756206f-5620-46e3-9562-0646e3956206"
    },
    {
        "name": "Desert Twilight",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "d50a252a-0a25-4d50-a252-a0a254d50a25"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "5bb7223b-b722-4b72-b722-3b5bb7223b11"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "7f4bc1d0-f4bc-4534-bc1d-0f4bc1d04534"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "df4efcd4-4efc-47ea-9efc-d44efcd47ea9"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "a2b27b23-2b27-451f-b27b-232b27451fb7"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "a5e9dbd0-e9db-453f-9dbd-0e9dbd453f0e"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "b2d284ec-d284-428b-2d28-4ecb2d284ecb2"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "add377be-d377-4f56-d377-bed377bed377"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "88adcaea-adca-4b6d-adca-ea88adca4b6d"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "c5ed8f42-ed8f-4ce5-ed8f-42ed8f4ce5ed"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "f715c39c-15c3-4be1-15c3-9cf715c39c15"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "7e23a81e-23a8-4e7e-23a8-1e23a81e23a8"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "9ea59ff5-a59f-4a4e-a59f-f59ea59f4a4e"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "504b6825-4b68-4450-b682-54b68254450b"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "f989cd1b-89cd-4f98-89cd-1bf989cd1b89"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "76c5f81f-c5f8-42f7-c5f8-1f76c5f842f7"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "938f18d4-8f18-4c93-8f18-d48f188c938f"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "e3ad14ad-ad14-43e3-ad14-ade3ad14ad14"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "d15f0d0d-5f0d-48d1-5f0d-0dd15f0d0d5f"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "f6a7f9a5-a7f9-4a3f-a7f9-a5f6a7f9a5a7"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "84ef41ef-f41e-4b84-ef41-ef84ef41ef41"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "d2a199a9-a199-4d2a-9a99-a9d2a199a9a1"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "ecb74f03-cb74-4c0e-b74f-03cb7404c0e7"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "a8ecfd8b-ecfd-449a-8ecf-d8ba8ecfd8ba8"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "d1b1d8e7-1b1d-481b-1d8e-71b1d8481b1d"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "a4f8a393-f8a3-4aa4-f8a3-93a4f8a393f8"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "4a3fd8d5-a3fd-4c4a-3fd8-d5a4a3fd8d5a4"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "1b43b94a-43b9-411b-b43b-944a43b944a43"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "e941f4ef-41f4-4de9-41f4-ef41f4ef41f4"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "f9d2e8a7-d2e8-4f9d-2e8a-7df9d2e84f9d"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "8a7e75ea-7e75-468a-7e75-ea8a7e75ea7e"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "c00e8d80-0e8d-4cc0-0e8d-80c00e8d4cc0"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "e6e2baba-2bab-416e-e2ba-bae6e2baba2ba"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "c605a297-05a2-4c60-05a2-97c605a29705"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "b907606e-0760-4b90-7606-0eb907606e07"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "b032a8c3-32a8-4cb0-32a8-c3b032a8c3b0"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "8f31d2df-31d2-4e8f-31d2-df8f31d2df31"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "fcab7d4a-ab7d-4efc-ab7d-4afcab7d4ab7"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "f647ce2d-47ce-4bf6-47ce-2df647ce2d47"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "edbd0e91-bd0e-4eed-bd0e-91edbd0e91bd"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "4857abda-57ab-4385-57ab-da4857abda57"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "b902d592-02d5-4bb9-02d5-92b902d59202"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "db6d81ac-6d81-4bdb-6d81-acdb6d81ac6d"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "8dd2ea99-dd2e-418d-d2ea-998dd2ea99dd"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "a4e3a75c-4e3a-494a-e3a7-5ca4e3a75c4e"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "4b05d77f-b05d-48c4-05d7-7f4b05d77f05"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "dc64f735-64f7-434d-64f7-3564f73564f7"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "b60ef9cc-0ef9-424b-0ef9-ccb60ef9cc0e"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "49a9ed88-a9ed-4049-a9ed-8849a9ed88a9"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "0b23ec57-b23e-4c0b-23ec-570b23ec57b23"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "f88da9cc-8da9-4df8-8da9-ccf88da9cc8d"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "1f758ccd-f758-441f-758c-cdf1f758ccd75"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "f3a21cd6-a21c-4ef3-a21c-d6f3a21cd6a2"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "a7cf9dbb-cf9d-49a7-cf9d-bba7cf9dbbcf"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "fc08ec48-c08e-4ffc-08ec-48fc08ec48fc"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "f41da3c1-1da3-4ef4-1da3-c1f41da3c11d"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "5d03c4c6-d03c-405d-03c4-c65d03c4c65d"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "c12379c8-2379-4ec1-2379-c8c12379c823"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "1a40b836-a40b-431a-40b8-361a40b836a4"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "8eb8990a-8990-48a8-8990-a88eb8990a88"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "5a9617f1-a961-45a9-9617-f15a9617f145"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "b5b1fca1-1fca-4bb5-b1fc-a11b5b1fca11"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "73e1dd5c-e1dd-4c73-e1dd-5c73e1dd5ce1"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "50a0b705-a0b7-4e50-a0b7-0550a0b705a0"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "11f858b3-f858-4811-f858-b311f858b3f85"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "bfeb5d48-feb5-4cbf-eb5d-48bfeb5d48fe"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "9cf43e7b-cf43-49f9-cf43-e7b9cf43e7bcf"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "afda1cf0-fda1-41af-da1c-f0afda1cf0af"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "da8ea877-a8ea-4fda-8ea8-77da8ea877a8"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "ff68c73b-f68c-4fff-68c7-3bff68c73bf6"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "0b12cc46-b12c-400b-12cc-460b12cc46b12"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "664e7d6d-4e7d-4666-e7d6-d664e7d6d466"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "77d3a8d0-d3a8-4777-d3a8-d077d3a8d077"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "fb33bbd9-b33b-45fb-33bb-d9fb33bbd9b3"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "8fa013d1-fa01-48c8-fa01-3d18fa013d1fa"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "7cb36d6e-cb36-4c7b-36d6-ec7cb36d6ecb"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "a7fd9c2f-fd9c-49a7-fd9c-2fa7fd9c2f9c"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "43c2d22a-c2d2-4543-c2d2-2a43c2d22ac2"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "1f2ce531-2ce5-401f-2ce5-312f2ce5312ce"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "d7c0a721-c0a7-4bd7-c0a7-21d7c0a721c0"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "5cf09a52-cf09-485c-f09a-52cf09a52cf0"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "5a663e26-663e-45a6-663e-265a663e26663"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "f5a361f7-a361-4cf5-a361-f7f5a361f7a3"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "6eb1e70a-b1e7-46e6-b1e7-0a6eb1e70ab1"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "ed922df6-922d-4aed-922d-f6922df6922d"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "63f274ba-f274-463f-f274-ba63f274ba63"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "6b676a46-b676-4b6b-676a-466b676a466b"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "3e70a96a-70a9-413e-70a9-6a3e70a96a70"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "9c826b9c-826b-499c-826b-9c9c826b9c82"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "7e8ea2a3-8ea2-4e7e-8ea2-a38e8ea2a38e"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "61c6d691-c6d6-4161-c6d6-9161c6d6d691c"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "cf85f64e-f85f-4bcf-85f6-4ecf85f64ecf"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "c334f24f-34f2-4ec3-34f2-f24c334f24f2"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "40d62ef7-d62e-4f40-d62e-f740d62ef7d62"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "cec84ed8-c84e-4ecec-84ed-8d8cec84ed8c8"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "9b23ca47-b23c-49b9-23ca-479b23ca479b"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "0b15422b-1542-40b0-1542-2b0b15422b154"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "fa5cfb97-5cfb-4efa-5cfb-975fa5cfb975"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "f5388bc4-388b-4ff5-388b-c4f5388bc438"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "2071e6eb-71e6-4207-71e6-eb2071e6eb71"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "5e186ffa-186f-45e1-86ff-a186e186ffa1"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "15473c14-473c-4154-73c1-415473c14573"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "935b8e4c-5b8e-4935-b8e4-c5935b8e4c5b"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "e1da51aa-1da5-4ee1-da51-aae1da51aa1d"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "ecddc028-cddc-4eec-ddc0-28ecddc028cd"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "6ebe3f2b-be3f-476e-be3f-2b6ebe3f2b6e"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "c2b82792-b827-4ec2-b827-92c2b82792b8"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "cecdb7e5-cedb-4fce-cedb-7e5cecdb7e5ce"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "f4ad1e4d-4ad1-4ff4-ad1e-4df4ad1e4d4ad"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "a6ec9620-ec96-4ca6-ec96-20a6ec9620ec"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "ecbc8434-bc84-4eec-bc84-34ecbc8434bc"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "bafcd4c3-afcd-47ba-fcd4-c3bafcd4c3afc"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "e26ea563-6ea5-4ce2-6ea5-63e26ea5636e"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "ddbd06b0-bd06-4ddbd-06b0-bd06ddbd06b0bd"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "12e8d81e-e8d8-4e12-e8d8-1e12e8d81e8d8"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "a66da1b6-6da1-46a6-da1b-66a66da1b66d"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "76d3e48e-d3e4-476d-3e48-ed76d3e48ed3"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "8c663d07-c663-48c6-663d-078c663d07c66"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "80b0a2a5-b0a2-480b-b0a2-a580b0a2a580"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "c9b7237f-b723-4ec9-b723-7fc9b7237fc9"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "b346c80d-46c8-4bb3-46c8-0db346c80d46"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "e50f3e96-0f3e-4e50-f3e9-60e50f3e960f"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "f84e5a74-4e5a-4ff8-4e5a-74f84e5a744e"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "df73e472-f73e-4ddf-73e4-72df73e472f73"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "c2eefbb9-ee1f-4ec2-eefb-b9c2eefbb9ee"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "c55e2850-5e28-4cc5-5e28-50c55e28505e"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "7d146ea9-146e-47d1-46ea-97146ea9146e"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "fc7d1f19-7d1f-4dfc-7d1f-19fc7d1f197d"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "a827268d-8272-4ba8-8272-68a827268d82"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "abbf2867-bbf2-45ab-bf28-67abbf2867bf"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "ae4ccbf0-e4cc-49ae-4ccbf0-e4ccae4ccbf0e"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "f130b2e5-30b2-4ff1-30b2-e530f130b2e5"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "fbc6782f-bc67-48fb-c678-2ffbc6782fb"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "a14f618d-4f61-4ba1-4f61-8da14f618d4f6"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "e0e7bd5a-0e7b-4ce0-e7bd-5ae0e0e7bd5a0"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "f58d269d-8d26-4df5-8d26-9df58d269d8d"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "e028d0c3-28d0-4ce0-28d0-c3e028d0c328"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "d0e07825-0e07-4ed0-e078-25d0e078250e"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "b9ad4947-ad49-4bb9-ad49-47b9ad4947ad"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "dcb9e01f-cb9e-4edc-b9e0-1fdcb9e01fcb"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "f0e103dd-0e10-4ff0-e103-ddf0e103ddf0"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "d9270794-2707-4dd9-9270-94d927079427"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "d57f1bb6-7f1b-4ed5-7f1b-b6d57f1bb67f"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "c52bbdca-2bbd-4cc5-2bbd-cac52bbdca2b"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "8cfbbede-cfbe-488c-fbbede-cfbe8cfbbede4"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "9ffda4a2-ffda-4f9f-fda4a2-ffda9ffda4a2f"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "e08d7f2d-08d7-4ee0-8d7f-2de08d7f2d08"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "8a504c72-a504-48a8-a504-c728a504c72a"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "4d3a597c-d3a5-4e4d-3a59-7c4d3a597cd3"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "59e6b6d3-9e6b-45b9-e6b6-d359e6b6d359"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "b8de85cb-8de8-4bb8-de85-cbb8b8de85cb8"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "c104ce8c-04ce-4fc1-04ce-8cc104ce8c04"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "d3eb573a-eb57-4cd3-eb57-3ad3eb573aeb"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "89b2e85f-9b2e-4889-b2e8-5f89b2e85f9b"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "ca46c751-a46c-4eca-46c7-51ca46c751a4"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "d3b75b7a-3b75-4dd3-b75b-7ad3b75b7a3b"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "b2fc7e0e-fc7e-4bb2-fc7e-0eb2fc7e0efc"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "e6ca6fe0-ca6f-4ee6-ca6f-e0e6ca6fe0ca"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "bd9e86c7-9e86-4ebd-9e86-c7bd9e86c79e"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "ea2c42bb-a2c4-4eea-2c42-bbea2c42bba2c"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "a0e8e036-0e8e-4ca0-e8e0-36a0e8e0360e"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "9f67411c-f674-49d9-f674-11c9f67411cf"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "b8d3b570-8d3b-4bb8-d3b5-708b8d3b5708"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "97fb15e4-fb15-49b7-fb15-e497fb15e4fb"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "f19ca14a-9ca1-4cf1-9ca1-4af19ca14a9c"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "64e7695c-e769-4b64-e769-5c64e7695ce7"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "bd8bf38a-d8bf-44bd-8bf3-8abd8bf38ad8"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "cb2f1d09-b2f1-4ecb-2f1d-09cb2f1d09b2"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "fcfcea4e-cfea-4afc-fcea-4efcfcea4ecfe"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "efb7a6d0-fb7a-4cef-b7a6-d0efb7a6d0fb"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "edbccc56-dbcc-4ced-bccc-56edbccc56db"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "bac8be2c-ac8b-4bba-c8be-2cbac8be2cac"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "b15dfba4-5dfb-4eb1-5dfb-a4b15dfba45d"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "0e3e04fc-3e04-40e3-e04f-c0e3e04fc3e"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "f36b741e-6b74-4ef3-6b74-1ef36b741e6b"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "d9b2c5fb-9b2c-4bd9-b2c5-fbd9b2c5fbd9"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "c9d7aaf9-7aaf-4ec9-d7aa-f9c9d7aaf97a"
    },
    {
        "name": "Vintage Charm",
        "colors": [
            { "name": "Charming Gold", "hex": "#ffd700" },
            { "name": "Elegant Black", "hex": "#000000" },
            { "name": "Deep Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "a2e6df5b-6df5-4ca2-e6df-5ba2e6df5b6df"
    },
    {
        "name": "Mystic Tranquility",
        "colors": [
            { "name": "Tranquil Teal", "hex": "#008080" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Ethereal White", "hex": "#ffffff" },
            { "name": "Midnight Black", "hex": "#000000" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "ab65f199-b65f-4fab-65f1-99ab65f199b6"
    },
    {
        "name": "Sunset Reflections",
        "colors": [
            { "name": "Reflective Blue", "hex": "#0077b6" },
            { "name": "Sunset Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Golden Sun", "hex": "#ffd700" },
            { "name": "Twilight Purple", "hex": "#8a2be2" }
        ],
        "id": "4cceb61d-ceb6-4c4c-ceb6-1d4cceb61dce"
    },
    {
        "name": "Desert Mirage",
        "colors": [
            { "name": "Desert Sand", "hex": "#edc9af" },
            { "name": "Twilight Blue", "hex": "#343c4e" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Mystic Purple", "hex": "#800080" },
            { "name": "Moonlit Silver", "hex": "#c0c0c0" }
        ],
        "id": "ab6ef7f3-b6ef-44ab-6ef7-f3ab6ef7f3b6"
    },
    {
        "name": "Autumn Radiance",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "f5aadc7a-aadc-4ef5-aadc-7af5aadc7aa7"
    },
    {
        "name": "Vintage Opulence",
        "colors": [
            { "name": "Opulent Gold", "hex": "#ffd700" },
            { "name": "Velvet Black", "hex": "#000000" },
            { "name": "Royal Red", "hex": "#8b0000" },
            { "name": "Platinum Silver", "hex": "#e5e4e2" },
            { "name": "Ivory Cream", "hex": "#fff8dc" }
        ],
        "id": "6e2e2a88-2e2a-46e6-2a88-82e2e2a88e2a"
    },
    {
        "name": "Mystic Wilderness",
        "colors": [
            { "name": "Wilderness Green", "hex": "#228b22" },
            { "name": "Enchanted Purple", "hex": "#800080" },
            { "name": "Mysterious Black", "hex": "#000000" },
            { "name": "Mystic Blue", "hex": "#4682b4" },
            { "name": "Ethereal White", "hex": "#ffffff" }
        ],
        "id": "6b5d7e3c-5d7e-46b5-d7e3-c46b5d7e3c5d"
    },
    {
        "name": "Sunset Oasis",
        "colors": [
            { "name": "Sunny Yellow", "hex": "#fff44f" },
            { "name": "Desert Orange", "hex": "#ff4500" },
            { "name": "Crimson Red", "hex": "#dc143c" },
            { "name": "Sandy Beige", "hex": "#f4a460" },
            { "name": "Turquoise Blue", "hex": "#00ced1" }
        ],
        "id": "bc1a5d32-1a5d-4ebc-1a5d-32bc1a5d321a"
    },
    {
        "name": "Autumn Dreams",
        "colors": [
            { "name": "Autumn Orange", "hex": "#ff6600" },
            { "name": "Harvest Gold", "hex": "#daa520" },
            { "name": "Rustic Brown", "hex": "#8b4513" },
            { "name": "Golden Yellow", "hex": "#ffd700" },
            { "name": "Crimson Red", "hex": "#dc143c" }
        ],
        "id": "d53b08d8-3b08-4ed5-3b08-d8d53b08d83b"
    }
]

# Your JSON data


collection.insert_many(data)
