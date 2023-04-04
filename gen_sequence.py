import random
import copy

data = {
      "guapea position": ["guapea", "enshuffla", "vacila", "vacila-enshuffla" , "vacilala", "panké", "prima", "sombrero", "montana", "denodo"]
    , "guapea": ["enshuffla", "vacila", "vacila-enshuffla" , "vacilala", "panké", "prima", "sombrero", "montana", "denodo"]
    , "dile que non": ["guapea position"]
    , "dile que non position": ["dile que non", "penala", "rodeo", "rodeolala", "sacala", "paseo poratraz"]
    , "dile que si": ["dile que non"]
    , "enshuffla": ["enshuffla (regular)", "enshuffla double", "dile que non position"]
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
    , "prima con familia": ["dile que non position right handed"]
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
    is_redundant= "position" in move or "enshuffla" in move
    is_prima = move == "prima"
    if is_redundant or is_prima:
        return True
    else:
        return False


def gen_sequence(length, start_pos="guapea"):
    iterator = 0
    if not start_pos:
        start_pos = random.choice(list(data.keys()))
    last_move = start_pos
    sequence = []
    while iterator <= length:
        if not is_silent_move(last_move):
            sequence.append(last_move)
            iterator = iterator + 1
        next_move = random_next(last_move)
        if not next_move:
            break
        last_move = copy.deepcopy(next_move)
    return sequence

def gen_longest_unique_path(start_pos="guapea", start_length=30, iterations=6000):
    sequences = {}
    for _ in range(iterations):
        seq = gen_sequence(start_length, start_pos)
        sequences[len(set(seq))] = seq
    max_key = max(list(sequences.keys()))
    longest_sequence = sequences[max_key]
    return longest_sequence

lp = gen_longest_unique_path()
print(lp)