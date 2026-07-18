# 🔑 Writeup

The challenge provides the following encrypted flag:

```text
6a657272686b7b67346a6933725f6c7633715f307a5f7467797968305f76316e7477336e7d
```

The string is clearly hexadecimal. Decoding it from hex to ASCII gives:

```text
jerrhk{g4ji3r_lv3q_0z_tgyyh0_v1ntw3n}
```

The challenge description hints at a simple alphabet shift. Trying a Caesar shift of `-7` gives:

```text
cxkkad{z4cb3k_eo3j_0s_mzrra0_o1gmp3g}
```

This is still not the flag, but the description also mentions a more advanced algorithm using a key. Since the key length is hinted to be seven characters, we can try a Vigenere cipher with the key:

```text
KITCHEN
```
### 🚩 Flag

Decrypting with Vigenere finally reveals the flag:

```text
spritz{m4st3r_ch3f_0f_crypt0_k1tch3n}
```
