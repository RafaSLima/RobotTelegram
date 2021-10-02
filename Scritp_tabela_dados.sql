-- Criando tabela onde ficarão as mensagens a serem enviadas

CREATE TABLE SEND_TELEGRAM(
	 ID			INT IDENTITY(1,1)
	,DATE_SEND	DATE NULL
	,DATE_PROC	DATE NULL
	,MESSAGE	VARCHAR(500) NULL
	,SRC_FILE	VARCHAR(100) NULL
	,SRC_IMG	VARCHAR(100) NULL
	,CONTACT	VARCHAR(50)
	,VALIDATION	INT

)
-- Inserindo mensagens para teste

INSERT INTO SEND_TELEGRAM VALUES(NULL,CONVERT(DATE,GETDATE()),'Bom dia!',NULL,NULL,'Teste Bot',0)

INSERT INTO SEND_TELEGRAM VALUES(NULL,CONVERT(DATE,GETDATE()),'Enviando arquivo de teste','C:\RobotTelegram\teste.txt',NULL,'Teste Bot',0)

INSERT INTO SEND_TELEGRAM VALUES(NULL,CONVERT(DATE,GETDATE()),'Enviando imagem de teste',NULL,'C:\RobotTelegram\teste.jpg','Teste Bot',0)

-- Realizando testes
UPDATE SEND_TELEGRAM
SET VALIDATION = 0