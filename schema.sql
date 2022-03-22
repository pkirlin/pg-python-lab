drop table if exists users;
create table users (
    userid serial primary key not null,
    firstname varchar(80) not null,
    lastname varchar(80) not null
);
