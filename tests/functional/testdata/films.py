es_film_works_data = [
    {
        'id': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
        'title': 'Star Trek: Starfleet Academy',
        'imdb_rating': 8.1,
        'description': 'In this FMV space combat simulator with elements of an adventure game, '
                       'you play David Forester, a young human cadet at Starfleet Academy who is going '
                       'through the extensive command training system that uses several simulator scenarios'
                       ' of missions with a variety of ship classes. In addition, you interact with your various '
                       'classmates with the mundane situations on campus. You also have some meetings with'
                       ' Captain Hikaru Sulu and Pavel Chekov while Captain James T. Kirk assigns the missions.'
                       ' Through various dialogue options and other choices, you shape your story and must prove'
                       ' to yourself, your crew that\'s prone to infighting and Kirk that you are worthy of '
                       'the captain\'s chair. The true test though arrives when your Vulcan member of the bridge '
                       'crew gets hurt in an explosion. The first signs of a conspiracy that wants to push the '
                       'Klingons and the Federation into another bloody conflict emerge here. You must also solve'
                       ' the mystery of a living spaceship created by an unknown alien race that uses unique form of '
                       'communication and either wants to make first contact, or attack.',
        'genres': [
            {
                'id': '120a21cf-9097-479e-904a-13dd7198c1dd',
                'name': 'Adventure',
            },
            {
                'id': '6c162475-c7ed-4461-9184-001ef3d9f26e',
                'name': 'Sci-Fi',
            },
            {
                'id': '3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff',
                'name': 'Action',
            },
        ],
        'genres_names': ['Adventure', 'Sci-Fi', 'Action'],
        'actors': [
            {
                'id': 'ff2b4d5a-d920-4728-ab21-6f7b3c003e51',
                'name': 'Brett Donowho',
            },
            {
                'id': '182c5b1a-6377-4b63-a294-996fca98ff49',
                'name': 'Patricia Skeriotis',
            },
        ],
        'actors_names': ['Brett Donowho', 'Patricia Skeriotis'],
        'writers': [
            {
                'id': '998acbe6-dd4b-4f93-9996-0efac51d5b95',
                'name': 'Daniel Greenberg',
            },
        ],
        'writers_names': ['Daniel Greenberg'],
        'directors': [
            {
                'id': '34e69ed1-68d7-47e5-9621-e4607e2e4f68',
                'name': 'Martin Denning',
            },
        ],
        'directors_names': ['Martin Denning'],
    },
    {
        'id': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
        'title': 'Star Trek: Elite Force II',
        'imdb_rating': 8.5,
        'description': 'After the long return journey of the USS Voyager to the Federation, the elite Hazard Team '
                       'finds themselves declared redundant and disbanded. You play Lt. Munro, the leader of the '
                       'team who is relegated to being an instructor at Starfleet Academy. After years at the'
                       ' unexciting post, your fortunes change dramatically when Capt. Picard himself has the team'
                       ' reassembled and assigned to the Enterprise. The good captain\'s wisdom could not have been'
                       ' better placed as the Enterprise is sent to investigate the loss of contact with the USS '
                       'Dallas. Leading your Hazard Team, you find yourself at the front line when you discover a'
                       ' formidable new enemy who represents a terrible threat to the galaxy and it will require'
                       ' all your courage and cunning to stop it.',
        'genres': [
            {
                'id': '6c162475-c7ed-4461-9184-001ef3d9f26e',
                'name': 'Sci-Fi',
            },
            {
                'id': '3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff',
                'name': 'Action',
            },
            {
                'id': '120a21cf-9097-479e-904a-13dd7198c1dd',
                'name': 'Adventure',
            },
        ],
        'genres_names': ['Adventure', 'Sci-Fi', 'Action'],
        'actors': [
            {
                'id': 'd1507689-c396-4603-89ed-825022d64296',
                'name': 'Dwight Schultz',
            },
            {
                'id': '998acbe6-dd4b-4f93-9996-0efac51d5b95',
                'name': 'Daniel Greenberg',
            },
        ],
        'actors_names': ['Dwight Schultz', 'Daniel Greenberg'],
        'writers': [
            {
                'id': '57a471b1-09dc-48fd-ba8a-1211015a0110',
                'name': 'Patrick Stewart',
            },
        ],
        'writers_names': ['Patrick Stewart'],
        'directors': [],
        'directors_names': [],
    },
]

