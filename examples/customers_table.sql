create table customers(
    id integer primary key autoincrement,
    name varchar(50) not null,
    gender varchar(10) check (gender in ('Male', 'Female')),
    email varchar(100) unique,
    phone varchar(50) unique,
    city varchar(50) default 'Bangalore'
)