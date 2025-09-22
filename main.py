import sys
from db import InMemoryDB


def print_usage():
    print("Available commands:")
    print("SET <key> <value> - Set a key-value pair")
    print("GET <key> - Retrieve a value by key")
    print("UNSET <key> - Remove a key-value pair")
    print("COUNTS <value> - Count keys with the given value")
    print("FIND <value> - Find keys with the given value")
    print("BEGIN - Start a transaction")
    print("ROLLBACK - Rollback the current transaction")
    print("COMMIT - Commit the current transaction")
    print("END - Exit the application")
    print("HELP - Show this help message")


def main():
    db = InMemoryDB()
    print("In-Memory Database Console Application")
    print("Type 'HELP' for available commands, 'END' to exit")

    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue

            parts = line.split()
            cmd = parts[0].upper()

            if cmd == "SET":
                if len(parts) != 3:
                    print("ERROR: SET requires exactly 2 arguments (key value)")
                else:
                    db.set_cmd(parts[1], parts[2])

            elif cmd == "GET":
                if len(parts) != 2:
                    print("ERROR: GET requires exactly 1 argument (key)")
                else:
                    print(db.get_cmd(parts[1]))

            elif cmd == "UNSET":
                if len(parts) != 2:
                    print("ERROR: UNSET requires exactly 1 argument (key)")
                else:
                    db.unset_cmd(parts[1])

            elif cmd == "COUNTS":
                if len(parts) != 2:
                    print("ERROR: COUNTS requires exactly 1 argument (value)")
                else:
                    print(db.counts_cmd(parts[1]))

            elif cmd == "FIND":
                if len(parts) != 2:
                    print("ERROR: FIND requires exactly 1 argument (value)")
                else:
                    keys = db.find_cmd(parts[1])
                    print(" ".join(keys) if keys else "No keys found")

            elif cmd == "BEGIN":
                if len(parts) != 1:
                    print("ERROR: BEGIN takes no arguments")
                else:
                    db.begin()

            elif cmd == "ROLLBACK":
                if len(parts) != 1:
                    print("ERROR: ROLLBACK takes no arguments")
                else:
                    result = db.rollback()
                    if result:
                        print(result)

            elif cmd == "COMMIT":
                if len(parts) != 1:
                    print("ERROR: COMMIT takes no arguments")
                else:
                    result = db.commit()
                    if result:
                        print(result)

            elif cmd == "END":
                if len(parts) != 1:
                    print("ERROR: END takes no arguments")
                else:
                    break

            elif cmd == "HELP":
                if len(parts) != 1:
                    print("ERROR: HELP takes no arguments")
                else:
                    print_usage()

            else:
                print(f"ERROR: Unknown command '{cmd}'. Type 'HELP' for available commands")

            
    except KeyboardInterrupt:
        print("\nApplication interrupted by user")

    finally:
        print("Exiting application")

    
if __name__ == "__main__":
    main()
            

            
