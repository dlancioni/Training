--
-- General
--
drop table if exists status;
create table status 
(
	id int generated always as identity,
	key text,
	value text
);

--
-- Mask
--
drop table if exists mask;
create table mask
(
	id int generated always as identity,
	key text,
	value text
);

insert into mask (key, value) values ('RG', '99"."999"."999"."9'),
                                     ('CPF', '999"."999"."999"."99');
                                    
--
-- Trace
--
drop table if exists trace;
create table trace
(
	id int generated always as identity,
	action char(1),
	dt date,
	record jsonb
	constraint check_operation CHECK (action in ('I', 'U', 'D'))
);                                    



--
-- Access Control
--
drop table if exists users;
create table users
(
	id int generated always as identity,
	username text,
	password text,
	primary key(id)
);

drop table if exists login;
create table login 
(
	id int generated always as identity,
	user_id int,
	dt date,
    constraint fk_tb_user foreign key(user_id) references users(id)
);
