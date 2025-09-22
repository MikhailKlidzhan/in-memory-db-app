# In-Memory Database Console Application

A Python-based interactive console application that simulates an in-memory database with transaction support.

## Features

- In-Memory Data Storage: Key-value storage with efficient O(1) operations
- Transaction Support: Nested transactions with COMMIT and ROLLBACK capabilities
- Complete Command Set:
  - SET key value - Store key-value pairs
  - GET key - Retrieve values by key
  - UNSET key - Remove key-value pairs
  - COUNTS value - Count occurrences of a value
  - FIND value - Find keys with specific values
  - BEGIN - Start a transaction
  - ROLLBACK - Rollback current transaction
  - COMMIT - Commit current transaction
  - END - Exit application
  - HELP - Show command help

## Project Structure

```text
app/
├── db.py        # Core database implementation logic
├── main.py      # Application entry point and CLI interface
├── tests.py     # Comprehensive EOF and validation testing
└── README.md    # This file
```

## Quick Start

**Clone this repo:**

```bash
git clone https://github.com/MikhailKlidzhan/in-memory-db-app.git
cd in-memory-db-app
```

**Run the application:**

```bash
python3 main.py
```

**Example session:**

```text
> SET name John
> GET name
John
> BEGIN
> SET name Jane
> GET name
Jane
> ROLLBACK
> GET name
John
> END
```

## Testing

```bash
# Run tests including EOF handling
python3 tests.py

# Test with input file
python3 main.py < test_commands.txt
```
