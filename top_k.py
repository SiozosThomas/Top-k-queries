import sys

class Top_k():

    def __init__(self):
        self.files = []
        self.maximums = []
        self.stats = []
        self.k = 0
        self.max_UB = 0
        self.categories = []
        self.get_arguments()
        self.file_tuples = []
        self.top_count = 0
        self.number_of_accesses = 0
        self.final_result = []
        for i in range(0, len(self.files)):
            self.file_tuples.append(self.read_file(self.files[i]))
        self.aggregation()

    def get_k(self):
        return self.k

    def get_categories(self):
        return self.categories

    def get_number_of_accesses(self):
        return self.number_of_accesses

    def get_final_result(self):
        return self.final_result

    def get_arguments(self):
        if len(sys.argv) < 4:
            print("Something wrong with command line arguments!")
            exit()
        for i in range(1, len(sys.argv) - 1):
            file_number = int(sys.argv[i])
            if file_number == 1:
                print("Give me the file's path with Rebounds: ")
                self.categories.append("Rebounds")
                file_path = input()
                self.files.append(file_path)
            elif file_number == 2:
                print("Give me the file's path with Assists: ")
                self.categories.append("Assists")
                file_path = input()
                self.files.append(file_path)
            elif file_number == 3:
                print("Give me the file's path with Steals: ")
                self.categories.append("Steals")
                file_path = input()
                self.files.append(file_path)
            elif file_number == 4:
                print("Give me the file's path with Blocks: ")
                self.categories.append("Blocks")
                file_path = input()
                self.files.append(file_path)
            elif file_number == 5:
                print("Give me the file's path with Points: ")
                self.categories.append("Points")
                file_path = input()
                self.files.append(file_path)
            else:
                print("Wrong arguments!")
                exit()
        self.k = int(sys.argv[len(sys.argv) - 1])

    def read_file(self, file):
        with open(file, encoding = "utf8") as file:
            for line in file:
                yield line

    def aggregation(self):
        access_line = []
        T = 0
        while True:
            self.max_UB = 0
            try:
                for i in range(0, len(self.file_tuples)):
                    line = next(self.file_tuples[i]).split(',')
                    if self.number_of_accesses == 0:
                        self.maximums.append(int(line[1]))
                    T += round(float(int(line[1]) / self.maximums[i]), 6)
                    access_line.append({"id": int(line[0]),\
                                        "stat": round(float(int(line[1])\
                                        / self.maximums[i]), 6)})
                self.update_upper_bound(access_line)
                access_line = self.find_same_id_in_same_access(access_line)
                self.update_stats(access_line, T)
                self.set_max_UB()
                self.check_lower_and_upper()
                if self.top_count >= self.k:
                    break
            except StopIteration:
                if self.top_count < self.k:
                    for i in range(self.top_count, self.k):
                        self.final_result.append(self.stats[0])
                        self.stats.pop(0)
                break
            T = 0
            access_line.clear()
            self.number_of_accesses += 1

    def update_upper_bound(self, access_line):
        list_number = []
        for i in range(0, len(access_line)):
            list_number.append(i)
        for i in range(0, len(self.stats)):
            upper_bound = 0
            rest = list(set(list_number) - set(self.stats[i]["file"]))
            if rest:
                for j in range(0, len(access_line)):
                    if j in rest:
                        upper_bound += access_line[j]["stat"]
                self.stats[i]["UB"] = round(self.stats[i]["LB"] +\
                                                    upper_bound, 6)

    def set_max_UB(self):
        for i in range(0, len(self.stats)):
            if self.stats[i]["UB"] >= self.max_UB:
                self.max_UB = self.stats[i]["UB"]

    def find_same_id_in_same_access(self, access_line):
        for i in range(0, len(access_line)):
            for j in range(i + 1, len(access_line)):
                if i < len(access_line) and j < len(access_line):
                    if access_line[i]["id"] == access_line[j]["id"]:
                        access_line[i]["stat"] += access_line[j]["stat"]
                        access_line.pop(j)
        return access_line

    def update_stats(self, access_line, T):
        find = -1
        for i in range(0, len(access_line)):
            for j in range(0, len(self.stats)):
                if access_line[i]["id"] == self.stats[j]["id"]:
                    find = j
                    break
            if find != -1:
                self.stats[find]["file"].append(i)
                self.stats[find]["LB"] = round(self.stats[find]["LB"] +\
                                        access_line[i]["stat"], 6)
                find = -1
            else:
                self.stats.append({"id": access_line[i]["id"],\
                                    "LB": round(access_line[i]["stat"], 6),\
                                    "UB": round(T, 6), "file": [i]})
        self.stats.sort(key=lambda k: k['LB'], reverse = True)

    def check_lower_and_upper(self):
        if self.stats[0]["LB"] >= self.max_UB:
            self.final_result.append(self.stats[0])
            self.stats.pop(0)
            self.top_count += 1

sys.argv = [sys.argv[0], 1, 2, 5]
top = Top_k()
results = top.get_final_result()
categories = top.get_categories()
s = categories[0]
for i in range(1, len(categories)):
    s += ", " + categories[i]
print("Number of accesses: " + str(top.get_number_of_accesses()))
nba = open("data/2017_ALL.csv", "r", encoding = "utf-8")
print(str(top.get_k()) + " Best players for season 2017 in categories(" + s +\
                                                                    "):")
lines = 0
ranking = []
with open("data/2017_ALL.csv", encoding = "utf8") as file:
    for line in file:
        for i in range(0, len(results)):
            if results[i]["id"] == lines:
                line_split = line.split(',')
                ranking.append({"rank": i + 1, "name": line_split[1]})
        lines += 1
ranking.sort(key=lambda k: k['rank'])
for player in ranking:
    print(str(player["rank"]) + ". " + player["name"])
