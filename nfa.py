"""
NFA (Non-Deterministic Finite Automaton) Program
--------------------------------------------------
Takes states, symbols, transitions, start state, final states,
and an input string from the user. Displays the transition table
and checks whether the string is accepted or rejected.
"""

def main():
    print("----- NFA Program -----")

    n = int(input("Enter number of states: "))
    states = [input(f"Enter name of state {i + 1}: ").strip() for i in range(n)]

    symbols = input("Enter input symbols separated by space (e.g. 0 1): ").split()

    transitions = {}
    print("\nEnter transitions one by one.")
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

    start_state = input("\nEnter start state: ").strip()
    final_states = set(input("Enter final states separated by space: ").split())

    # ---- Display Transition Table ----
    print("\n----- NFA Transition Table -----")
    header = f"{'State':<10}" + "".join(f"{sym:<15}" for sym in symbols)
    print(header)
    for state in states:
        row = f"{state:<10}"
        for sym in symbols:
            next_states = transitions.get((state, sym), [])
            row += f"{'{' + ','.join(next_states) + '}':<15}"
        print(row)

    # ---- Check Input String ----
    test_string = input("\nEnter string to check: ").strip()

    current_states = {start_state}
    for ch in test_string:
        next_states = set()
        for state in current_states:
            next_states.update(transitions.get((state, ch), []))
        current_states = next_states
        if not current_states:
            break

    print("\n----- Result -----")
    if current_states & final_states:
        print(f"String '{test_string}' is ACCEPTED by the NFA.")
    else:
        print(f"String '{test_string}' is REJECTED by the NFA.")


if __name__ == "__main__":
    main()
