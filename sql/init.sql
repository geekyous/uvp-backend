create database uvp charset utf8mb4 collate utf8mb4_0900_bin;

create table api_credential
(
    access_key varchar(64) primary key,
    secret_key varchar(128),
    app_name   varchar(128),
    status     tinyint,
    expire_at  datetime,
    created_at datetime
) engine innodb;