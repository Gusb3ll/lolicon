import subprocess
# Lolicon error handling
# Wank wank dicks dicks

class LoliconException(Exception):
    """Raised when there is a fucking lolicon"""
    pass

# Lolicon Main
# Me me big disappointment

def intice():
    """do nothing because weebs are already attracted to underage anime girls"""
    pass

def callthefbi(age: int):
    if age < 15:
        subprocess.run(["call_911"], capture_output=True)
    else:
        raise LoliconException("Probably just something weird happened.")

def main():
    age = input("What's the girl's age? ")
    callthefbi(age)
    
if __name__ == "__main__":
    main()
