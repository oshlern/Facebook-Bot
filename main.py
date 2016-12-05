import re, random, parser, markov, sys
from parser import Parser
from markov import Markov

# CURRENTLY JUST LEFTOVER GARBAGE

# Markov Chain For Shakespeare Plays
# First Chain: Who is talking - {Othello: {2: Desdemona, 18: Desdemona, ...}, Iago.}

# should line num be half-character
# ~null: {1: Let}, Let: {1: him}, him, {}
# speakers = {'~null': {}, 'Othello': {2: 'Iago', 18: 'Desdemona', ...}, 'Iago': {}}
# speeches = {'Othello': {'lines': {12: 1, 23: 2, 68: 3}, 'words': {'~null': {}, 'hi': {'.': 12, 'there'``}, '.':  }}}
# can Make more sophisticated: what words are said more after certain speakers, speechLengths, etc. or at which point in the speech or dialogue

othello = Parser('Text/othello')
othello.parseText()
generator = Markov(othello.exportInfo())
print generator.generateResponse(sys.argv[1:])
# print generator.generateText()
# print words['emilia']['world']
# print text['words']['iago']['is']
# print speechLengths
