def print_dfa(q):
    i = 0
    while i < len(q):
        print(q[i].full_repr())
        # print(q[i].nexts)
        for _, next_state in q[i].nexts:
            if next_state not in q:
                q.append(next_state)
        i += 1


def print_diagram(state_machines):
    for literal, state in state_machines.items():
        print()
        print(literal)
        print_dfa([state])
