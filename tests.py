import subprocess
import sys
import os


def test_eof_with_file():
    """Test EOF handling with temporary file"""
    test_commands = """
                    SET A 10
                    GET A
                    SET B 20
                    GET B
                    """
    
    with open("test_input.txt", "w") as f:
        f.write(test_commands)

    result = subprocess.run(
        [sys.executable, "main.py"],
        stdin=open("test_input.txt"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    os.remove("test_input.txt")

    print("EOF Test with File Input:")
    print("Output:", result.stdout)
    print("Return code:", result.returncode)
    print()


def test_eof_with_pipe():
    """Test EOF handling using a pipe"""
    test_commands = """
                    SET X 100
                    GET X
                    SET Y 200
                    GET Y
                    """

    result = subprocess.run(
        [sys.executable, "main.py"],
        input=test_commands,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    print("EOF Test with Piped Input:")
    print("Output:", result.stdout)
    print("Return code:", result.returncode)
    print()


def test_invalid_commands():
    """Test handling of invalid commands"""
    invalid_commands = """
                        SET A
                        GET
                        BEGIN TRANSACTION
                        INVALID_CMD
                        HELP ME
                        """
    
    result = subprocess.run(
        [sys.executable, "main.py"],
        input=invalid_commands,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    print("Invalid Commands Test:")
    print("Output:", result.stdout)
    print("Return code:", result.returncode)



if __name__ == '__main__':
    test_eof_with_file()
    test_eof_with_pipe()
    test_invalid_commands()