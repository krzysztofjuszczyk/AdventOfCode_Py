class CrateStack:
    def __init__(self):
        self.content = []

    def add_item_on_top(self, item):
        self.content.append(item)

    def take_x_crates(self, x, multiple):
        return_crates = self.content[-x:] #take x crates from top of stack
        self.content = self.content[:-x]
        if multiple:
            return return_crates
        else:
            return reversed(return_crates)

    def add_crates(self, crates):
        self.content += crates

    def get_top_content(self):
        return self.content[-1] if len(self.content)>0 else ''



class CargoBay:
    def __init__(self, number_of_crates):
        self.number_of_crates = number_of_crates
        self.crates = [CrateStack() for _ in range(number_of_crates)]

    def add_items_to_crates(self, items):
        for crate, item in zip(self.crates, items):
            if item != ' ':
                crate.add_item_on_top(item)

    def move_items(self, amount, source, target, move_multiple):
        moving_crates = self.crates[source].take_x_crates(amount, move_multiple)
        self.crates[target].add_crates(moving_crates)

    def get_top_stacks(self):
        return_message = ""
        for crate in self.crates:
            return_message += crate.get_top_content()
        return return_message

    def print_crates(self):
        for crate in self.crates:
            print(crate.content)
        print('-----')

with open('./inputs/d5.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry for entry in lines]
number_of_crates = len(lines[0]) // 4

crate_lines = lines[:lines.index('\n')-1]
moving_lines = lines[lines.index('\n')+1:]

for l in crate_lines:
    c = list(l)[1::4]
    print(c)

for m in moving_lines:
    amount, source, target = [int(entry) for entry in m.strip().split(' ') if entry.isdigit() ]
    # t1, amount, t2, source,t3, target = [entry for entry in m.strip().split(' ')]
    # cast amount etc. to int

cargo_bay = CargoBay(number_of_crates)
# everything before the empty line (minus the ' 1   2   3...' line are crate lines)
crate_lines = lines[:lines.index('\n') - 1]
# iterate over the crates from the bottom to the top
for line in reversed(crate_lines):
    items = list(line)[1:-1:4]
    cargo_bay.add_items_to_crates(items)

# everything after the empty line are moving lines
moving_lines = lines[lines.index('\n') + 1:]
for line in moving_lines:
    # cargo_bay.print_crates()
    amount, source, target = [int(entry) for entry in line.strip().split(' ') if entry.isdigit()]
    cargo_bay.move_items(amount, source - 1, target - 1, False)     #set to True if part 2

print(cargo_bay.get_top_stacks())


