-- a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
create table if not exists second_table (
    id int,
    name varchar(256),
    score int
);
insert into second_table (1, "John", 10);
insert into second_table (1, "Alex", 3);
insert into second_table (1, "Bob", 14);
insert into second_table (1, "George", 8);