test_data_for_film = [
    (
        'db594b91-a587-48c4-bac9-5c6be5e4cf33',
        {
            'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
            'title': 'Star Trek: Starfleet Academy',
            'imdb_rating': 8.1,
            'description': 'In this FMV space combat simulator with elements of '
                           'an adventure game, you play David Forester, a young '
                           'human cadet at Starfleet Academy who is going through '
                           'the extensive command training system that uses several '
                           'simulator scenarios of missions with a variety of ship classes. '
                           'In addition, you interact with your various classmates with '
                           'the mundane situations on campus. You also have some meetings '
                           'with Captain Hikaru Sulu and Pavel Chekov while Captain James '
                           'T. Kirk assigns the missions. Through various dialogue options '
                           'and other choices, you shape your story and must prove to yourself, '
                           'your crew that\'s prone to infighting and Kirk that you are '
                           'worthy of the captain\'s chair. The true test though arrives '
                           'when your Vulcan member of the bridge crew gets hurt in an '
                           'explosion. The first signs of a conspiracy that wants to '
                           'push the Klingons and the Federation into another bloody '
                           'conflict emerge here. You must also solve the mystery of '
                           'a living spaceship created by an unknown alien race that '
                           'uses unique form of communication and either wants to make '
                           'first contact, or attack.',
            'genres': [
                {'uuid': '120a21cf-9097-479e-904a-13dd7198c1dd', 'name': 'Adventure'},
                {'uuid': '6c162475-c7ed-4461-9184-001ef3d9f26e', 'name': 'Sci-Fi'},
                {'uuid': '3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff', 'name': 'Action'},
            ],
            'actors': [
                {
                    'uuid': 'ff2b4d5a-d920-4728-ab21-6f7b3c003e51',
                    'full_name': 'Brett Donowho',
                },
                {
                    'uuid': '182c5b1a-6377-4b63-a294-996fca98ff49',
                    'full_name': 'Patricia Skeriotis',
                },
            ],
            'writers': [
                {
                    'uuid': '998acbe6-dd4b-4f93-9996-0efac51d5b95',
                    'full_name': 'Daniel Greenberg',
                }
            ],
            'directors': [
                {
                    'uuid': '34e69ed1-68d7-47e5-9621-e4607e2e4f68',
                    'full_name': 'Martin Denning',
                }
            ],
        },
        {'status': 200, 'is_use_cache': True},
    ),
    (
        'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
        {
            'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
            'title': 'Star Trek: Elite Force II',
            'imdb_rating': 8.5,
            'description': 'After the long return journey of the USS Voyager to '
                           'the Federation, the elite Hazard Team finds themselves '
                           'declared redundant and disbanded. You play Lt. Munro, the '
                           'leader of the team who is relegated to being an instructor '
                           'at Starfleet Academy. After years at the unexciting post, '
                           'your fortunes change dramatically when Capt. Picard himself '
                           'has the team reassembled and assigned to the Enterprise. The '
                           'good captain\'s wisdom could not have been better placed as the '
                           'Enterprise is sent to investigate the loss of contact with the '
                           'USS Dallas. Leading your Hazard Team, you find yourself at the '
                           'front line when you discover a formidable new enemy who represents '
                           'a terrible threat to the galaxy and it will require all your courage '
                           'and cunning to stop it.',
            'genres': [
                {'uuid': '6c162475-c7ed-4461-9184-001ef3d9f26e', 'name': 'Sci-Fi'},
                {'uuid': '3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff', 'name': 'Action'},
                {'uuid': '120a21cf-9097-479e-904a-13dd7198c1dd', 'name': 'Adventure'},
            ],
            'actors': [
                {
                    'uuid': 'd1507689-c396-4603-89ed-825022d64296',
                    'full_name': 'Dwight Schultz',
                },
                {
                    'uuid': '998acbe6-dd4b-4f93-9996-0efac51d5b95',
                    'full_name': 'Daniel Greenberg',
                },
            ],
            'writers': [
                {
                    'uuid': '57a471b1-09dc-48fd-ba8a-1211015a0110',
                    'full_name': 'Patrick Stewart',
                }
            ],
            'directors': [],
        },
        {'status': 200, 'is_use_cache': True},
    ),
    (
        'b1a2aae8-5c9e-4583-b89e-883c0d0c969M',
        {'detail': 'Film not found'},
        {'status': 404, 'is_use_cache': False},
    ),
]

