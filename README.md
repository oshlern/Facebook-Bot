# Facebook Bot

A chat bot for Facebook Messenger as a part of a [hackathon at Parisoma](https://www.eventbrite.com/e/facebook-bot-hackathon-san-francisco-tickets-29295012170)


### Definitions:

**Sentence** `:=` unit of speech, the kind of thing we get as input or output

**Vectorize** `:=` Convert sentence to vector based on the trained vector space representation


### Vectorizing:

Represent each sentence as a vector. Represent movie/story/play(s) as a vector space. Convert between sentences and vectors.


### Distance-Based Subsequent:

Vectorize input, find closest existing vector, and then reply with the next sentence unit that followed it in the script.

  * Limit to consecutive text. Last sentence isn’t an option for input but is an option for output.


### Predictive Function:

Train function on a (possibly vectorized) sentence to the next (possibly vectorized) sentence. This is a usual predictive function. We might want to vectorize inputs and unvectorize outputs such that inputs that are treated as close by the function are actually close. Probably a neural network. 

We should code a separation of input and response. We might be able to train an LSTM that takes in the user's input and the last words it outputted as long term and the usual short term. This could be trained on the previous sentence as input and the sentence as output.

### Text Formats:

**Dialogue**

  * Movies

  * TV Shows

  * Comedies

  * Plays (Shakespeare)

**Writer’s works**

  * Write a story alongside a famous author

Remove stage instructions and such

Lots of text, many different (but similar?) episodes/films/plays etc.

Funny and different, recognizable, conversational?


### Parse Dialogue Text:

Give sample text with labeled `SPEAKER`, `WORDS`, and `JUNK` and record structure so that bot can parse accordingly (super cool)

**_OR_**

Decide strict text format and program parser to fit percisely that




### Problems:
Flexibility of text input size (and output?)

Text input is different from training data

Deterministic (repetitive for same input?) - is this bad?

Typos?
