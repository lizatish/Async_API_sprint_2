test_data_for_film_search = [
    (
        {'query': 'The Star'},
        {'status': 200, 'length': 50}
    ),
    (
        {'query': 'Mashed potato'},
        {'status': 404, 'length': 1}
    )
]

es_film_works_data = [
    {
        "id": "db594b91-a587-48c4-bac9-5c6be5e4cf33",
        "title": "Star Trek: Starfleet Academy",
        "imdb_rating": 8.1,
        "description": "In this FMV space combat simulator with elements of an adventure game, you play David Forester, a young human cadet at Starfleet Academy who is going through the extensive command training system that uses several simulator scenarios of missions with a variety of ship classes. In addition, you interact with your various classmates with the mundane situations on campus. You also have some meetings with Captain Hikaru Sulu and Pavel Chekov while Captain James T. Kirk assigns the missions. Through various dialogue options and other choices, you shape your story and must prove to yourself, your crew that's prone to infighting and Kirk that you are worthy of the captain's chair. The true test though arrives when your Vulcan member of the bridge crew gets hurt in an explosion. The first signs of a conspiracy that wants to push the Klingons and the Federation into another bloody conflict emerge here. You must also solve the mystery of a living spaceship created by an unknown alien race that uses unique form of communication and either wants to make first contact, or attack.",
        "genres": [
            {
                "id": "120a21cf-9097-479e-904a-13dd7198c1dd",
                "name": "Adventure"
            },
            {
                "id": "6c162475-c7ed-4461-9184-001ef3d9f26e",
                "name": "Sci-Fi"
            },
            {
                "id": "3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff",
                "name": "Action"
            }
        ],
        "actors": [
            {
                "id": "ff2b4d5a-d920-4728-ab21-6f7b3c003e51",
                "full_name": "Brett Donowho"
            },
            {
                "id": "182c5b1a-6377-4b63-a294-996fca98ff49",
                "full_name": "Patricia Skeriotis"
            },
            {
                "id": "39b762d2-9619-4cb1-897e-09aee5f5cc86",
                "full_name": "Julianna Robinson"
            },
            {
                "id": "8045d6ca-718d-4190-b913-49ff1d001c26",
                "full_name": "Chuck Beyer"
            }
        ],
        "writers": [
            {
                "id": "998acbe6-dd4b-4f93-9996-0efac51d5b95",
                "full_name": "Daniel Greenberg"
            },
            {
                "id": "e99d9990-9e6f-40d7-907a-ea98a631de1e",
                "full_name": "Scott Bennie"
            },
            {
                "id": "a1d2a348-f01c-4799-986b-c1681806a04c",
                "full_name": "Brian Freyermuth"
            },
            {
                "id": "d93a93f6-4ff7-4e92-acdd-738a9da1689f",
                "full_name": "Karin Kearns"
            },
            {
                "id": "ebffa4e1-7398-45e6-8338-07ef25d7d4cb",
                "full_name": "Andrew Greenberg"
            },
            {
                "id": "7c6ca6c2-ab64-4103-b490-825fdd232e0c",
                "full_name": "Bill Maxwell"
            },
            {
                "id": "d625b1da-be2e-4776-9768-784641f5de9e",
                "full_name": "Bill Bridge"
            },
            {
                "id": "736d31be-fbdd-4a98-89a4-44dc23ac6bbb",
                "full_name": "Rusty Buchert"
            },
            {
                "id": "8efd4b0d-8760-45e7-ba37-cbbcfe4ba189",
                "full_name": "Diane Carey"
            }
        ],
        "directors": [
            {
                "id": "34e69ed1-68d7-47e5-9621-e4607e2e4f68",
                "full_name": "Martin Denning"
            },
        ],
    },
]
