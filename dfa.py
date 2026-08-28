"""
DFA (Deterministic Finite Automaton) Program
--------------------------------------------------
Takes states, symbols, transitions, start state, final states,
and an input string from the user. Displays the transition table
and checks whether the string is accepted or rejected.
"""

def main():
    print("----- DFA Program -----")

    n = int(input("Enter number of states: "))
    states = [input(f"Enter name of state {i + 1}: ").strip() for i in range(n)]

    symbols = input("Enter input symbols separated by space (e.g. 0 1): ").split()

    transitions = {}
    print("\nEnter transitions one by one.")
    print("Format: state symbol next_state")
    print("Type 'done' when finished.\n")
    while True:
        line = input("Transition (or 'done'): ").strip()
        if line.lower() == "done":
            break
        parts = line.split()
        if len(parts) != 3:
            print("Invalid format. Use: state symbol next_state")
            continue
        state, symbol, next_state = parts
        transitions[(state, symbol)] = next_state

    start_state = input("\nEnter start state: ").strip()
    final_states = set(input("Enter final states separated by space: ").split())

    # ---- Display Transition Table ----
    print("\n----- DFA Transition Table -----")
    header = f"{'State':<10}" + "".join(f"{sym:<10}" for sym in symbols)
    print(header)
    for state in states:
        row = f"{state:<10}"
        for sym in symbols:
            row += f"{transitions.get((state, sym), '-'):<10}"
        print(row)

    # ---- Check Input String ----
    test_string = input("\nEnter string to check: ").strip()

    current_state = start_state
    valid = True
    for ch in test_string:
        if (current_state, ch) in transitions:
            current_state = transitions[(current_state, ch)]
        else:
            valid = False
            break

    print("\n----- Result -----")
    if valid and current_state in final_states:
        print(f"String '{test_string}' is ACCEPTED by the DFA.")
    else:
        print(f"String '{test_string}' is REJECTED by the DFA.")


if __name__ == "__main__":
    main()
