CREATE SCHEMA holerite_xpto;

CREATE TABLE funcionarios (
	matricula INT auto_increment NOT NULL,
    nome VARCHAR(255) NOT NULL,
    cpf CHAR(11) NOT NULL,
    admissao DATE NOT NULL,
    cargo VARCHAR(255) NOT NULL,
    comissao ENUM('sim','nao') NOT NULL,
    primary key (matricula)
);
ALTER TABLE funcionarios AUTO_INCREMENT = 100000;