--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.13 (Ubuntu 14.13-0ubuntu0.22.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;
SET SESSION AUTHORIZATION 'admin';
--
-- Name: language; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public.language AS ENUM (
    'en',
    'ru'
);


ALTER TYPE public.language OWNER TO admin;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: achievements; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.achievements (
    id integer NOT NULL,
    name character varying(50),
    points smallint,
    description text,
    description_rus character varying(1000),
    name_rus character varying(100),
    CONSTRAINT pointsnotnegative CHECK ((points > 0))
);


ALTER TABLE public.achievements OWNER TO admin;

--
-- Name: achievements_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.achievements_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.achievements_id_seq OWNER TO admin;

--
-- Name: achievements_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.achievements_id_seq OWNED BY public.achievements.id;


--
-- Name: user_achievement; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.user_achievement (
    "time" timestamp with time zone,
    user_id integer,
    achievement_id integer
);


ALTER TABLE public.user_achievement OWNER TO admin;

--
-- Name: users; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(50),
    language public.language
);


ALTER TABLE public.users OWNER TO admin;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO admin;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: achievements id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.achievements ALTER COLUMN id SET DEFAULT nextval('public.achievements_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: achievements; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.achievements (id, name, points, description, description_rus, name_rus) FROM stdin;
20	achievement2	35	 test achievement2	тестовое достижение2	достижение2
2	cleanliness	2	order on the desktop	порядок на рабочем столе	чистоплотность
1	achievement1	10	test achievement1	тестовое достижение1	достижение1
22	famous singer	45	very famous singer	очень знаменитый певец	знаменитый певец
23	song	7	wrote a song	написал песню	песня
24	concert	10	performed at a concert	выступил на концерте	концерт
\.


--
-- Data for Name: user_achievement; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.user_achievement ("time", user_id, achievement_id) FROM stdin;
2024-10-30 15:56:38.219276+03	2	1
2024-11-01 16:07:30.043908+03	1	20
2024-10-31 13:44:08.516028+03	7	23
2024-10-30 14:02:54.26235+03	7	23
2024-10-29 14:03:13.284637+03	7	23
2024-10-28 14:03:18.522224+03	7	23
2024-10-27 14:03:23.780596+03	7	23
2024-10-26 14:03:29.213356+03	7	23
2024-10-25 14:03:34.54612+03	7	23
2024-10-24 14:03:38.499588+03	7	23
2024-10-23 14:03:43.716059+03	7	23
2024-10-23 14:10:43.664942+03	8	23
2024-10-22 14:10:48.714224+03	8	23
2024-10-21 14:10:54.02255+03	8	23
2024-10-20 14:11:00.463794+03	8	23
2024-10-19 14:11:05.90976+03	8	23
2024-10-18 14:11:41.122462+03	8	24
2024-10-17 14:11:47.635179+03	8	24
2024-10-16 14:11:52.818251+03	8	24
2024-10-16 14:11:59.315297+03	8	23
2024-10-15 14:12:04.381443+03	8	23
2024-10-14 14:12:17.414155+03	8	24
2024-10-14 14:13:30.244069+03	7	24
2024-10-13 14:13:38.388452+03	7	24
2024-09-04 16:05:35.347279+03	3	23
2024-09-05 16:05:42.234006+03	3	23
2024-09-23 16:05:52.132771+03	3	23
2024-09-24 16:05:58.231936+03	3	23
2024-09-25 16:06:02.502736+03	3	23
2024-09-26 16:06:14.299179+03	3	23
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.users (id, name, language) FROM stdin;
1	Man Mansly	en
2	Chelovek Chelovekovitch	ru
3	Hugh Laurie	en
4	Борис Гребенщиков	ru
5	Агата Кристи	ru
6	David Bowie	en
7	Nick Cave	en
8	Леонид Федоров	ru
\.


--
-- Name: achievements_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.achievements_id_seq', 24, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.users_id_seq', 8, true);


--
-- Name: achievements achievements_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.achievements
    ADD CONSTRAINT achievements_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: user_achievement user_achievement_achievement_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.user_achievement
    ADD CONSTRAINT user_achievement_achievement_id_fkey FOREIGN KEY (achievement_id) REFERENCES public.achievements(id);


--
-- Name: user_achievement user_achievement_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.user_achievement
    ADD CONSTRAINT user_achievement_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

