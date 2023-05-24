-- Table: public.SD1

-- DROP TABLE IF EXISTS public."SD1";

CREATE TABLE IF NOT EXISTS public."SD1"
(
    "ID" integer NOT NULL,
    "Uchr" text COLLATE pg_catalog."default" NOT NULL,
    "PerNapr1" text COLLATE pg_catalog."default" NOT NULL,
    "Kol1" integer NOT NULL,
    "PerNapr2" text COLLATE pg_catalog."default" NOT NULL,
    "Kol2" integer NOT NULL,
    "PerNapr3" text COLLATE pg_catalog."default" NOT NULL,
    "Kol3" integer NOT NULL,
    "PerNapr4" text COLLATE pg_catalog."default" NOT NULL,
    "Kol4" integer NOT NULL,
    "PerNapr5" text COLLATE pg_catalog."default" NOT NULL,
    "Kol5" integer NOT NULL,
    "PerNapr6" text COLLATE pg_catalog."default" NOT NULL,
    "Kol6" integer NOT NULL,
    "Year" integer NOT NULL,
    CONSTRAINT "StudyDirections_pkey1" PRIMARY KEY ("ID")
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."SD1"
    OWNER to postgres;

COMMENT ON TABLE public."SD1"
    IS 'Направления обучения';

INSERT INTO "SD" VALUES (1,'ГБУДО г. Москвы ДМШ им. К.Н.Игумнова','Фортепиано',88,'Фортепиано',13,'Фортепиано',2,'Фортепиано',48,'духовые и ударные инструменты',2,'Фортепиано',37,0)
INSERT INTO "SD" VALUES (2,'ГБУДО г. Москвы ДМШ им. К.Н.Игумнова','струнные инструменты',45,'струнные инструменты',4,'',0,'струнные инструменты',18,'народные инструменты',2,'струнные инструменты',8,0)
INSERT INTO "SD" VALUES (3,'ГБУДО г. Москвы ДМШ им. К.Н.Игумнова','духовые и ударные инструменты',40,'духовые и ударные инструменты',6,'',0,'духовые и ударные инструменты',22,'хоровое пение',6,'духовые и ударные инструменты',22,0)
INSERT INTO "SD" VALUES (4,'ГБУДО г. Москвы ДМШ им. К.Н.Игумнова','народные инструменты',34,'народные инструменты',6,'',0,'народные инструменты',39,'сольное академическое пение',1,'народные инструменты',7,0)

SELECT * FROM "SD"