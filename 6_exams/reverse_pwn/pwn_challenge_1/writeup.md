# Buffer Overflow Writeup

Running the binary shows that the goal is to reach the `print_flag` function by providing the correct input:

```text
$ ./buffer
BUFFER OVERFLOW
This is a buffer overflow challenge, you have to leverage one or more vulnerabilities for reaching the print_flag function.
Use static and dynamic analysis for determing the correct input to provide.
The input can be provided with the terminal.
Solutions based on patching the executable or modifying the program control flow with gdb will not be considered
Provide and input for:
```

By decompiling the binary, we can see that the vulnerable function contains a classic stack-based buffer overflow:

```c
undefined8 uVar1;
undefined8 local_1e;
undefined2 local_16;
int local_14;
int local_10;
undefined4 local_c;

local_c = 0x41414141;
local_10 = 0x40404040;
local_14 = 0x40404040;
local_1e = 0;
local_16 = 0;

printf("Provide and input for: ");
fflush(stdout);
__isoc99_scanf(&DAT_001021ae, &local_1e);

if ((local_14 == 0x44434241) && (local_10 == 0x41424344)) {
    uVar1 = 1;
}
```

The input is written into `local_1e`, but there is no proper size check. This allows us to overwrite the following stack variables.

The buffer area before the two checked integers is made of:

```text
local_1e: 8 bytes
local_16: 2 bytes
```

So we need `10` padding bytes before overwriting `local_14` and `local_10`.

The program checks for these values:

```text
local_14 == 0x44434241
local_10 == 0x41424344
```

Because the architecture is little-endian, the bytes must be provided in reverse order:

```text
0x44434241 -> ABCD
0x41424344 -> DCBA
```

Therefore, a valid payload is:

```text
AAAAAAAAAAABCDDCBA
```

It can be split like this:

```text
AAAAAAAAAA + ABCD + DCBA
```

The first `10` characters fill `local_1e` and `local_16`, `ABCD` overwrites `local_14`, and `DCBA` overwrites `local_10`.

Running the binary with this input prints the flag:

```text
Here is your flag! spritz{577ec32fY87bbY5gg:Yb4bbYde51fc82g1:c}
```
