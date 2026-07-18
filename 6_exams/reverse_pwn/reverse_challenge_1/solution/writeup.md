# 🔑 Reverse Engineering Writeup

Running the binary shows that we need to provide the correct input in order to reach the `print_flag` function:

```text
$ ./reverse
REVERSE ENGINEERING
This is a reverse challenge, you have to provide the correct input for reaching the print_flag function.
Use static and dynamic analysis for determing the correct input to provide.
Solutions based on patching the executable or modyfing the program control flow with gdb will not be considered
Provide a input:
```

The decompiled code reveals the main input check:

```c
printf("Provide a input: ");
__isoc99_scanf(&DAT_00102175, input);

for (i = 0; i < 6; i = i + 1) {
    if ((char)(input[i] + -1) != (char)*(undefined4 *)(pass + (long)(i * 10) * 4)) {
        puts("wrong input!");
        exit(1);
    }
}
```

For each character of the input, the program subtracts `1` and compares the result with a value stored in the `pass` array.

The compared values are read from these offsets:

```text
pass + 0
pass + 40
pass + 80
pass + 120
pass + 160
pass + 200
```

Inspecting the values in memory with Ghidra gives:

```text
46 45 44 43 42 41
```

Interpreting them as ASCII characters gives:

```text
F E D C B A
```

So the program expects `input[i] - 1` to be equal to `FEDCBA`. To get the required input, we add `1` to each character:

```text
FEDCBA -> GFEDCB
```

### 🚩 Flag 

Using `GFEDCB` as input successfully reaches the flag:

```text
Here is your flag! spritz{i:eh66;8e4fjef876=g<769hhh96:j55hj77}
```
