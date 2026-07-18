# Buffer Overflow

### 📄 Description
This is a buffer overflow challenge: you have to leverage one or more vulnerabilities to reach the `print_flag` function.

Use static and dynamic analysis to determine the input to provide.

### ⚙ How to run
```bash
./buffer
```

### ⛔ Rules
- You cannot patch the executable.
- You cannot modify the program control flow with gdb to jump directly to the flag function.
- The challenge must be solved by providing a valid input.
- If you think you are breaking these rules with your solution, please ask the teachers.