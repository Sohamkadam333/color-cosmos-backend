from pymongo import MongoClient

# Replace the connection string with your MongoDB Atlas connection string
connection_string = "mongodb+srv://sohamkadam58:gWaUPTqfXyZp6iXC@cluster0.epoajue.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client["color-cosmos"]
collection = db["gradients"]

# Insert the data
data = [
    {
        "id": "f3a7a66d-5f70-4f07-af7f-9f0011c3db89",
        "name": "Lush Greens",
        "colors": [
            {
              "name": "Lime Green",
              "hex": "#32CD32"
            },
            {
                "name": "Forest Green",
                "hex": "#228B22"
            },
            {
                "name": "Green",
                "hex": "#008000"
            },
            {
                "name": "Olive Drab",
                "hex": "#6B8E23"
            }
        ],
        "css": "background: linear-gradient(to bottom, #32CD32, #228B22, #008000, #6B8E23);"
    },
    {
        "id": "ce6075a0-0c38-49d4-ae24-82540de3d4fc",
        "name": "Sunset Serenade",
        "colors": [
            {
              "name": "Gold",
              "hex": "#FFD700"
            },
            {
                "name": "Dark Orange",
                "hex": "#FF8C00"
            },
            {
                "name": "Firebrick",
                "hex": "#B22222"
            },
            {
                "name": "Crimson",
                "hex": "#DC143C"
            },
            {
                "name": "Dark Red",
                "hex": "#8B0000"
            }
        ],
        "css": "background: linear-gradient(to bottom, #FFD700, #FF8C00, #B22222, #DC143C, #8B0000);"
    },
    {
        "id": "14463de9-2a53-4584-b722-2b4a0a75c3f9",
        "name": "Ocean Waves",
        "colors": [
            {
              "name": "Dodger Blue",
              "hex": "#1E90FF"
            },
            {
                "name": "Royal Blue",
                "hex": "#4169E1"
            },
            {
                "name": "Medium Blue",
                "hex": "#0000CD"
            },
            {
                "name": "Navy Blue",
                "hex": "#000080"
            }
        ],
        "css": "background: linear-gradient(to bottom, #1E90FF, #4169E1, #0000CD, #000080);"
    },
    {
        "id": "27be9d8e-6c13-4970-9c49-15e0b5a46c33",
        "name": "Golden Horizon",
        "colors": [
            {
              "name": "Gold",
              "hex": "#FFD700"
            },
            {
                "name": "Goldenrod",
                "hex": "#DAA520"
            },
            {
                "name": "Dark Orange",
                "hex": "#FF8C00"
            },
            {
                "name": "Orange",
                "hex": "#FFA500"
            }
        ],
        "css": "background: linear-gradient(to bottom, #FFD700, #DAA520, #FF8C00, #FFA500);"
    },
    {
        "id": "1361cc12-2a44-4082-bf61-1525ee5a6b19",
        "name": "Winter Frost",
        "colors": [
            {
              "name": "Light Blue",
              "hex": "#ADD8E6"
            },
            {
                "name": "Powder Blue",
                "hex": "#B0E0E6"
            },
            {
                "name": "Sky Blue",
                "hex": "#87CEEB"
            },
            {
                "name": "Light Sky Blue",
                "hex": "#87CEFA"
            },
            {
                "name": "Azure",
                "hex": "#007FFF"
            }
        ],
        "css": "background: linear-gradient(to bottom, #ADD8E6, #B0E0E6, #87CEEB, #87CEFA, #007FFF);"
    },
    {
        "id": "c1f9bf3b-c1a4-4464-9314-d579a0de2f05",
        "name": "Sapphire Night",
        "colors": [
            {
              "name": "Midnight Blue",
              "hex": "#191970"
            },
            {
                "name": "Navy Blue",
                "hex": "#000080"
            },
            {
                "name": "Dark Slate Blue",
                "hex": "#483D8B"
            },
            {
                "name": "Blue",
                "hex": "#0000FF"
            },
            {
                "name": "Deep Sky Blue",
                "hex": "#00BFFF"
            }
        ],
        "css": "background: linear-gradient(to bottom, #191970, #000080, #483D8B, #0000FF, #00BFFF);"
    },
    {
        "id": "7d56b6d2-75c1-4301-bb67-9bf50a9f5ae7",
        "name": "Desert Oasis",
        "colors": [
            {
              "name": "Sandy Brown",
              "hex": "#F4A460"
            },
            {
                "name": "Khaki",
                "hex": "#F0E68C"
            },
            {
                "name": "Pale Goldenrod",
                "hex": "#EEE8AA"
            },
            {
                "name": "Beige",
                "hex": "#F5F5DC"
            },
            {
                "name": "Lemon Chiffon",
                "hex": "#FFFACD"
            }
        ],
        "css": "background: linear-gradient(to bottom, #F4A460, #F0E68C, #EEE8AA, #F5F5DC, #FFFACD);"
    },
    {
        "id": "da69484d-6c99-4090-97cc-daeec91d18ce",
        "name": "Elegant Evening",
        "colors": [
            {
              "name": "Dark Slate Gray",
              "hex": "#2F4F4F"
            },
            {
                "name": "Slate Gray",
                "hex": "#708090"
            },
            {
                "name": "Light Slate Gray",
                "hex": "#778899"
            },
            {
                "name": "Silver",
                "hex": "#C0C0C0"
            },
            {
                "name": "Light Gray",
                "hex": "#D3D3D3"
            }
        ],
        "css": "background: linear-gradient(to bottom, #2F4F4F, #708090, #778899, #C0C0C0, #D3D3D3);"
    },
    {
        "id": "f74d88b6-1eb5-4ff0-981f-9ed5719909c2",
        "name": "Rainbow Burst",
        "colors": [
            {
              "name": "Red",
              "hex": "#FF0000"
            },
            {
                "name": "Orange",
                "hex": "#FFA500"
            },
            {
                "name": "Yellow",
                "hex": "#FFFF00"
            },
            {
                "name": "Green",
                "hex": "#008000"
            },
            {
                "name": "Blue",
                "hex": "#0000FF"
            },
            {
                "name": "Violet",
                "hex": "#EE82EE"
            }
        ],
        "css": "background: linear-gradient(to bottom, #FF0000, #FFA500, #FFFF00, #008000, #0000FF, #EE82EE);"
    },
    {
        "id": "cf005be1-3d6a-4775-a726-774a14bbf862",
        "name": "Mystic Galaxy",
        "colors": [
            {
              "name": "Black",
              "hex": "#000000"
            },
            {
                "name": "Navy Blue",
                "hex": "#000080"
            },
            {
                "name": "Midnight Blue",
                "hex": "#191970"
            },
            {
                "name": "Indigo",
                "hex": "#4B0082"
            },
            {
                "name": "Purple",
                "hex": "#800080"
            },
            {
                "name": "Dark Orchid",
                "hex": "#9932CC"
            }
        ],
        "css": "background: linear-gradient(to bottom, #000000, #000080, #191970, #4B0082, #800080, #9932CC);"
    },
    {
        "id": "ede5a0fb-20e2-4bfe-9b61-5fbff59a6464",
        "name": "Cotton Candy",
        "colors": [
            {
              "name": "Pink",
              "hex": "#FFC0CB"
            },
            {
                "name": "Light Pink",
                "hex": "#FFB6C1"
            },
            {
                "name": "Lavender Blush",
                "hex": "#FFF0F5"
            },
            {
                "name": "Misty Rose",
                "hex": "#FFE4E1"
            }
        ],
        "css": "background: linear-gradient(to bottom, #FFC0CB, #FFB6C1, #FFF0F5, #FFE4E1);"
    },
    {
        "id": "29b02d1a-c4b4-4c62-998c-249774540fa7",
        "name": "Cherry Blossom",
        "colors": [
            {
              "name": "Pink",
              "hex": "#FFC0CB"
            },
            {
                "name": "Light Pink",
                "hex": "#FFB6C1"
            },
            {
                "name": "Light Coral",
                "hex": "#F08080"
            },
            {
                "name": "Salmon",
                "hex": "#FA8072"
            },
            {
                "name": "Tomato",
                "hex": "#FF6347"
            }
        ],
        "css": "background: linear-gradient(to bottom, #FFC0CB, #FFB6C1, #F08080, #FA8072, #FF6347);"
    },
    {
        "id": "c0546b1d-af1e-4629-84f3-5f13cbe1cd0a",
        "name": "Electric Lemonade",
        "colors": [
            {
              "name": "Lemon Chiffon",
              "hex": "#FFFACD"
            },
            {
                "name": "Gold",
                "hex": "#FFD700"
            },
            {
                "name": "Dark Orange",
                "hex": "#FF8C00"
            },
            {
                "name": "Firebrick",
                "hex": "#B22222"
            }
        ],
        "css": "background: linear-gradient(to bottom, #FFFACD, #FFD700, #FF8C00, #B22222);"
    },
    {
        "id": "a397f1c1-e26d-4ee7-88b5-1dbbf24298ac",
        "name": "Crimson Glory",
        "colors": [
            {
              "name": "Crimson",
              "hex": "#DC143C"
            },
            {
                "name": "Firebrick",
                "hex": "#B22222"
            },
            {
                "name": "Dark Red",
                "hex": "#8B0000"
            },
            {
                "name": "Maroon",
                "hex": "#800000"
            }
        ],
        "css": "background: linear-gradient(to bottom, #DC143C, #B22222, #8B0000, #800000);"
    },
    {
        "id": "cf968c3b-26ed-4376-80a7-9c8c87d7a9d2",
        "name": "Lavender Fields",
        "colors": [
            {
              "name": "Lavender",
              "hex": "#E6E6FA"
            },
            {
                "name": "Thistle",
                "hex": "#D8BFD8"
            },
            {
                "name": "Plum",
                "hex": "#DDA0DD"
            },
            {
                "name": "Medium Purple",
                "hex": "#9370DB"
            },
            {
                "name": "Blue Violet",
                "hex": "#8A2BE2"
            }
        ],
        "css": "background: linear-gradient(to bottom, #E6E6FA, #D8BFD8, #DDA0DD, #9370DB, #8A2BE2);"
    }
]

# Your JSON data


collection.insert_many(data)
