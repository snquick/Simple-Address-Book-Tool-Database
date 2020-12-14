DROP DATABASE IF EXISTS simple_address_book;
CREATE DATABASE IF NOT EXISTS simple_address_book;
USE simple_address_book;

create table people_master (
	person_id	int			not null,
    person_first_name	varchar(14)	not null,
    person_last_name	varchar(16)	not null,
	person_dob	date		not null,
    active_phone_number	varchar(22)	not null,
    primary key(person_id)
);

create table addresses (
	address_id	int		not null,
    street_address	varchar(25)	not null,
    city 			varchar(25) not null,
    state			varchar(25) not null,
    zip_code 		char(5)		not null,
    primary key(address_id)
);

create table people_address (
	person_id	int		not null,
    address_id 	int		not null,
    start_date	date	not null,
    end_date	date	not null,
    foreign key (person_id) references people_master (person_id) ON DELETE CASCADE,
    foreign key (address_id) references addresses (address_id) ON DELETE CASCADE,
    primary key (person_id, address_id)
);
insert into people_master (person_id, person_first_name, person_last_name, person_dob, active_phone_number) values (1, 'test', 'random', '2000-00-00', 300000);
insert into addresses (address_id, street_address, city, state, zip_code) values (1, "random street 123", "randomness", "randooim", 10001);
insert into people_address (person_id, address_id, start_date, end_date) values (1, 1, '2000-00-00', '2002-02-02');




