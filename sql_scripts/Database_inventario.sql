create database if not EXISTS gestor_inventario;
use gestor_inventario;

drop table if exists INVENTARIO;
drop table if exists USUARIOS;

create table if not exists USUARIOS(
u_id int auto_increment primary key,
u_correo varchar(50) not null,
u_contraseña varchar(16) not null
);

create table if not exists INVENTARIO(
i_id int auto_increment primary key,
u_id int not null,
foreign key (u_id) references gestor_inventario.usuarios(u_id),
i_nombre varchar(50) not null,
i_marca varchar(25) not null,
i_cantidad int not null
);