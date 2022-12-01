create DATABASE project_unes;

use project_unes;

create table usuarios (
id int(10) not null auto_increment primary key,
email varchar(50) not null,
assunto varchar(100) not null,
descricao varchar(150) not null
);

select * from usuarios;


