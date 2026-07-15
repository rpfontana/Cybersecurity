# Description
# Ita To World Cup 2026

## Context

The FIFA World Cup 2026 is just around the corner and the 48 qualified national teams have already been registered into the official bracket manager. As soon as the registration window closes, the system will automatically generate the 12 groups of the tournament, and from that moment on the list of participants will be frozen forever.

There is just one (huge) problem: Italy did not qualify. The Azzurri are out for the third edition in a row, an entire country is in mourning, and a certain die-hard Italian fan — half tifoso, half hacker — has decided that *this time* the blue jersey is going to be on the pitch no matter what. They have spent the last few weeks studying the FIFA bracket manager and they need your help to register the Azzurri into the database before the groups are auto-generated: that is the only objective of this challenge.

Our hacker friend has already spent some time studying the bracket manager and has come back with a very promising lead. By probing the login page they have realised that the portal is affected by a classic *SQL Injection of type *stacked queries* (also called piggy-backed queries) — the kind of attack in which the attacker terminates the original SQL statement and *piggybacks* one or more brand-new statements on the very same call to the database. A clean, beginner-friendly description of how this technique works is available at <https://pentesterlab.com/glossary/stacked-queries>, and that page is exactly the reference your hacker friend used to confirm the finding. To add Italy back to the World Cup, the objective is to insert the value `Italy` into the `teams` table under collumns 'name' before the auto-generation of the groups freezes the bracket forever.

Deep inside the FIFA control room, an automated *Bracket Officer* is on duty around the clock: every couple of seconds it walks down the list of registered nations, double-checks the roster and — when the federation finally calls "registration closed!" — pulls the names out of an urn to compose the twelve groups of the tournament. The Bracket Officer is a creature of pure procedure: it does not question *how* a country ended up on the roster, it just trusts the database. So the moment our beloved Azzurri appear among the registered teams, even just a heartbeat before the draw, the Officer will quietly stamp Italy's name into one of the twelve groups, the giant scoreboard above the entrance of the bracket manager will light up in green-white-red, and a celebration banner will flash across the login page.

Your mission is therefore simple: help the hacker turn their reconnaissance into a working exploit and get Italy back into the World Cup before the bracket is frozen.

## Rules
IN THIS CHALLENGE YOU CANNOT LOOK AT THE webapp FOLDER!

In order to get the points of this challenge, you need to provide a
detailed description of the procedure that you used to get the flag.
Otherwise we account for the flag as read by the web application folder itself.

## Deployment
```bash
# Build the container
docker build --network=host -t cpp/itatoworldcup2026 .

# Start the container (first time)
docker run -d -p "127.0.0.1:8080:5000" --name "itatoworldcup2026" "cpp/itatoworldcup2026"

# Start the container (after first run)
docker start itatoworldcup2026

# Stop the container
docker stop itatoworldcup2026

# Remove the container
docker rm itatoworldcup2026
```

The web application will be reachable at **http://127.0.0.1:8080/**.