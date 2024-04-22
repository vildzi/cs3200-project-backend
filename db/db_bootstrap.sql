-- This file is to bootstrap a database for the CS3200 project. 

-- Create a new database.  You can change the name later.  You'll
-- need this name in the FLASK API file(s),  the AppSmith 
-- data source creation.
create database libmanagement;

-- Via the Docker Compose file, a special user called webapp will 
-- be created in MySQL. We are going to grant that user 
-- all privilages to the new database we just created. 
-- TODO: If you changed the name of the database above, you need 
-- to change it here too.
grant all privileges on libmanagement.* to 'webapp'@'%';
flush privileges;

-- Move into the database we just created.
-- TODO: If you changed the name of the database above, you need to
-- change it here too. 
use libmanagement;

-- Put your DDL 
drop table if exists BookLoans cascade;
drop table if exists Users cascade;
drop table if exists BookGenres cascade;
drop table if exists Books cascade;
drop table if exists Genres cascade;
drop table if exists BookLocations cascade;
drop table if exists Employees cascade;
drop table if exists EmployeeShifts cascade;

CREATE TABLE Users (
    user_id int primary key auto_increment,

    email varchar(100) not null,
    phone varchar(25),
    membership_start_date datetime not null default now(),

    address_street varchar(50) not null,
    address_street_2 varchar(50) default null,
    address_city varchar(25) not null,
    address_zipcode int
);

CREATE TABLE Genres (
    genre_id int primary key auto_increment,
    genre_name varchar(25) unique not null
);

CREATE TABLE Books (
    book_id int primary key auto_increment,
    title varchar(200) not null,
    description text,
    author text not null,
    physical_condition int,
    total_stock_count int not null default 0,
    rating int not null default 0
);

CREATE TABLE BookGenres (
    book_id int not null,
    genre_id int not null,
    foreign key (book_id) references Books(book_id) on delete cascade,
    foreign key (genre_id) references Genres(genre_id) on delete cascade
);

CREATE TABLE BookLoans (
    loan_id int primary key auto_increment,

    book_id int not null,
    user_id int not null,
    foreign key (book_id) references Books(book_id) on delete cascade,
    foreign key (user_id) references Users(user_id) on delete cascade,

    loan_start datetime not null default now(),
    loan_end datetime not null default (now() + interval 7 day),
    return_date datetime default null
);

CREATE TABLE BookLocations (
    book_id int not null,
    foreign key (book_id) references Books(book_id) on delete cascade,

    row_num int,
    shelf_num int
);

CREATE TABLE Employees (
    employee_id int primary key auto_increment,
    hire_date datetime not null default now(),
    direct_deposit_routing_num varchar(9),
    direct_deposit_account_num varchar(12),
    email varchar(100),
    phone varchar(25),
    age int
);

CREATE TABLE EmployeeShifts (
    employee_id int not null,
    foreign key (employee_id) references Employees(employee_id),

    clock_in_datetime datetime not null default now(),
    clock_out_datetime datetime default null
);

-- Add sample data. 
INSERT INTO Users (email, phone, address_street, address_city, address_zipcode) VALUES (
    'test@example.com', '+11234567890', '123 test street', 'test city', '10010'
);

INSERT INTO Employees (direct_deposit_routing_num, direct_deposit_account_num, email, phone, age) VALUES (
    '123456789', '123456789123', 'employee1@example.com', '+11234567891', 21
);

INSERT INTO EmployeeShifts (employee_id) VALUES (1);

INSERT INTO Books (title, description, author, physical_condition, total_stock_count) VALUES (
    'sample book 1', 'A book to give an example of how the library management system works', 'test author', 100, 15
);

INSERT INTO BookLocations (book_id, row_num, shelf_num) VALUES (1, 12, 456);

INSERT INTO BookLoans (book_id, user_id) VALUES (
    1, 1
);

INSERT INTO Genres (genre_name) VALUES ('Fiction');
INSERT INTO Genres (genre_name) VALUES ('Non-Fiction');
INSERT INTO Genres (genre_name) VALUES ('Sci-fi');

INSERT INTO BookGenres (book_id, genre_id) VALUES (1, 1);
INSERT INTO BookGenres (book_id, genre_id) VALUES (1, 2);