"""
NFA to DFA Conversion Program (Subset Construction Method)
--------------------------------------------------------------
Takes an NFA (states, symbols, transitions, start state, final states)
from the user, converts it into an equivalent DFA, displays the DFA
transition table, and checks whether an input string is accepted.
"""

def main():
    print("----- NFA to DFA Conversion (Subset Construction) -----")

    n = int(input("Enter number of NFA states: "))
    states = [input(f"Enter name of state {i + 1}: ").strip() for i in range(n)]

    symbols = input("Enter input symbols separated by space (e.g. 0 1): ").split()

    transitions = {}
    print("\nEnter NFA transitions one by one.")
    print("Format: state symbol next_state1,next_state2,...")
    print("Type 'done' when finished.\n")
    while True:
        line = input("Transition (or 'done'): ").strip()
        if line.lower() == "done":
            break
        parts = line.split()
        if len(parts) != 3:
            print("Invalid format. Use: state symbol next_states")
            continue
        state, symbol, next_states = parts
        transitions[(state, symbol)] = next_states.split(",")

    start_state = input("\nEnter NFA start state: ").strip()
    final_states = set(input("Enter NFA final states separated by space: ").split())

    # ---- Subset Construction ----
    def move(state_set, symbol):
        result = set()
        for s in state_set:
            result.update(transitions.get((s, symbol), []))
        return frozenset(result)

    def name(state_set):
        return "{" + ",".join(sorted(state_set)) + "}" if state_set else "phi"

    start = frozenset([start_state])
    dfa_states = [start]
    dfa_transitions = {}
    unprocessed = [start]

    while unprocessed:
        current = unprocessed.pop(0)
        for sym in symbols:
            nxt = move(current, sym)
            dfa_transitions[(current, sym)] = nxt
            if nxt and nxt not in dfa_states:
                dfa_states.append(nxt)
                unprocessed.append(nxt)

    dfa_final_states = [s for s in dfa_states if s & final_states]

    # ---- Display DFA Transition Table ----
    print("\n----- Converted DFA Transition Table -----")
    header = f"{'State':<20}" + "".join(f"{sym:<20}" for sym in symbols)
    print(header)
    for s in dfa_states:
        row = f"{name(s):<20}"
        for sym in symbols:
            nxt = dfa_transitions.get((s, sym), frozenset())
            row += f"{name(nxt):<20}"
        print(row)

    print(f"\nDFA Start State   : {name(start)}")
    print(f"DFA Final State(s): {[name(s) for s in dfa_final_states]}")

    # ---- Check Input String on Converted DFA ----
    test_string = input("\nEnter string to check: ").strip()

    current = start
    for ch in test_string:
        current = dfa_transitions.get((current, ch), frozenset())
        if not current:
            break

    print("\n----- Result -----")
    if current in dfa_final_states:
        print(f"String '{test_string}' is ACCEPTED by the converted DFA.")
    else:
        print(f"String '{test_string}' is REJECTED by the converted DFA.")


if __name__ == "__main__":
    main()
