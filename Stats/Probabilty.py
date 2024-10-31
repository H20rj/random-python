



from random import getrandbits

def coin_flip_simulation(num_flips):
    tails = getrandbits(num_flips).bit_count()
    heads = num_flips - tails

    print(f'Tails: {tails} Heads: {heads}')
    print(f'Probability of heads: {(heads/num_flips * 100):.2f}%')
    print(f'Probability of tails: {(tails/num_flips * 100):.2f}%')

coin_flip_simulation(1000000000)