test_data_for_films_pagination = [
    (
        '',
        {'status': 200, 'is_use_cache': True, 'response_length': 2, 'redis_length': 2},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            },
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            }
        ]
    ),
    (
        '?size=2&number=0',
        {'status': 200, 'is_use_cache': True, 'response_length': 2, 'redis_length': 2},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            },
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            }
        ]
    ),
    (
        '?size=-10&number=0',
        {'status': 422, 'is_use_cache': False, 'response_length': 1, 'redis_length': 0},
        {
            'detail': [
                {
                    'loc': [
                        'query',
                        'size'
                    ],
                    'msg': 'ensure this value is greater than or equal to 1',
                    'type': 'value_error.number.not_ge',
                    'ctx': {
                        'limit_value': 1
                    }
                }
            ]
        }
    ),
    (
        '?size=1&number=-500',
        {'status': 200, 'is_use_cache': True, 'response_length': 1, 'redis_length': 1},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            },
        ]
    ),
    (
        '?sizeee=13&nuumber=-500',
        {'status': 200, 'is_use_cache': True, 'response_length': 2, 'redis_length': 2},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            },
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            }
        ]
    ),
]

test_data_for_films_sort = [
    (
        '',
        {
            'status': 200,
            'is_use_cache': True,
            'response_length': 2,
            'redis_length': 2,
            'comparison': 0,
        },
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            },
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            }
        ]
    ),
    (
        '?sort=-imdb_rating',
        {
            'status': 200,
            'is_use_cache': True,
            'response_length': 2,
            'redis_length': 2,
            'comparison': 0,
        },
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            },
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            },
        ]
    ),
    (
        '?sort=imdb_rating',
        {
            'status': 200,
            'is_use_cache': True,
            'response_length': 2,
            'redis_length': 2,
            'comparison': 1,
        },
        [
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            },
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            }
        ]
    ),
    (
        '?sooort=imdb_rating',
        {
            'status': 200,
            'is_use_cache': True,
            'response_length': 2,
            'redis_length': 2,
            'comparison': 0,
        },
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            },
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            }
        ]
    ),
    (
        '?sort=imdb_raaaating',
        {
            'status': 422,
            'is_use_cache': False,
            'response_length': 1,
            'redis_length': 0,
            'comparison': 2,
        },
        {
            'detail': [
                {
                    'loc': [
                        'query',
                        'sort'
                    ],
                    'msg': "unexpected value; permitted: 'imdb_rating', '-imdb_rating'",
                    'type': 'value_error.const',
                    'ctx': {
                        'given': 'imdb_raaaating',
                        'permitted': [
                            'imdb_rating',
                            '-imdb_rating'
                        ]
                    }
                }
            ]
        }
    ),
]

test_data_for_films_filter_nested = [
    (
        {'genres': '3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff'},
        '?filter[genres]=3d8d9bf5-0d90-4353-88ba-4ccc5d2c07ff&size=2&number=0',
        {'status': 200, 'is_use_cache': True, 'response_length': 2, 'redis_length': 2},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            },
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            },
        ]
    ),
    (
        {'genres': '3d8d9bf5-0d90-4353-88ba-4ccc5d2c07f'},
        '?filter[genres]=3d8d9bf5-0d90-4353-88ba-4ccc5d2c07f&size=5&number=0',
        {'status': 404, 'is_use_cache': False, 'response_length': 1, 'redis_length': 0},
        {
            'detail': 'Film not found'
        }
    ),
    (
        None,
        '?filterrr[genres]=3d8d9bf5-0d90-4353-88ba-4ccc5d2c07f&size=2&number=0',
        {'status': 200, 'is_use_cache': True, 'response_length': 2, 'redis_length': 2},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            },
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            },
        ]
    ),
    (
        {'actors': 'd1507689-c396-4603-89ed-825022d64296'},
        '?filter[actors]=d1507689-c396-4603-89ed-825022d64296&size=1&number=0',
        {'status': 200, 'is_use_cache': True, 'response_length': 1, 'redis_length': 1},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            }
        ]
    ),
    (
        {'writers': '57a471b1-09dc-48fd-ba8a-1211015a0110'},
        '?filter[writers]=57a471b1-09dc-48fd-ba8a-1211015a0110&size=1&number=0',
        {'status': 200, 'is_use_cache': True, 'response_length': 1, 'redis_length': 1},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            }
        ]
    ),
    (
        {'directors': '34e69ed1-68d7-47e5-9621-e4607e2e4f68'},
        '?filter[directors]=34e69ed1-68d7-47e5-9621-e4607e2e4f68&size=1&number=0',
        {'status': 200, 'is_use_cache': True, 'response_length': 1, 'redis_length': 1},
        [
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            }
        ]
    ),
    (
        {
            'directors': '34e69ed1-68d7-47e5-9621-e4607e2e4f68',
            'genres': '120a21cf-9097-479e-904a-13dd7198c1dd',
            'writers': '998acbe6-dd4b-4f93-9996-0efac51d5b95',
            'actors': 'ff2b4d5a-d920-4728-ab21-6f7b3c003e51',
        },
        '?size=1&number=0&filter[actors]=ff2b4d5a-d920-4728-ab21-6f7b3c003e51&filter[directors]'
        '=34e69ed1-68d7-47e5-9621-e4607e2e4f68&filter[writers]=998acbe6-dd4b-4f93-9996-0efac51d5b95&filter'
        '[genres]=120a21cf-9097-479e-904a-13dd7198c1dd',
        {'status': 200, 'is_use_cache': True, 'response_length': 1, 'redis_length': 1},
        [
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            }
        ]
    ),
]

