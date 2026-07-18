# 🔑 Writeup

The login form appears to build an SQL query similar to this one:

```sql
SELECT id, username FROM users WHERE username='user' AND password='password'
```

Since the user input is inserted directly into the query, the password field is vulnerable to SQL injection. In particular, we can use a stacked query to insert `Italy` into the `teams` table.

The username can be any value. In the password field, we can submit:

```sql
'; INSERT INTO teams (name) VALUES ('Italy')--
```

This closes the original string, executes a second query that adds Italy to the database, and comments out the rest of the original query.

### 🚩 Flag

After submitting the payload, the application returns the flag:

```text
spritz{Azzurri_hacked_back_to_the_World_Cup}
```
