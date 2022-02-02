from functools import total_ordering


@total_ordering
class team:
    def __init__(self, team_id: int):
        self.id = team_id
        self.correct_answers = set()
        self.invalid_answers = {}
        self.penalty_time = 0

    # ordering criteria: (max correct_answers, min penalty_time, min id)
    def __lt__(self, other):
        return (-len(self.correct_answers), self.penalty_time, self.id) < (-len(other.correct_answers), other.penalty_time, other.id)

    def __eq__(self, other):
        return (-len(self.correct_answers), self.penalty_time, self.id) == (-len(other.correct_answers), other.penalty_time, other.id)

    def __str__(self):
        return '{} {} {}'.format(self.id, len(self.correct_answers), self.penalty_time)

    def add_entry(self, ex: int, time: int, res: str):
        if res == 'R' or res == 'U' or res == 'E':
            return None
        if ex not in self.correct_answers:
            if res == 'I':
                self.invalid_answers[ex] = self.invalid_answers.get(ex, 0) + 1
            else:
                self.correct_answers.add(ex)
                self.penalty_time += time + 20 * \
                    self.invalid_answers.get(ex, 0)


M = int(input())

for i in range(M):
    R = int(input())
    marathon: dict[int, team] = {}
    for j in range(R):
        team_id, ex, time, res = [x for x in input().split()]
        team_id = int(team_id)
        ex = int(ex)
        time = int(time)
        if team_id not in marathon:
            marathon[team_id] = team(team_id)
        marathon[team_id].add_entry(ex, time, res)

    results = []
    for t in marathon.values():
        if len(t.correct_answers) > 0:
            results.append(t)
    results.sort()
    print('maraton ' + str(i + 1) + ':')
    print(*results, sep='\n')
