from typing import Callable
import random


class Creatives:
    _hash_tags = [
        '#coffee', '#homeroasting', '#specialtycoffee', '#liveroast',
        '#coffeetech', '#greencoffee', '#roastupdates', '#roastbot',
        '#autoroast', '#hottop', '#bot', '#splitkeycoffee',
        '#localroasters', '#freshcoffee', '#freshroast', '#iot',
        '#internetroaster'
    ]

    _messages_by_function = {
        'on_start_monitor': [
            "Looks like the roast is starting!",
            "A new roast just started! Live updates to follow...",
            "Let the coffee roasting begin!",
            "Roasting monitors switched on!",
            "Tune-in, drop-out and roast with us!",
            "We're getting ready to begin a new roast!"
        ],
        'on_stop_monitor': [
            "That's a wrap, roast complete.",
            "That conclude this roasting session.",
            "Another roast for the log books.",
            "Coffee roasting completed. Until next time!",
        ],
        'on_first_crack': [
            "Cue the sounds of first crack!",
            "First crack just started!",
            "We've entered first crack.",
            "Our roast is now at first crack.",
            "Pop, Pop! First crack has begun."
        ],
        'on_second_crack': [
            "Entering into second crack.",
            "Hope you like dark roasts, we just hit second crack!",
            "Creeping our way into second crack",
            "Looks like our roasting is almost over. Just heard second crack!"
        ],
        'on_drop': [
            "Weee! Our roast just dropped and is cooling off!",
            "Time to cool down the beans for final weight.",
            "Target temperature reached, time to drop!",
            "Ah, the sweet smell of freshly roasted coffee!"
        ],
        'on_shutdown': [
            "Charting of the roast."
        ],
    }

    @classmethod
    def get_random(cls, func: Callable) -> str:
        name = func.__name__
        options = cls._messages_by_function.get(name, [])
        return random.choice(options)

    @classmethod
    def add_hashtags(cls, current_message: str, max_tags: int = 8, target_length: int = 250) -> str:
        message, remaining_tags = current_message, set(cls._hash_tags)
        target_count, added_count = random.randint(2, max_tags), 0

        while added_count < target_count and len(message) < target_length and remaining_tags:
            added_count += 1
            tag = remaining_tags.pop()
            message += ' ' + tag

        return message
