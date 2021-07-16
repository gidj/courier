--
-- Name: courier; Type: DATABASE; Schema: -; Owner: courier
--

DO $$
BEGIN
  CREATE ROLE courier WITH NOLOGIN;
  EXCEPTION WHEN DUPLICATE_OBJECT THEN
  RAISE NOTICE 'not creating role courier -- it already exists';
END
$$;

ALTER ROLE courier WITH NOSUPERUSER INHERIT CREATEROLE CREATEDB LOGIN NOREPLICATION NOBYPASSRLS VALID UNTIL 'infinity';
ALTER DATABASE courier OWNER TO courier;

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

\connect courierdb
