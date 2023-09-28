class Language():
    """Instiates a general langauge card for words."""

    def __init__(self, word_list) -> None:
        self.world_list = word_list

    def get_word(self, idx)->str:
        """Returns the word at its corresponding index based on the word list"""
        word = self.world_list[idx]
        return word
