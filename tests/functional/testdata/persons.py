es_persons_data = [
    {
        'id': 'ff2b4d5a-d920-4728-ab21-6f7b3c003e51',
        'full_name': 'Brett Donowho',
    },
    {
        'id': '182c5b1a-6377-4b63-a294-996fca98ff49',
        'full_name': 'Patricia Skeriotis',
    },
    {
        'id': '998acbe6-dd4b-4f93-9996-0efac51d5b95',
        'full_name': 'Daniel Greenberg',
    },
    {
        'id': '34e69ed1-68d7-47e5-9621-e4607e2e4f68',
        'full_name': 'Martin Denning',
    },
    {
        'id': 'd1507689-c396-4603-89ed-825022d64296',
        'full_name': 'Dwight Schultz',
    },
    {
        'id': '57a471b1-09dc-48fd-ba8a-1211015a0110',
        'full_name': 'Patrick Stewart',
    },
]

test_data_get_film_by_id = [
    ('d1507689-c396-4603-89ed-825022d64296',
     {
         'uuid': 'd1507689-c396-4603-89ed-825022d64296',
         'full_name': 'Dwight Schultz',
         'films': [
             {
                 'role': 'actor',
                 'film_ids': [
                     'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                 ],
             },
         ],
     },
     200,
     True,
     ),
    (
        '998acbe6-dd4b-4f93-9996-0efac51d5b95',
        {
            'uuid': '998acbe6-dd4b-4f93-9996-0efac51d5b95',
            'full_name': 'Daniel Greenberg',
            'films': [
                {
                    'role': 'writer',
                    'film_ids': [
                        'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                    ],
                },
                {
                    'role': 'actor',
                    'film_ids': [
                        'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                    ],
                },
            ],
        },
        200,
        True,
    ),
    ('not_found_id',
     {'detail': 'Person not found'},
     404,
     False,
     ),
]

test_data_get_films_by_person = [
    ('998acbe6-dd4b-4f93-9996-0efac51d5b95',
     [
         {
             'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
             'title': 'Star Trek: Starfleet Academy',
             'imdb_rating': 8.1,
         },
         {
             'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
             'title': 'Star Trek: Elite Force II',
             'imdb_rating': 8.5,
         },
     ],
     200,
     True,
     ),
    (
        'd1507689-c396-4603-89ed-825022d64296',
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5,
            },
        ],
        200,
        True,
    ),
    (
        'not_found_person',

        {'detail': 'Person not found'},
        404,
        False,
    ),
]
test_data_search_persons = [
    (
        '',
        [
            {
                'uuid': 'ff2b4d5a-d920-4728-ab21-6f7b3c003e51',
                'full_name': 'Brett Donowho',
                'films': [
                    {
                        'role': 'actor',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                ],
            },
            {
                'uuid': '182c5b1a-6377-4b63-a294-996fca98ff49',
                'full_name': 'Patricia Skeriotis',
                'films': [
                    {
                        'role': 'actor',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                ],
            },
            {
                'uuid': '998acbe6-dd4b-4f93-9996-0efac51d5b95',
                'full_name': 'Daniel Greenberg',
                'films': [
                    {
                        'role': 'writer',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                    {
                        'role': 'actor',
                        'film_ids': [
                            'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                        ],
                    },
                ],
            },
            {
                'uuid': '34e69ed1-68d7-47e5-9621-e4607e2e4f68',
                'full_name': 'Martin Denning',
                'films': [
                    {
                        'role': 'director',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                ],
            },
            {
                'uuid': 'd1507689-c396-4603-89ed-825022d64296',
                'full_name': 'Dwight Schultz',
                'films': [
                    {
                        'role': 'actor',
                        'film_ids': [
                            'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                        ],
                    },
                ],
            },
            {
                'uuid': '57a471b1-09dc-48fd-ba8a-1211015a0110',
                'full_name': 'Patrick Stewart',
                'films': [
                    {
                        'role': 'writer',
                        'film_ids': [
                            'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                        ],
                    },
                ],
            },
        ],
        True,
    ),
    (
        '?query=patric',
        [
            {
                'uuid': '57a471b1-09dc-48fd-ba8a-1211015a0110',
                'full_name': 'Patrick Stewart',
                'films': [
                    {
                        'role': 'writer',
                        'film_ids': [
                            'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                        ],
                    },
                ],
            },
            {
                'uuid': '182c5b1a-6377-4b63-a294-996fca98ff49',
                'full_name': 'Patricia Skeriotis',
                'films': [
                    {
                        'role': 'actor',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                ],
            },
        ],
        True,
    ),
]

test_data_for_persons_pagination = [
    (
        '?size=1&number=1',
        [
            {
                'uuid': 'ff2b4d5a-d920-4728-ab21-6f7b3c003e51',
                'full_name': 'Brett Donowho',
                'films': [
                    {
                        'role': 'actor',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                ],
            },
        ],
        True,
    ),
    (
        '?size=1&number=3',
        [
            {
                'uuid': '998acbe6-dd4b-4f93-9996-0efac51d5b95',
                'full_name': 'Daniel Greenberg',
                'films': [
                    {
                        'role': 'writer',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                    {
                        'role': 'actor',
                        'film_ids': [
                            'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                        ],
                    },
                ],
            },
        ],
        True,
    ),
    (
        '?size=2&number=2',
        [
            {
                'uuid': '998acbe6-dd4b-4f93-9996-0efac51d5b95',
                'full_name': 'Daniel Greenberg',
                'films': [
                    {
                        'role': 'writer',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                    {
                        'role': 'actor',
                        'film_ids': [
                            'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                        ],
                    },
                ],
            },
            {
                'uuid': '34e69ed1-68d7-47e5-9621-e4607e2e4f68',
                'full_name': 'Martin Denning',
                'films': [
                    {
                        'role': 'director',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                ],
            },
        ],
        True,
    ),
    (
        '?size=2&number=1',
        [
            {
                'uuid': 'ff2b4d5a-d920-4728-ab21-6f7b3c003e51',
                'full_name': 'Brett Donowho',
                'films': [
                    {
                        'role': 'actor',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                ],
            },
            {
                'uuid': '182c5b1a-6377-4b63-a294-996fca98ff49',
                'full_name': 'Patricia Skeriotis',
                'films': [
                    {
                        'role': 'actor',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                ],
            },
        ],
        True,
    ),
    (
        '?size=1&number=-100',
        [
            {
                'uuid': 'ff2b4d5a-d920-4728-ab21-6f7b3c003e51',
                'full_name': 'Brett Donowho',
                'films': [
                    {
                        'role': 'actor',
                        'film_ids': [
                            'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                        ],
                    },
                ],
            },
        ],
        True,
    ),
]
