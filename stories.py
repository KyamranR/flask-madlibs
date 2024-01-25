"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, code, title, words, text):
        """Create story with words and template text."""
        self.code = code
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    "tale",
    "Once upon a time in",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story_2 = Story(
    "tale_2",
    "High up in the mighty",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """High up in the mighty {place}, explorers stumbled upon a hidden {adjective} {noun}.
       Excitement filled the air as they began to {verb} the {plural_noun} around."""
)

story_3 = Story(
    "tale_3",
    "Deep within the mystical",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Deep within the mystical {place}, a {adjective} {noun} resided.
       It had a unique ability to {verb} and safeguard and filled with {plural_noun}."""
)

stories = {s.code: s for s in [story, story_2, story_3]}