test_data_for_films_filter_simple = [
    (
        {'id': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a'},
        '?size=1&number=0&filter[id]=b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
        {'status': 200, 'is_use_cache': True, 'response_length': 1, 'redis_length': 1},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            }
        ]
    ),
    (
        {'id': '87c64348-61a0-4e6c-99c5-a6bd8b0bcbc'},
        '?size=1&number=0&filter[id]=87c64348-61a0-4e6c-99c5-a6bd8b0bcbc',
        {'status': 404, 'is_use_cache': False, 'response_length': 1, 'redis_length': 0},
        {
            'detail': 'Film not found'
        }
    ),
    (
        {'imdb_rating': 8.1},
        '?size=1&number=0&filter[imdb_rating]=8.1',
        {'status': 200, 'is_use_cache': True, 'response_length': 1, 'redis_length': 1},
        [
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            }
        ]
    ),
    (
        {'title': 'Academy'},
        '?size=50&number=0&filter[title]=Academy',
        {'status': 200, 'is_use_cache': True, 'response_length': 1, 'redis_length': 1},
        [
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            }
        ]
    ),
    (
        {'description': 'Dallas'},
        '?size=50&number=0&filter[description]=Dallas',
        {'status': 200, 'is_use_cache': True, 'response_length': 1, 'redis_length': 1},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            }
        ]
    ),
    (
        {
            'description': 'Dallas',
            'title': 'Elite',
            'imdb_rating': 8.5,
            'id': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
        },
        '?size=50&number=0&filter[description]=Dallas&filter[title]=Elite'
        '[imdb_rating]=8.5&filter[id]=b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
        {'status': 200, 'is_use_cache': True, 'response_length': 1, 'redis_length': 1},
        [
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            }
        ]
    ),
]

test_data_for_films_search = [
    (
        '?size=30&number=0&query=Academy',
        {'status': 200, 'is_use_cache': True, 'response_length': 2, 'redis_length': 2},
        [
            {
                'uuid': 'db594b91-a587-48c4-bac9-5c6be5e4cf33',
                'title': 'Star Trek: Starfleet Academy',
                'imdb_rating': 8.1
            },
            {
                'uuid': 'b1a2aae8-5c9e-4583-b89e-883c0d0c969a',
                'title': 'Star Trek: Elite Force II',
                'imdb_rating': 8.5
            }
        ]
    ),
    (
        '',
        {'status': 422, 'is_use_cache': False, 'response_length': 1, 'redis_length': 0},
        {
            'detail': [
                {
                    'loc': [
                        'query',
                        'query'
                    ],
                    'msg': 'field required',
                    'type': 'value_error.missing'
                }
            ]
        }
    ),
    (
        '?query=wqrwqeqweq',
        {'status': 404, 'is_use_cache': False, 'response_length': 1, 'redis_length': 0},
        {'detail': 'Film not found'},
    ),
]
