import random
from game_state import *
from player import *

ambient_dialogue = {
    'siren': [
        "The air thickens with her song. You feel it pulling — not your body, but your will. 'Come closer,' she whispers. 'You're already halfway gone.'",
        "They tried to warn you. That was kind of them.",
        "The sea does not take prisoners. Only offerings.",
        "You drift closer with each breath. Even now.",
        "I'm waiting. Whenever you're ready."
    ],
    'hermit': [
        "The sea doesn't forget. Not even the things we wish it would.",
        "I heard her voice once, down near the caves. That was enough. It's why I'm out here now.",
        "The sea hums when she's near. You just have to feel it."
        "Tradition fades over time. It becomes myth. Legend. And then… it's forgotten. Sometimes it comes back to bite us."
        "I knew a man who listened too long. Gone now, probably."
        "Some doors are better left closed."
        "There's a hollow in the cliffs. Used to be a smugglers' den, or so they say. Now the caves just echo."
    ],
    'bartender': [
        "Storm's creeping in again. Bad weather brings old things ashore.",
        "Folks used to stay late. Some for hours. Not anymore.",
        "You hear the sea singing at night too, don't you? I don't believe in fairytales, but this… this feels different",
        "That storm the other night? Took more than just boats.",
        "Some faces blur with time. Others… stay clear as glass.",
        "You been out near the caves? Don't linger there."
        "You been out past the cliffs? Not much out there but fog and rock. Still… some folks say they hear singing from that way."
    ],
    'sailor': [
        "This fog isn't just weather. Some nights it carries things back — voices, smells, memories. Stuff you didn't know you lost.",
        "Ships don't come back right anymore. If they come back at all.",
        "There's something under the water that doesn't move with the tide.",
        "Tied a bell to my bunk. Still don't sleep much."
        "She called to me once. Thought it was the wind. I just try to ignore it now."
        "I don't walk near that side of the shore anymore. Something about the way the caves echo. Feels like it's hiding something."
    ],
    'marla': [
        "Ever feel like we forget things on purpose? Like we're all just pretending none of this is happening?",
        "I see lights on the beach sometimes. Blue ones. No one else does.",
        "You ever have dreams that don't feel like yours?",
        "I used to sing to the sea. Now it sings back.",
        "Everyone here feels it. Most pretend they don't."
        "Sometimes I see footprints near the cliffs. Just one set. Leading toward the rocks."
    ]
}

