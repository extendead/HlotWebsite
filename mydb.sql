drop database script_data;
create database script_data;
use script_data;

select * from users;
select * from admin_data where login = "Test";

insert into admin_data(login, pass_word) values ('A', '1');
update admin_data set login = "Test", pass_word = "scrypt:32768:8:1$wCOfQcx8595OfXar$6da2c441b889c984af66da15bce2549515b5c9807b09e65921c0ba018c02d19f6193b8a1957d64d5d352d5d185b3bd285249beb6e45809dfaf65eb39212086a2" where id = 1;

create table if not exists users (
	id int unsigned primary key auto_increment,
	user_name varchar(25),
    phone varchar(18),
	email varchar(50) default "None",
    fb_text varchar(1500) default "None",
    social_media varchar(15) default "None"
);

create table if not exists admin_data (
	id int unsigned primary key auto_increment,
    login varchar(20) not null,
    pass_word varchar(40) not null
);

drop table users;
