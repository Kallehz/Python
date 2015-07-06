# Hangman
#
# Hangman is a two player game that proceeds as follows. One player chooses a word and tells the other player how long it is by writing a dash (-) for each letter in the word. The second player's goal is then to discover which word the first player chose. He does this by guessing letters. If the letter is in the word, the first player writes the letter in its correct positions, by replacing the dashes. If the second player guesses incorrectly 10 times, the first player wins; otherwise, if the second player manages to discover the word, he wins.
#
# As computer scientist we don't want to waste brainpower thinking of words, so what we do is guess the first few letters, and then write a program that matches the partially guessed word to all the words in the english dictionary.
#
# Write a function hangman(dict_file, state, guessed) that takes three strings as parameters. The first string gives the path to a dictionary file, all_words.txt, that contains a list of all the words that can appear in the game, one word per line. The second string contains the state of the game. The state is represented by a sequence of dashes, where the dashes have been replaced for correctly guessed letters. So, for example, if the second player has correctly guessed the letters i and o, the state could be '-------io-'. The third string is a list containing all the letters player two has guessed. The function returns a list of all the possible words the first player might have chosen.
#
# Note that the words will only contain lower case english letters.
#
# Example
#
hangman('[path-to-file]', 's-a--o--s', 'aeiosu'])