askable_dialogue = {
    'siren': {
        'shrine': "You stood before the shrine — the old stone buried in the forest. It spoke, didn't it? The ones who hear it never leave unchanged.",
        'journal': "He wrote of dreams, of voices on the water. Thought the pages would protect him. They didn't.",
        'artifact': "Her voice ripples through the mist. 'The carved stone opened a door. Not all doors can be shut.'",
        'sapphire bracelet': "She smiles faintly. 'That bracelet shimmered on another's wrist once. She followed the melody too. Walked straight into the tide.'",
        'cliffs': "I used to wander the cliffs all the time. I like it better in here though.",
        'caves': "The caves are my home. They'll be yours soon too.",
        'girl': "She came to me willingly. Heard the call before she knew what it meant. She sang with me beneath the waves, her voice lost to the air, but not to the sea. She's home now. Happier, perhaps, than she ever was on land."
    },
    'hermit': {
        'artifact': "A carved stone. That's no relic — it's a piece of something older. Something that still breathes beneath the tide. Something our ancestors carried. A token.",
        'journal': "Words in that book weren't written by one man. Not really. By the end he was a whole new person. There are warnings in there. Most people don't realize that though. By the time he realized, it was too late.",
        'shrine': "The shrine? That's not just for prayer. It's a boundary marker. A Gate. Older folks tell tales offerings brought by our ancestors to keep us safe from the sea. Most say all but myths now.",
        'sapphire bracelet': "It shines like it's calling, doesn't it? That's how it lures you. Pretty things always go missing around here.",
        'cliffs': "Down by the cliffs… the caves… that's where things start to slip. Your thoughts. Your footing. Your grip on what's real. Something lives beneath them — something our ancestors tried to protext us from.",
        'caves': "Legends tell of an ancient creature that dwells there. People used to worship near the shrine. They would make offering to spare their people.",
        'ancestors': "Our people made a pact with the sea. Old tales, sure. But some debts never wash away.",
        'girl': "She was curious, like most who vanish. Asked questions no one should ask. I warned her. Told her the tides remember those who listen too long. But she followed the melody down to the shore one night... and the sea kept her."
    },
    'bartender': {
        'shrine': "I heard people mention it here and there. No one seems to know much about it though. Probably just some old superstitious thing.",
        'journal': "That journal's been drifting around for years. Some of the ink seems to move if you stare too long. Most folks stop reading before the end.",
        'artifact': "Last time one showed up, the guy who found it walked into the sea and never looked back. Folks said he smiled the whole way.",
        'sapphire bracelet': "A girl used to wear one just like it, would drop by all the time. She sat right over yonder. Sang to herself, quiet. Disappeared without a trace. Sometimes people swear they can still hear her on the beach at night.",
        'cliffs': "Used to be just a scenic spot. Lately, folks say they hear voices from the caves. Singing, even. I don't go near the cliffs anymore, not since that girl vanished.",
        'caves': "I hear people talk about them occasionaly. Folks say that's where the girl went missing all those year ago.",
        'girl': "Not many remember. It's just a story to most people. She used to hang around here though. Would drop in, sit right over there. Hum to herself. One day, she just stopped showing up though. Some say her footprints ended at the edge of the water, down near the caves."
    },
    'sailor': {
        'shrine': "I heard of something like that up in the woods. Never went to check it out personally.",
        'journal': "That old sea journal? Belonged to a fisherman years back. Wrote strange things near the end. His boat left, and no one saw him again.",
        'fisherman': "I was the only one who really knew him. Didn't have many friends. Once he heard the song, he never turned back though. I try to warn people of it if I can.",
        'artifact': "We found one washed up after a storm. Boat sank the next day. Superstition, maybe — but I'd toss it.",
        'sapphire bracelet': "Saw a trinket like that once. Worn by a girl who used to hum out here near the docks. One morning, just… wasn't there anymore",
        'cliffs': "Fog rolls in thicker down there. Messes with your senses. I once thought I heard someone crying out past the rocks. But no one was there. Just the waves. Sometimes the caves echo though.",
        'caves': "Nobody goes near the caves. Everytime somebody does, we never see 'em again. Rough waters down there, and some say it's a trap.",
        'girl': "Used to see her out here all the time. Pretty little thing. She'd stare out past the breakers like she was looking for something no one else could see. I tried to warn her. Never saw her again.",
        'song': "Old folklore mostly. The kind of thing you don't believe until you see… or hear. People say that those who hear it never recover… I was one of the few who did."
    },
    'marla': {
        'shrine': "I used to walk past it every day when I lived up in the hills. Always gave me the creeps. My mom would always tell me never to touch it.",
        'journal': "Old book? I've seen it before. People find it, swear it's nonsense — some people seem to change their minds though.",
        'artifact': "I saw one like that in a dream — half-buried in wet sand, humming like it was alive.",
        'sapphire bracelet': "That bracelet… real pretty ain't it. Sapphire I think. Belonged to a girl who lived here. Quiet type. Used to walk the shore at night, always humming. Then one day, she was just… gone.",
        'cliffs': "The caves there hum. Not like wind or water, but… like breath. Like something down there is alive, waiting. You feel it too, right?",
        'caves': "I've heard of people going missing down there. Didn't used to be a problem, but weather's been worse, and some say it's been haunted ever since the girl went missing.",
        'girl': "She wasn't from around here, but this place stuck to her. Used to walk the beach alone, humming to herself. Pretty voice, but there was something hollow in it, like she was halfway gone. One night, she followed that song—and never came back.",
        'song': "The sea seems to sing to some people. Lures them in slowly, but surely. Nobody knows why. Not many who hear it survive though."
    },
}


class DialogueHandler:
    def talk_to(npc_name) -> str:
        lines = ambient_dialogue.get(npc_name.lower())
        if not lines:
            return f"You don't see anyone named {npc_name} here."
        else:
            return random.choice(lines)
    def ask_about(npc_name, topic) -> str:
        askable_lines = askable_dialogue.get(npc_name.lower())
        
        if not askable_lines:
            return f"You don't see anyone named {npc_name} here."
        
        response = askable_lines.get(topic.lower())
        if response:
            return response
        
        return f"{npc_name.capitalize()} doesn't seem to know anything about {topic}."