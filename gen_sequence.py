import random
import copy

data = {
      "guapea position": ["guapea", "enshuffla (regular)", "vacila", "vacila-enshuffla" , "vacilala", "panké", "prima (regular)", "prima con hermana", "sombrero", "montana", "denodo"]
    , "guapea": ["enshuffla (regular)", "vacila", "vacila-enshuffla" , "vacilala", "panké", "prima (regular)", "sombrero", "montana", "denodo"]
    , "dile que non": ["guapea position"]
    , "dile que non position": ["dile que non", "penala", "rodeo", "rodeolala", "sacala", "paseo poratraz"]
    , "dile que si": ["dile que non"]
    , "enshuffla (regular)": ["dile que non position"]
    , "enshuffla double": ["dile que non position"]
    , "vacila": ["dile que non position"]
    , "vacilala": ["dile que non position"]
    , "panké": ["guapea position"]
    , "denodo": ["dile que non position right handed"]
    , "prima (regular)": ["guapea position"]
    , "vacila-enshuffla": ["dile que non position"]
    , "rodeolala": ["dile que non position"]
    , "rodeo": ["dile que non position"]
    , "sombrero": ["dile que non"]
    # , "prima con familia": ["dile que non position right handed"] # only for rueda
    , "prima con hermana": ["dile que non position"]
    , "paseo poratraz": ["guapea position"]
    , "sacala": ["dile que non position"]
    , "montana": ["dile que non"]
    , "dile que non position right handed": ["dile que non"]
    , "penala": ["guapea position"]
}

def random_next(start_pos):
    if start_pos in data:
        possible_moves = data[start_pos]
        return random.choice(possible_moves)
    else:
        return None

def is_silent_move(move):
    is_redundant= "position" in move
    if is_redundant:
        return True
    else:
        return False


def gen_sequence(length, start_pos="guapea", explicit=False):
    iterator = 0
    if not start_pos:
        start_pos = random.choice(list(data.keys()))
    last_move = start_pos
    sequence = []
    while iterator <= length:
        next_move = ''
        if not is_silent_move(last_move) or explicit:
            sequence.append(last_move)
            iterator = iterator + 1
        while True:
            next_move = random_next(last_move)
            if next_move != sequence[-1]:
                break
            if len(sequence) > 2 and next_move != sequence[-2]:
                break
        if not next_move:
            break
        last_move = copy.deepcopy(next_move)
    return sequence

def gen_longest_unique_path(start_pos="guapea", start_length=20, iterations=1000, explicit=False):
    sequences = {}
    for _ in range(iterations):
        seq = gen_sequence(start_length, start_pos, explicit)
        sequences[len(set(seq))] = seq
    max_key = max(list(sequences.keys()))
    longest_sequence = sequences[max_key]
    return longest_sequence

lp = gen_longest_unique_path(start_pos="guapea", start_length=20, iterations=1000, explicit=False)

for n, move in enumerate(lp):
  print(str(n + 1) + '. ' + move.capitalize())