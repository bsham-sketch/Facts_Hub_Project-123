# In-memory data storage (no database)
FACTS = [
    {
        'id': 1,
        'title': 'Water covers 71% of Earth',
        'content': 'About 71% of the Earth\'s surface is covered by water, with the oceans holding about 96.5% of all Earth\'s water.',
        'category': 'Science',
        'created_at': '2024-01-01T10:00:00Z'
    },
    {
        'id': 2,
        'title': 'Honey never spoils',
        'content': 'Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.',
        'category': 'Food',
        'created_at': '2024-01-02T10:00:00Z'
    },
    {
        'id': 3,
        'title': 'Bananas are berries',
        'content': 'Botanically speaking, bananas are considered berries, while strawberries are not. A berry is a fleshy fruit produced from the single ovary of a flower.',
        'category': 'Food',
        'created_at': '2024-01-03T10:00:00Z'
    },
    {
        'id': 4,
        'title': 'Octopuses have three hearts',
        'content': 'Two hearts pump blood to the gills, while the third pumps it to the rest of the body. The heart that delivers blood to the body actually stops beating when the octopus swims.',
        'category': 'Science',
        'created_at': '2024-01-04T10:00:00Z'
    },
    {
        'id': 5,
        'title': 'The Eiffel Tower grows in summer',
        'content': 'Due to thermal expansion, the Eiffel Tower can be up to 15 cm taller during hot summer days when the iron heats up and expands.',
        'category': 'Industry',
        'created_at': '2024-01-05T10:00:00Z'
    },
    {
        'id': 6,
        'title': 'Vitamin C deficiency causes scurvy',
        'content': 'Scurvy, a disease caused by vitamin C deficiency, was once common among sailors on long voyages. Symptoms include fatigue, swollen gums, and joint pain.',
        'category': 'Health',
        'created_at': '2024-01-06T10:00:00Z'
    },
    {
        'id': 7,
        'title': 'The first computer bug was a real bug',
        'content': 'In 1947, engineers found a moth trapped in a relay of the Harvard Mark II computer. They taped it to their logbook with the note "First actual case of bug being found."',
        'category': 'Technology',
        'created_at': '2024-01-07T10:00:00Z'
    },
    {
        'id': 8,
        'title': 'Lightning strikes about 8 million times per day',
        'content': 'On average, lightning strikes the Earth about 100 times every second, which adds up to roughly 8.6 million strikes per day.',
        'category': 'Science',
        'created_at': '2024-01-08T10:00:00Z'
    },
    {
        'id': 9,
        'title': 'The Great Wall of China is not visible from space',
        'content': 'Despite popular belief, the Great Wall of China is generally not visible to the unaided eye from space, especially from low Earth orbit.',
        'category': 'Industry',
        'created_at': '2024-01-09T10:00:00Z'
    },
    {
        'id': 10,
        'title': 'Apples float in water',
        'content': 'Apples are about 25% air, which makes them less dense than water and allows them to float.',
        'category': 'Food',
        'created_at': '2024-01-10T10:00:00Z'
    },
    {
        'id': 11,
        'title': 'The universe is 13.8 billion years old',
        'content': 'According to the Big Bang theory, the universe began approximately 13.8 billion years ago with a rapid expansion from a hot, dense state.',
        'category': 'Science',
        'created_at': '2024-01-11T10:00:00Z'
    },
    {
        'id': 12,
        'title': 'The human brain uses 20% of the body\'s energy',
        'content': 'Although the brain only makes up about 2% of body weight, it consumes approximately 20% of the body\'s energy and oxygen supply.',
        'category': 'Science',
        'created_at': '2024-01-12T10:00:00Z'
    },
    {
        'id': 13,
        'title': 'Diamonds are made of compressed carbon',
        'content': 'Diamonds form deep within the Earth under extreme pressure and temperature conditions, where carbon atoms crystallize into the hardest known natural material.',
        'category': 'Science',
        'created_at': '2024-01-13T10:00:00Z'
    },
    {
        'id': 14,
        'title': 'The Great Pyramid was built with over 2 million stone blocks',
        'content': 'The Great Pyramid of Giza, built around 2560 BC, consists of approximately 2.3 million limestone and granite blocks, each weighing an average of 2.5 tons.',
        'category': 'Industry',
        'created_at': '2024-01-14T10:00:00Z'
    },
    {
        'id': 15,
        'title': 'Concrete is the most widely used building material',
        'content': 'Concrete is the second most consumed substance on Earth after water. It\'s used in everything from buildings and bridges to roads and dams.',
        'category': 'Industry',
        'created_at': '2024-01-15T10:00:00Z'
    },
    {
        'id': 16,
        'title': 'The first skyscraper was built in 1885',
        'content': 'The Home Insurance Building in Chicago, completed in 1885, is considered the world\'s first skyscraper at 10 stories tall, using a steel frame construction.',
        'category': 'Industry',
        'created_at': '2024-01-16T10:00:00Z'
    },
    {
        'id': 17,
        'title': 'Regular exercise reduces risk of chronic diseases',
        'content': 'Engaging in regular physical activity can reduce the risk of heart disease, stroke, type 2 diabetes, and certain types of cancer by up to 50%.',
        'category': 'Health',
        'created_at': '2024-01-17T10:00:00Z'
    },
    {
        'id': 18,
        'title': 'Sleep is essential for memory consolidation',
        'content': 'During sleep, especially during REM sleep, the brain processes and consolidates memories from the day, helping with learning and cognitive function.',
        'category': 'Health',
        'created_at': '2024-01-18T10:00:00Z'
    },
    {
        'id': 19,
        'title': 'The human body has 206 bones',
        'content': 'At birth, humans have around 270 bones, but many fuse together as we grow. By adulthood, we have 206 bones, with the smallest being in the ear and the largest in the thigh.',
        'category': 'Health',
        'created_at': '2024-01-19T10:00:00Z'
    },
    {
        'id': 20,
        'title': 'Garlic has natural antibiotic properties',
        'content': 'Garlic contains allicin, a compound with antimicrobial properties that can help fight bacteria, viruses, and fungi. It has been used medicinally for thousands of years.',
        'category': 'Health',
        'created_at': '2024-01-20T10:00:00Z'
    },
    {
        'id': 21,
        'title': 'Dark chocolate can improve brain function',
        'content': 'Dark chocolate contains flavonoids that can improve blood flow to the brain, potentially enhancing cognitive function and reducing the risk of neurological diseases.',
        'category': 'Health',
        'created_at': '2024-01-21T10:00:00Z'
    },
    {
        'id': 22,
        'title': 'Coffee beans are actually seeds',
        'content': 'What we call coffee "beans" are actually the seeds of the coffee plant\'s fruit, which are processed, roasted, and ground to make coffee.',
        'category': 'Food',
        'created_at': '2024-01-22T10:00:00Z'
    },
    {
        'id': 23,
        'title': 'Honey is made from flower nectar',
        'content': 'Bees collect nectar from flowers and store it in their honey stomach. Enzymes in the honey stomach break down the nectar, which is then regurgitated and fanned by bees to evaporate water, creating honey.',
        'category': 'Food',
        'created_at': '2024-01-23T10:00:00Z'
    },
    {
        'id': 24,
        'title': 'Chocolate was once used as currency',
        'content': 'The ancient Mayans and Aztecs used cacao beans as currency and also consumed them as a bitter drink, often mixed with spices and water.',
        'category': 'Food',
        'created_at': '2024-01-24T10:00:00Z'
    },
    {
        'id': 25,
        'title': 'The world\'s most expensive coffee comes from cat droppings',
        'content': 'Kopi Luwak is made from coffee beans that have been eaten and excreted by civet cats. The digestive process is believed to improve the coffee\'s flavor.',
        'category': 'Food',
        'created_at': '2024-01-25T10:00:00Z'
    },
    {
        'id': 26,
        'title': 'The first website went live in 1991',
        'content': 'The first website was created by Tim Berners-Lee at CERN and went live on August 6, 1991. It provided information about the World Wide Web project.',
        'category': 'Technology',
        'created_at': '2024-01-26T10:00:00Z'
    },
    {
        'id': 27,
        'title': 'Wi-Fi doesn\'t stand for "Wireless Fidelity"',
        'content': 'Despite popular belief, Wi-Fi is not an acronym for "Wireless Fidelity." It was created as a catchy brand name by the Wi-Fi Alliance.',
        'category': 'Technology',
        'created_at': '2024-01-27T10:00:00Z'
    },
    {
        'id': 28,
        'title': 'The first computer mouse was made of wood',
        'content': 'Invented by Douglas Engelbart in 1964, the first computer mouse had a wooden shell with two metal wheels and was called an "X-Y position indicator for a display system."',
        'category': 'Technology',
        'created_at': '2024-01-28T10:00:00Z'
    },
    {
        'id': 29,
        'title': 'The internet was originally called ARPANET',
        'content': 'The internet began as ARPANET (Advanced Research Projects Agency Network) in 1969, a project funded by the U.S. Department of Defense to connect computers across different locations.',
        'category': 'Technology',
        'created_at': '2024-01-29T10:00:00Z'
    },
    {
        'id': 30,
        'title': 'The Milky Way galaxy is 100,000 light-years across',
        'content': 'Our home galaxy, the Milky Way, is a barred spiral galaxy approximately 100,000 light-years in diameter and contains 100-400 billion stars.',
        'category': 'Universe',
        'created_at': '2024-01-30T10:00:00Z'
    },
    {
        'id': 31,
        'title': 'A day on Venus is longer than its year',
        'content': 'Venus takes 243 Earth days to rotate once on its axis but only 225 Earth days to orbit the Sun, making its day longer than its year.',
        'category': 'Universe',
        'created_at': '2024-01-31T10:00:00Z'
    },
    {
        'id': 32,
        'title': 'Neutron stars are incredibly dense',
        'content': 'A neutron star is so dense that a teaspoon of its material would weigh about 6 billion tons on Earth. They form when massive stars collapse at the end of their life cycle.',
        'category': 'Universe',
        'created_at': '2024-02-01T10:00:00Z'
    },
    {
        'id': 33,
        'title': 'There are more trees on Earth than stars in the Milky Way',
        'content': 'Scientists estimate there are about 3 trillion trees on Earth, compared to approximately 100-400 billion stars in our galaxy.',
        'category': 'Universe',
        'created_at': '2024-02-02T10:00:00Z'
    },
    {
        'id': 34,
        'title': 'Light from the Sun takes 8 minutes to reach Earth',
        'content': 'The Sun is approximately 93 million miles (150 million kilometers) away from Earth. Light travels at 186,282 miles per second, taking about 8 minutes and 20 seconds to reach us.',
        'category': 'Universe',
        'created_at': '2024-02-03T10:00:00Z'
    },
    {
        'id': 35,
        'title': 'Black holes aren\'t actually holes',
        'content': 'Black holes are regions of spacetime where gravity is so strong that nothing, not even light, can escape. They form when massive stars collapse under their own gravity.',
        'category': 'Universe',
        'created_at': '2024-02-04T10:00:00Z'
    }
]

CATEGORIES = [
    'Science',
    'Industry',
    'Health',
    'Food',
    'Technology',
    'Universe'
]

# Global counter for new facts
next_id = 36
