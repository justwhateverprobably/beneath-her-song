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
        "I heard her voice once. That was enough. It's why I'm out here now.",
        "The sea hums when she's near. You just have to feel it."
        "Tradition fades over time. It becomes myth. Legend. And then... it's forgotten. Sometimes it comes back to bite us."
        "I knew a man who listened too long. Gone now, probably."
        "Some doors are better left closed. Some open anyways."
    ],
    'bartender': [
        "Storm's creeping in again. Bad weather brings old things ashore.",
        "Folks used to stay late. Some for hours. Not anymore.",
        "You hear the sea singing at night too, don't you? I don't believe in fairytales, but this... this is different",
        "That storm the other night? Took more than just boats. Folks around here are starting to get uncomfortable with all this weather.",
        "Some faces blur with time. Others… stay clear as glass.",
        "You been out to the cliffs? Don't linger there. More people been going missing around the cave."
    ],
    'sailor': [
        "This fog isn't just weather. Some nights it carries things back — voices, smells, memories. Stuff you didn't know you lost.",
        "Ships don't come back right anymore. If they come back at all.",
        "There's something under the water that doesn't move with the tide.",
        "Tied a bell to my bunk. Still don't sleep much."
        "She called to me once. Thought it was the wind. I just try to ignore it now."
    ],
    'marla': [
        "Ever feel like we forget things on purpose? Like we're all just pretending none of this is happening?",
        "I see lights on the beach sometimes. Blue ones. No one else does.",
        "You ever have dreams that don't feel like yours?",
        "I used to sing to the sea. Now it sings back.",
        "Everyone here feels it. Most pretend they don't."
    ]
}

askable_dialogue = {
    'siren': {
        'shrine': "You stood before the shrine — the old stone buried in the forest. It spoke, didn't it? The ones who hear it never leave unchanged.",
        'journal': "He wrote of dreams, of voices on the water. Thought the pages would protect him. They didn't.",
        'artifact': "Her voice ripples through the mist. 'The carved stone opened a door. Not all doors can be shut.'",
        'bracelet': "She smiles faintly. 'That bracelet shimmered on another's wrist once. She followed the melody too. Walked straight into the tide.'",
    },
    'hermit': {
        'shrine': "A carved stone. That's no relic — it's a piece of something older. Something that still breathes beneath the tide.",
        'journal': "Words in that book weren't written by one man. They're warnings, not stories. Most people don't realize that.",
        'artifact': "The shrine? That's not just for prayer. It's a boundary marker. A Gate. Older folks tell tales offerings brought by our ancestors to keep us safe from the sea. Most say all but myths now.",
        'bracelet': "It shines like it's calling, doesn't it? That's how it lures you. Pretty things always go missing around here.",
    },
    'bartender': {
        'shrine': "I heard people mention it here and there. No one seems to know much about it though. Probably just some old superstitious thing.",
        'journal': "That journal's been drifting around for years. Some of the ink seems to move if you stare too long. Most folks stop reading before the end.",
        'artifact': "Last time one showed up, the guy who found it walked into the sea and never looked back. Folks said he smiled the whole way.",
        'bracelet': "A girl used to wear one just like it, would drop by all the time. She sat right over yonder. Sang to herself, quiet. Disappeared without a trace. Sometimes people swear they can still hear her on the beach at night.",
    },
    'sailor': {
        'shrine': "I heard of something like that up in the woods. Never went to check it out personally.",
        'journal': "That old sea journal? Belonged to a fisherman years back. Wrote strange things near the end. His boat left, and no one saw him again.",
        'artifact': "We found one washed up after a storm. Boat sank the next day. Superstition, maybe — but I'd toss it.",
        'bracelet': "Saw a trinket like that once. Worn by a girl who used to hum out here near the docks. One morning, just... wasn't there anymore",
    },
    'marla': {
        'shrine': "I used to walk past it every day when I lived up in the hills. Always gave me the creeps. My mom would always tell me never to touch it.",
        'journal': "Old book? I've seen it before. People find it, swear it's nonsense — some people seem to change their minds though.",
        'artifact': "I saw one like that in a dream — half-buried in wet sand, humming like it was alive.",
        'bracelet': "That bracelet... real pretty ain't it. Sappire I think. Belonged to a girl who lived here. Quiet type. Used to walk the shore at night, always humming. Then one day, she was just... gone.",
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