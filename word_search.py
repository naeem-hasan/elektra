import random


class WordSearch(object):
    def __init__(self, x=0, y=0, **kwargs):
        self.x = x
        self.y = y
        self.grid_ids = range(self.x * self.y)
        self.grid = ['' for i in self.grid_ids]
        self.difficulty_level = kwargs.get('difficulty', 5)

    def difficulty(self, level):
        self.difficulty_level = level

    def get_difficulty(self):
        grid_directions = [0]
        if self.difficulty_level > 0:
            grid_directions.append(2)
        if self.difficulty_level > 1:
            grid_directions.append(1)
        if self.difficulty_level > 2:
            grid_directions += [6, 7]
        if self.difficulty_level > 3:
            grid_directions.append(4)
        if self.difficulty_level > 4:
            grid_directions += [3, 5]
        return grid_directions

    def direction_coordinate(self, inital_location, direction):
        directions = {}
        directions['right'] = 1
        directions['down'] = self.x
        directions['left'] = -directions['right']
        directions['up'] = -directions['down']

        direction_move = (directions['right'],
                          directions['right'] + directions['down'],
                          directions['down'],
                          directions['left'] + directions['down'],
                          directions['left'],
                          directions['left'] + directions['up'],
                          directions['up'],
                          directions['right'] + directions['up'])

        old_coordinate = self.get_coordinate(inital_location)
        new_location = inital_location + direction_move[direction]
        new_coordinate = self.get_coordinate(new_location)

        if old_coordinate and new_coordinate:
            if all(new_coordinate[i] in (old_coordinate[i] + j for j in xrange(-1, 2)) for i in xrange(2)) and 0 < new_location < self.x * self.y:
                return new_location

    def format_input_list(self, word_list=None, word_length_min=3, word_length_max=None, **kwargs):
        if word_length_max is None:
            word_length_max = (min(self.x, self.y) + (self.x + self.y) / 2) / 2

        return [i for i in word_list if word_length_min < len(i) <= word_length_max]

    def word_variations(self, words, min_length=1):
        all_letters = ''.join(words)
        word_list = []
        while len(word_list) < min_length:

            for word in words:
                original_word = word
                word_len = len(word)
                word_range = xrange(word_len)

                for repeat in xrange(random.randint(0, 4)):

                    # Remove random letters from the word - word = wrd, wod, etc
                    remove_letters = random.sample(word_range, random.randint(0, word_len / 3))
                    num_removed_letters = 0
                    for index in remove_letters:
                        word = word[:index - num_removed_letters] + word[index + 1 - num_removed_letters:]
                        num_removed_letters += 1

                    # Replace random letters in word - word = ward, wore, wond, etc
                    word_section = sorted(random.sample(word_range, 2))
                    if word_section[0] or word_section[1] != word_len:

                        new_word = word[random.randint(0, word_section[0]):random.randint(word_section[1], word_len)]
                        new_word_len = len(new_word)

                        for replacement in xrange(random.randint(0, new_word_len / 2)):
                            replacement_index = random.randint(0, new_word_len - 1)
                            new_letter = random.choice(all_letters)

                            new_word = new_word[:replacement_index] + new_letter + new_word[replacement_index + 1:]

                            # Only add to list if
                            if new_word != original_word:
                                word_list.append(new_word)
        return word_list

    def debug_grid(self):
        count = 0
        max_len = len(str(self.x * self.y - 1))
        for i in range(self.y):
            print ' '.join(str(i + count).zfill(max_len) for i in range(self.x))
            count += self.x

    def get_coordinate(self, id=0, **kwargs):
        ignore_limit = kwargs.get('ignore', False)

        # location_x = id % self.x
        location_y = id / self.x
        if location_y <= self.y or ignore_limit:
            return (id % self.x, id / self.x)

    @staticmethod
    def direction_to_text(direction):
        return ('right', 'down-right', 'down', 'down-left', 'left', 'left-up', 'up', 'right-up')[direction]

    def generate(self, num_iterations, second_pass=True, fill_empty_values=True, **kwargs):
        capitalise_non_matches = False
        input_words = kwargs.get('words')
        grid_directions = self.get_difficulty()
        self.used_words = {}

        for stage in xrange(1 + second_pass):

            # Detect which word list to use depending on the pass
            if stage and self.used_words:
                word_list = self.word_variations(self.used_words.keys(), num_iterations)
            else:
                word_list = input_words

            for i in range(num_iterations):

                # Cancel loop when out of words
                if not word_list and not stage:
                    break

                random.shuffle(grid_directions)

                initial_word_list = []

                # Build list of matching words
                if word_list:
                    while not initial_word_list:
                        # Pick a coordinate, and fill with letter if empty
                        current_coordinate = random.choice(self.grid_ids)
                        using_new_letter = False
                        if not self.grid[current_coordinate]:
                            self.grid[current_coordinate] = random.choice(word_list)[0]
                            using_new_letter = True
                            if capitalise_non_matches and stage:
                                self.grid[current_coordinate] = self.grid[current_coordinate].upper()

                        # Create a selection of words
                        initial_word_list = [word for word in word_list if self.grid[current_coordinate] in word[0]]
                        initial_word_list = random.sample(initial_word_list, min(len(initial_word_list), num_iterations))

                else:
                    initial_word_list = []

                valid_word = None

                if initial_word_list:
                    for direction_index in xrange(len(grid_directions)):

                        direction = grid_directions[direction_index]

                        next_direction = current_coordinate
                        matching_word_list = initial_word_list
                        random.shuffle(matching_word_list)
                        # Loop while there are matching words
                        count = 0
                        while matching_word_list:
                            # Cancel if invalid direction
                            if next_direction is None:
                                matching_word_list = []
                                break

                            # Loop for each word
                            delete_count = 0
                            for i in xrange(len(matching_word_list)):

                                i -= delete_count

                                # Add to invalid words if the letter doesn't match
                                if self.grid[next_direction] and self.grid[next_direction] != matching_word_list[i][count]:
                                    del matching_word_list[i]
                                    delete_count += 1

                                    if not matching_word_list:
                                        break

                                # If reached the length of a word, it's succeeded
                                elif count >= len(matching_word_list[i]) - 1:

                                    # Choose whether to stop here or continue for a longer word
                                    if random.uniform(0, 1) < max(0.25, 1.0 / (max(1, len(matching_word_list) / 2))) or count > (self.x + self.y) / random.choice(xrange(2, 5)):
                                        valid_word = matching_word_list[i]
                                        matching_word_list = []
                                        break
                                    else:
                                        del matching_word_list[i]
                                        delete_count += 1

                            next_direction = self.direction_coordinate(next_direction, direction)
                            count += 1
                            # Update the grid data
                        if valid_word is not None:

                            used_word = word_list.pop(word_list.index(valid_word))
                            if not stage:
                                self.used_words[used_word] = (current_coordinate, direction)

                            next_direction = current_coordinate
                            for i in range(1, len(valid_word)):

                                letter = valid_word[i]
                                next_direction = self.direction_coordinate(next_direction, direction)
                                if not self.grid[next_direction]:
                                    if stage and capitalise_non_matches:
                                        letter = letter.upper()
                                    self.grid[next_direction] = letter

                                # If the data doesn't match the word, this shouldn't happen
                                elif self.grid[next_direction] != letter:
                                    self.grid[next_direction] = '-'

                            break

                        # Remove single remaining letters if the word was not completed
                        elif len(grid_directions) - 1 == direction_index:
                            if using_new_letter:
                                self.grid[current_coordinate] = ''

        # Fill with random letters
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if capitalise_non_matches:
            alphabet = alphabet.upper()
        if fill_empty_values:
            for i in xrange(len(self.grid)):
                if not self.grid[i]:
                    self.grid[i] = random.choice(alphabet)

    def display(self):
        count = 0
        totalgrid = []
        for i in xrange(self.y):
            current_row = []
            for j in xrange(self.x):
                letter = self.grid[count]
                if not letter:
                    letter = ' '
                current_row.append(letter)
                count += 1
            totalgrid.append(current_row)

        return totalgrid

    def solutions(self):
        words = self.used_words
        solutions_ = []
        for word in words:
            x_, t_ = self.get_coordinate(words[word][0]), self.direction_to_text(words[word][1])
            solutions_.append([word, x_, t_])

        return solutions_
