import random


def create_transaction_ref():
    
    characters = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ]
    
    ref= ''
    num_chars = 9

    while num_chars != 0:
        ref += random.choice(characters)
        num_chars = num_chars - 1
    
    ref_list = list(ref)
    last_char = ref_list[-1]

    current_index = characters.index(last_char)

    if current_index < len(characters) - 1:
            ref_list[-1] = characters[current_index + 1]
    else:
        ref_list[-1] = characters[0]

    ref2 = "".join(ref_list)
    print(f"[{ref}, {ref2}]")

    return [ref, ref2]