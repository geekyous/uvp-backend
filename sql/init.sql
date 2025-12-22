create database uvp charset utf8mb4 collate utf8mb4_0900_bin;

create table app_auth
(
    ak         varchar(64) primary key,
    sk         varchar(128),
    app_name   varchar(128),
    status     tinyint,
    created_at datetime
) engine innodb;