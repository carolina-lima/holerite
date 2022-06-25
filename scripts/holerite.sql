CREATE SCHEMA holerite_xpto;

CREATE TABLE cargos (
	codigo INT NOT NULL,
    descricao VARCHAR(255) NOT NULL,
    salario_base FLOAT NOT NULL,
    comissao FLOAT NOT NULL,
    PRIMARY KEY (codigo)
);

INSERT INTO cargos (codigo, descricao, salario_base, comissao) VALUES (10, 'Cientista de Dados', 10200.00, 0.1);
INSERT INTO cargos (codigo, descricao, salario_base, comissao) VALUES (20,'Especialista em Business Intelligence',7000.00,0.08);
INSERT INTO cargos (codigo, descricao, salario_base, comissao) VALUES (30,'Desenvolvedor Mobile Sênior',6700.00,0.07);
INSERT INTO cargos (codigo, descricao, salario_base, comissao) VALUES (31,'Desenvolvedor Mobile Pleno',3550.00,0.06);
INSERT INTO cargos (codigo, descricao, salario_base, comissao) VALUES (32,'Desenvolvedor Junior',3000.00,0.03);
INSERT INTO cargos (codigo, descricao, salario_base, comissao) VALUES (50,'Gerente de Projetos',8900.00,0.08);

CREATE TABLE funcionarios (
	matricula INT auto_increment NOT NULL,
    nome VARCHAR(255) NOT NULL,
    cpf CHAR(11) NOT NULL,
    admissao DATE NOT NULL,
    cargo VARCHAR(255) NOT NULL,
    comissao VARCHAR(255) NOT NULL,
    primary key (matricula)
);

ALTER TABLE funcionarios AUTO_INCREMENT = 100000;