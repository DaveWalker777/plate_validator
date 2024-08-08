validated_nums = set('1234567890')
validated_letters = set('авекмнорстух')


def validate_nums(plate_element):
    if plate_element in validated_nums:
        return True
    else:
        return False
p

def validate_letters(plate_element):
    if plate_element.lower() in validated_letters:
        return True
    else:
        return False


def validate_len(plate, plate_type):
    valid_lengths = {
        1: [8, 9],
        2: [7, 8],
        3: [8, 9],
        4: [8, 9],
        5: [6, 7, 8]
    }
    return len(plate) in valid_lengths.get(plate_type, [])


def validate_plate(plate, plate_type):
    if not validate_len(plate, plate_type):
        return False

    validation_rules = {
        1: {'nums': [1, 2, 3, 6, 7], 'letters': [0, 4, 5]},
        2: {'nums': [2, 3, 4, 5, 6], 'letters': [0, 1]},
        3: {'nums': [0, 1, 2, 3, 6, 7, 8], 'letters': [4, 5]},
        4: [
            {'nums': [0, 1, 2, 3, 6, 7], 'letters': [4, 5]},
            {'nums': [2, 3, 4, 5, 6, 7], 'letters': [0, 1]},
        ],
        5: [
            {'nums': [1, 2, 3, 4, 5, 6], 'letters': [0]},
            {'nums': [0, 1, 2, 4, 5, 6], 'letters': [3]},
            {'nums': [0, 1, 2, 3, 5, 6], 'letters': [4]},
        ]
    }

    rules = validation_rules.get(plate_type, [])

    if plate_type in [4, 5]:
        for rule in rules:
            valid = True
            for i in range(len(plate)):
                if i in rule['nums']:
                    if not validate_nums(plate[i]):
                        valid = False
                        break
                elif i in rule['letters']:
                    if not validate_letters(plate[i]):
                        valid = False
                        break
            if valid:
                return True
        return False
    else:
        nums_positions = rules.get('nums', [])
        letters_positions = rules.get('letters', [])

        for i in range(len(plate)):
            if i in nums_positions:
                if not validate_nums(plate[i]):
                    return False
            elif i in letters_positions:
                if not validate_letters(plate[i]):
                    return False

        return True

