from services.url_service import URLService

class Generator():
    def __init__(self):
        self.res = {'1': [], '2': [], '3': [], '4': []}
        return

    def GenerateUserNamesAndFetch(self, name, separators):
        all_names = []
        names = name.split()
        for length in range(2, 5):
            self.generate_combinations([], names, length, length, all_names)

        final_result_name = []
        final_result = []
        for name in all_names:
            for separator in separators:
                if separator != 'both':
                    final_result_name = self.generate_username(name, separator)
                    for name in final_result_name:
                        final_result += URLService.is_username_present(name)
        return final_result

    def GenerateUserNames(self, en_names, separators):
        all_names = []
        en_names = en_names.split()
        for length in range(2, 5):
            self.generate_combinations([], en_names, length, length, all_names)

        final_result = []
        for name in all_names:
            for separator in separators:
                if separator != 'both':
                    final_result += self.generate_username(name, separator)
        return final_result

    def generate_username(self, name, symbol):
        temp = []
        if len(name) == 2:
            for i in range(1, len(name[0])+1):
                for j in range(1, len(name[1])+1):
                    if symbol == '' or symbol == '.':
                        combine1 = f"{name[0][:i].lower()}{symbol}{name[1][:j].lower()}"
                        temp.append(combine1)
                    elif symbol == '_':
                        combine1 = [name[0][:i].lower(), name[1][:j].lower()]
                        temp += self.generate_symbol_names(combine1, symbol)
                    elif symbol == 'both':
                        pass
            return temp
        elif len(name) == 3:
            for i in range(1, len(name[0])+1):
                for j in range(1, len(name[1])+1):
                    for k in range(1, len(name[2])+1):
                        if symbol == '':
                            combine1 = f"{name[0][:i].lower()}{name[1][:j].lower()}{name[2][:k].lower()}"
                            temp.append(combine1)
                        elif symbol == '.':
                            combine1 = f"{name[0][:i].lower()}{symbol}{name[1][:j].lower()}{name[2][:k].lower()}"
                            combine2 = f"{name[0][:i].lower()}{name[1][:j].lower()}{symbol}{name[2][:k].lower()}"
                            temp += [combine1, combine2]
                        elif symbol == '_':
                            combine1 = [name[0][:i].lower(), name[1][:j].lower(), name[2][:k].lower()]
                            temp += self.generate_symbol_names(combine1, symbol)
                        elif symbol == 'both':
                            pass
            return temp
        elif len(name) == 4:
            for i in range(max(len(name[0])-4, 1), len(name[0])+1):
                for j in range(max(len(name[1])-4, 1), len(name[1])+1):
                    for k in range(max(len(name[2])-4, 1), len(name[2])+1):
                        for m in range(max(len(name[3])-4, 1), len(name[3])+1):
                            if symbol == '':
                                combine1 = f"{name[0][:i].lower()}{name[1][:j].lower()}{name[2][:k].lower()}{name[3][:m].lower()}"
                                temp.append(combine1)
                            elif symbol == '.':
                                combine1 = f"{name[0][:i].lower()}{symbol}{name[1][:j].lower()}{name[2][:k].lower()}{name[3][:m].lower()}"
                                combine2 = f"{name[0][:i].lower()}{name[1][:j].lower()}{symbol}{name[2][:k].lower()}{name[3][:m].lower()}"
                                combine3 = f"{name[0][:i].lower()}{name[1][:j].lower()}{name[2][:k].lower()}{symbol}{name[3][:m].lower()}"
                                temp += [combine1, combine2, combine3]
                            elif symbol == '_':
                                combine1 = [name[0][:i].lower(), name[1][:j].lower(), name[2][:k].lower(), name[3][:m].lower()]
                                temp += self.generate_symbol_names(combine1, symbol)
                            elif symbol == 'both':
                                pass
            return temp


    def generate_combinations(self, current_combination, remaining_numbers, min_length, max_length, all_combinations):
        if min_length <= len(current_combination) <= max_length:
            all_combinations.append(current_combination)
        if len(current_combination) >= max_length:
            return
        for i in range(len(remaining_numbers)):
            new_combination = current_combination + [remaining_numbers[i]]
            new_remaining_numbers = remaining_numbers[:i] + remaining_numbers[i+1:]
            self.generate_combinations(new_combination, new_remaining_numbers, min_length, max_length, all_combinations)
    def generate_symbol_names(self, name, symbol):
        merge_name = ''.join(name)
        with_dashes = []
        looplen = len(merge_name)
        if looplen > 10:
            looplen = 10
        for i in range(1, 2**(looplen - 1)):
            binary = bin(i)[2:].zfill(len(merge_name)-1)
            combination = merge_name[0]
            for j in range(len(binary)):
                if binary[j] == '1':
                    combination += symbol
                combination += merge_name[j+1]
            with_dashes.append(combination)
        return with_dashes

    def generate_dot_dash(self, name_array):
        with_dashes = []
        for i in range(1, 2**(len(name_array)-1)):
            binary = bin(i)[2:].zfill(len(name_array)-1)
        combination_dash = name_array[0]
        for j in range(len(binary)):
            if binary[j] == "1":
                combination_dash += name_array[j+1]
            if j == len(binary)-1:
                for k in range(1, len(combination_dash)):
                    if combination_dash[k] != "" and combination_dash[k-1] != "":
                        str = combination_dash[:k] + "." + combination_dash[k:]
                        with_dashes.append(str)
        return with_dashes
