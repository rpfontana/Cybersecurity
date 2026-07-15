drop table if exists users;
create table users (
    id integer primary key autoincrement,
    username text not null,
    password text not null
);

drop table if exists teams;
create table teams (
    id integer primary key autoincrement,
    name text not null
);

drop table if exists groups_table;
create table groups_table (
    id integer primary key autoincrement,
    group_name text not null,
    team_name text not null
);

drop table if exists login_attempts;
create table login_attempts (
    id integer primary key autoincrement,
    username text,
    password text,
    ts datetime default current_timestamp
);

drop table if exists status;
create table status (
    id integer primary key,
    generated integer not null default 0
);
