--% index/fmus
--
-- PostgreSQL database dump
--

-- Dumped from database version 14.1 (Debian 14.1-1.pgdg110+1)
-- Dumped by pg_dump version 14.1 (Debian 14.1-1.pgdg110+1)

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

--
-- Name: tempdb; Type: DATABASE; Schema: -; Owner: usef
--

CREATE DATABASE tempdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.utf8';


ALTER DATABASE tempdb OWNER TO usef;

\connect tempdb

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO usef;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO usef;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO usef;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO usef;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO usef;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO usef;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.auth_user (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(255) NOT NULL,
    email character varying(254) NOT NULL,
    phone character varying(255) NOT NULL,
    is_active boolean NOT NULL,
    is_staff boolean NOT NULL,
    roles character varying(50) NOT NULL,
    first_name character varying(255),
    last_name character varying(255),
    name character varying(255)
);


ALTER TABLE public.auth_user OWNER TO usef;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id bigint NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO usef;

--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id bigint NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO usef;

--
-- Name: authtoken_token; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.authtoken_token OWNER TO usef;

--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO usef;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO usef;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO usef;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO usef;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO usef;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO usef;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO usef;

--
-- Name: ml_bayesiannetwork; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.ml_bayesiannetwork (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    sm_type smallint,
    has_results boolean NOT NULL,
    metadata text,
    engine_object text,
    engine_object_timestamp timestamp with time zone,
    engine_meta_iterations smallint NOT NULL,
    engine_iterations smallint,
    results_storage character varying(100),
    counter integer,
    counter_threshold integer,
    threshold_actions character varying(200),
    network_type smallint,
    image character varying(100)
);


ALTER TABLE public.ml_bayesiannetwork OWNER TO usef;

--
-- Name: ml_bayesiannetwork_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.ml_bayesiannetwork_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ml_bayesiannetwork_id_seq OWNER TO usef;

--
-- Name: ml_bayesiannetwork_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.ml_bayesiannetwork_id_seq OWNED BY public.ml_bayesiannetwork.id;


--
-- Name: ml_bayesiannetworkedge; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.ml_bayesiannetworkedge (
    id bigint NOT NULL,
    description character varying(50) NOT NULL,
    child_id bigint NOT NULL,
    network_id bigint NOT NULL,
    parent_id bigint NOT NULL
);


ALTER TABLE public.ml_bayesiannetworkedge OWNER TO usef;

--
-- Name: ml_bayesiannetworkedge_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.ml_bayesiannetworkedge_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ml_bayesiannetworkedge_id_seq OWNER TO usef;

--
-- Name: ml_bayesiannetworkedge_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.ml_bayesiannetworkedge_id_seq OWNED BY public.ml_bayesiannetworkedge.id;


--
-- Name: ml_bayesiannetworknode; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.ml_bayesiannetworknode (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    node_type smallint NOT NULL,
    is_observable boolean NOT NULL,
    distribution character varying(50),
    distribution_params character varying(200),
    deterministic character varying(50),
    deterministic_params character varying(200),
    engine_object text,
    engine_object_timestamp timestamp with time zone,
    engine_inferred_object text,
    engine_inferred_object_timestamp timestamp with time zone,
    graph_interval character varying(20),
    image character varying(100),
    network_id bigint NOT NULL
);


ALTER TABLE public.ml_bayesiannetworknode OWNER TO usef;

--
-- Name: ml_bayesiannetworknode_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.ml_bayesiannetworknode_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ml_bayesiannetworknode_id_seq OWNER TO usef;

--
-- Name: ml_bayesiannetworknode_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.ml_bayesiannetworknode_id_seq OWNED BY public.ml_bayesiannetworknode.id;


--
-- Name: ml_bayesiannetworknodecolumn; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.ml_bayesiannetworknodecolumn (
    id bigint NOT NULL,
    ref_column character varying(100) NOT NULL,
    "position" smallint,
    node_id bigint NOT NULL,
    ref_model_id integer NOT NULL
);


ALTER TABLE public.ml_bayesiannetworknodecolumn OWNER TO usef;

--
-- Name: ml_bayesiannetworknodecolumn_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.ml_bayesiannetworknodecolumn_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ml_bayesiannetworknodecolumn_id_seq OWNER TO usef;

--
-- Name: ml_bayesiannetworknodecolumn_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.ml_bayesiannetworknodecolumn_id_seq OWNED BY public.ml_bayesiannetworknodecolumn.id;


--
-- Name: ml_commentofmysite; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.ml_commentofmysite (
    id bigint NOT NULL,
    is_spam boolean,
    is_misclassified boolean NOT NULL,
    is_revised boolean NOT NULL,
    comment text NOT NULL,
    user_id smallint NOT NULL
);


ALTER TABLE public.ml_commentofmysite OWNER TO usef;

--
-- Name: ml_commentofmysite_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.ml_commentofmysite_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ml_commentofmysite_id_seq OWNER TO usef;

--
-- Name: ml_commentofmysite_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.ml_commentofmysite_id_seq OWNED BY public.ml_commentofmysite.id;


--
-- Name: ml_spamfilter; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.ml_spamfilter (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    sm_type smallint,
    has_results boolean NOT NULL,
    metadata text,
    engine_object text,
    engine_object_timestamp timestamp with time zone,
    engine_meta_iterations smallint NOT NULL,
    engine_iterations smallint,
    results_storage character varying(100),
    counter integer,
    counter_threshold integer,
    threshold_actions character varying(200),
    is_inferred boolean NOT NULL,
    sl_type smallint,
    labels_column character varying(100),
    pretraining character varying(100),
    cv_is_enabled boolean NOT NULL,
    cv_folds smallint,
    engine_object_vectorizer text,
    engine_object_data text,
    classifier character varying(100),
    spam_model_is_enabled boolean NOT NULL,
    spam_model_model character varying(100),
    cv_metric character varying(20),
    bow_is_enabled boolean NOT NULL,
    bow_enconding character varying(20) NOT NULL,
    bow_decode_error character varying(20) NOT NULL,
    bow_strip_accents character varying(20),
    bow_analyzer character varying(20) NOT NULL,
    bow_ngram_range_min smallint NOT NULL,
    bow_ngram_range_max smallint NOT NULL,
    bow_stop_words text,
    bow_max_df double precision NOT NULL,
    bow_min_df double precision NOT NULL,
    bow_max_features integer,
    bow_vocabulary text,
    bow_binary boolean NOT NULL,
    bow_use_tf_idf boolean NOT NULL
);


ALTER TABLE public.ml_spamfilter OWNER TO usef;

--
-- Name: ml_spamfilter_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.ml_spamfilter_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ml_spamfilter_id_seq OWNER TO usef;

--
-- Name: ml_spamfilter_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.ml_spamfilter_id_seq OWNED BY public.ml_spamfilter.id;


--
-- Name: ml_userinfo; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.ml_userinfo (
    id bigint NOT NULL,
    age integer NOT NULL,
    sex smallint,
    avg1 double precision,
    avg_time_pages double precision,
    visits_pages integer NOT NULL,
    avg_time_pages_a double precision,
    visits_pages_a integer NOT NULL,
    avg_time_pages_b double precision,
    visits_pages_b integer NOT NULL,
    avg_time_pages_c double precision,
    visits_pages_c integer NOT NULL,
    avg_time_pages_d double precision,
    visits_pages_d integer NOT NULL,
    avg_time_pages_e double precision,
    visits_pages_e integer NOT NULL,
    avg_time_pages_f double precision,
    visits_pages_f integer NOT NULL,
    avg_time_pages_g double precision,
    visits_pages_g integer NOT NULL,
    avg_time_pages_h double precision,
    visits_pages_h integer NOT NULL,
    avg_time_pages_i double precision,
    visits_pages_i integer NOT NULL,
    avg_time_pages_j double precision,
    visits_pages_j integer NOT NULL,
    cluster_1 character varying(1)
);


ALTER TABLE public.ml_userinfo OWNER TO usef;

--
-- Name: ml_userinfo_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.ml_userinfo_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ml_userinfo_id_seq OWNER TO usef;

--
-- Name: ml_userinfo_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.ml_userinfo_id_seq OWNED BY public.ml_userinfo.id;


--
-- Name: newss; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.newss (
    id integer NOT NULL,
    title character varying(1000) NOT NULL,
    link character varying(500) NOT NULL,
    summary character varying(5000) NOT NULL,
    content text NOT NULL,
    tags character varying(500) NOT NULL,
    images character varying(5000) NOT NULL
);


ALTER TABLE public.newss OWNER TO usef;

--
-- Name: newss_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.newss_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.newss_id_seq OWNER TO usef;

--
-- Name: newss_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.newss_id_seq OWNED BY public.newss.id;


--
-- Name: orderitems; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.orderitems (
    name character varying(200),
    qty integer,
    price numeric(7,2),
    image character varying(200),
    _id integer NOT NULL,
    order_id integer,
    product_id integer
);


ALTER TABLE public.orderitems OWNER TO usef;

--
-- Name: orderitems__id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.orderitems__id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orderitems__id_seq OWNER TO usef;

--
-- Name: orderitems__id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.orderitems__id_seq OWNED BY public.orderitems._id;


--
-- Name: orders; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.orders (
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone,
    "paymentMethod" character varying(200),
    "taxPrice" numeric(7,2),
    "shippingPrice" numeric(7,2),
    "totalPrice" numeric(7,2),
    "isPaid" boolean NOT NULL,
    "paidAt" timestamp with time zone,
    "isDelivered" boolean NOT NULL,
    "deliveredAt" timestamp with time zone,
    _id integer NOT NULL,
    user_id bigint
);


ALTER TABLE public.orders OWNER TO usef;

--
-- Name: orders__id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.orders__id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.orders__id_seq OWNER TO usef;

--
-- Name: orders__id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.orders__id_seq OWNED BY public.orders._id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.products (
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone,
    _id integer NOT NULL,
    brand character varying(200),
    category character varying(200),
    "countInStock" integer,
    description text,
    image character varying(100),
    name character varying(200),
    "numReviews" integer,
    price numeric(7,2),
    rating numeric(7,2),
    user_id bigint
);


ALTER TABLE public.products OWNER TO usef;

--
-- Name: products__id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.products__id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products__id_seq OWNER TO usef;

--
-- Name: products__id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.products__id_seq OWNED BY public.products._id;


--
-- Name: profile_profile; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.profile_profile (
    id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    bio text NOT NULL,
    image character varying(200) NOT NULL,
    user_id bigint NOT NULL
);


ALTER TABLE public.profile_profile OWNER TO usef;

--
-- Name: profile_profile_follows; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.profile_profile_follows (
    id integer NOT NULL,
    from_profile_id bigint NOT NULL,
    to_profile_id bigint NOT NULL
);


ALTER TABLE public.profile_profile_follows OWNER TO usef;

--
-- Name: profile_profile_follows_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.profile_profile_follows_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.profile_profile_follows_id_seq OWNER TO usef;

--
-- Name: profile_profile_follows_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.profile_profile_follows_id_seq OWNED BY public.profile_profile_follows.id;


--
-- Name: profile_profile_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.profile_profile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.profile_profile_id_seq OWNER TO usef;

--
-- Name: profile_profile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.profile_profile_id_seq OWNED BY public.profile_profile.id;


--
-- Name: reviews; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.reviews (
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone,
    name character varying(200),
    rating integer,
    comment text,
    _id integer NOT NULL,
    product_id integer,
    user_id bigint
);


ALTER TABLE public.reviews OWNER TO usef;

--
-- Name: reviews__id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.reviews__id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reviews__id_seq OWNER TO usef;

--
-- Name: reviews__id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.reviews__id_seq OWNED BY public.reviews._id;


--
-- Name: shippingaddresss; Type: TABLE; Schema: public; Owner: usef
--

CREATE TABLE public.shippingaddresss (
    address character varying(200),
    city character varying(200),
    "postalCode" character varying(200),
    country character varying(200),
    "shippingPrice" numeric(7,2),
    _id integer NOT NULL,
    order_id integer
);


ALTER TABLE public.shippingaddresss OWNER TO usef;

--
-- Name: shippingaddresss__id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.shippingaddresss__id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.shippingaddresss__id_seq OWNER TO usef;

--
-- Name: shippingaddresss__id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.shippingaddresss__id_seq OWNED BY public.shippingaddresss._id;


--
-- Name: users_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.users_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_groups_id_seq OWNER TO usef;

--
-- Name: users_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.users_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO usef;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.auth_user.id;


--
-- Name: users_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: usef
--

CREATE SEQUENCE public.users_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_permissions_id_seq OWNER TO usef;

--
-- Name: users_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: usef
--

ALTER SEQUENCE public.users_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.users_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.users_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: ml_bayesiannetwork id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetwork ALTER COLUMN id SET DEFAULT nextval('public.ml_bayesiannetwork_id_seq'::regclass);


--
-- Name: ml_bayesiannetworkedge id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworkedge ALTER COLUMN id SET DEFAULT nextval('public.ml_bayesiannetworkedge_id_seq'::regclass);


--
-- Name: ml_bayesiannetworknode id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworknode ALTER COLUMN id SET DEFAULT nextval('public.ml_bayesiannetworknode_id_seq'::regclass);


--
-- Name: ml_bayesiannetworknodecolumn id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworknodecolumn ALTER COLUMN id SET DEFAULT nextval('public.ml_bayesiannetworknodecolumn_id_seq'::regclass);


--
-- Name: ml_commentofmysite id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_commentofmysite ALTER COLUMN id SET DEFAULT nextval('public.ml_commentofmysite_id_seq'::regclass);


--
-- Name: ml_spamfilter id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_spamfilter ALTER COLUMN id SET DEFAULT nextval('public.ml_spamfilter_id_seq'::regclass);


--
-- Name: ml_userinfo id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_userinfo ALTER COLUMN id SET DEFAULT nextval('public.ml_userinfo_id_seq'::regclass);


--
-- Name: newss id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.newss ALTER COLUMN id SET DEFAULT nextval('public.newss_id_seq'::regclass);


--
-- Name: orderitems _id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.orderitems ALTER COLUMN _id SET DEFAULT nextval('public.orderitems__id_seq'::regclass);


--
-- Name: orders _id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.orders ALTER COLUMN _id SET DEFAULT nextval('public.orders__id_seq'::regclass);


--
-- Name: products _id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.products ALTER COLUMN _id SET DEFAULT nextval('public.products__id_seq'::regclass);


--
-- Name: profile_profile id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.profile_profile ALTER COLUMN id SET DEFAULT nextval('public.profile_profile_id_seq'::regclass);


--
-- Name: profile_profile_follows id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.profile_profile_follows ALTER COLUMN id SET DEFAULT nextval('public.profile_profile_follows_id_seq'::regclass);


--
-- Name: reviews _id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.reviews ALTER COLUMN _id SET DEFAULT nextval('public.reviews__id_seq'::regclass);


--
-- Name: shippingaddresss _id; Type: DEFAULT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.shippingaddresss ALTER COLUMN _id SET DEFAULT nextval('public.shippingaddresss__id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add news	1	add_news
2	Can change news	1	change_news
3	Can delete news	1	delete_news
4	Can view news	1	view_news
5	Can add profile	2	add_profile
6	Can change profile	2	change_profile
7	Can delete profile	2	delete_profile
8	Can view profile	2	view_profile
9	Can add user	3	add_user
10	Can change user	3	change_user
11	Can delete user	3	delete_user
12	Can view user	3	view_user
13	Can add log entry	4	add_logentry
14	Can change log entry	4	change_logentry
15	Can delete log entry	4	delete_logentry
16	Can view log entry	4	view_logentry
17	Can add permission	5	add_permission
18	Can change permission	5	change_permission
19	Can delete permission	5	delete_permission
20	Can view permission	5	view_permission
21	Can add group	6	add_group
22	Can change group	6	change_group
23	Can delete group	6	delete_group
24	Can view group	6	view_group
25	Can add content type	7	add_contenttype
26	Can change content type	7	change_contenttype
27	Can delete content type	7	delete_contenttype
28	Can view content type	7	view_contenttype
29	Can add session	8	add_session
30	Can change session	8	change_session
31	Can delete session	8	delete_session
32	Can view session	8	view_session
33	Can add Token	9	add_token
34	Can change Token	9	change_token
35	Can delete Token	9	delete_token
36	Can view Token	9	view_token
37	Can add token	10	add_tokenproxy
38	Can change token	10	change_tokenproxy
39	Can delete token	10	delete_tokenproxy
40	Can view token	10	view_tokenproxy
41	Can add shipping address	11	add_shippingaddress
42	Can change shipping address	11	change_shippingaddress
43	Can delete shipping address	11	delete_shippingaddress
44	Can view shipping address	11	view_shippingaddress
45	Can add order item	12	add_orderitem
46	Can change order item	12	change_orderitem
47	Can delete order item	12	delete_orderitem
48	Can view order item	12	view_orderitem
49	Can add order	13	add_order
50	Can change order	13	change_order
51	Can delete order	13	delete_order
52	Can view order	13	view_order
53	Can add product	14	add_product
54	Can change product	14	change_product
55	Can delete product	14	delete_product
56	Can view product	14	view_product
57	Can add review	15	add_review
58	Can change review	15	change_review
59	Can delete review	15	delete_review
60	Can view review	15	view_review
61	Can add Bayesian Network	16	add_bayesiannetwork
62	Can change Bayesian Network	16	change_bayesiannetwork
63	Can delete Bayesian Network	16	delete_bayesiannetwork
64	Can view Bayesian Network	16	view_bayesiannetwork
65	Can add Comment of my Site	17	add_commentofmysite
66	Can change Comment of my Site	17	change_commentofmysite
67	Can delete Comment of my Site	17	delete_commentofmysite
68	Can view Comment of my Site	17	view_commentofmysite
69	Can add Spam Filter	18	add_spamfilter
70	Can change Spam Filter	18	change_spamfilter
71	Can delete Spam Filter	18	delete_spamfilter
72	Can view Spam Filter	18	view_spamfilter
73	Can add User Info	19	add_userinfo
74	Can change User Info	19	change_userinfo
75	Can delete User Info	19	delete_userinfo
76	Can view User Info	19	view_userinfo
77	Can add Bayesian Networks Node Column	20	add_bayesiannetworknodecolumn
78	Can change Bayesian Networks Node Column	20	change_bayesiannetworknodecolumn
79	Can delete Bayesian Networks Node Column	20	delete_bayesiannetworknodecolumn
80	Can view Bayesian Networks Node Column	20	view_bayesiannetworknodecolumn
81	Can add bayesian network edge	21	add_bayesiannetworkedge
82	Can change bayesian network edge	21	change_bayesiannetworkedge
83	Can delete bayesian network edge	21	delete_bayesiannetworkedge
84	Can view bayesian network edge	21	view_bayesiannetworkedge
85	Can add bayesian network node	22	add_bayesiannetworknode
86	Can change bayesian network node	22	change_bayesiannetworknode
87	Can delete bayesian network node	22	delete_bayesiannetworknode
88	Can view bayesian network node	22	view_bayesiannetworknode
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.auth_user (id, created_at, updated_at, password, last_login, is_superuser, username, email, phone, is_active, is_staff, roles, first_name, last_name, name) FROM stdin;
1	2022-01-21 12:19:58.151787+00	2022-01-21 12:19:58.15181+00	pbkdf2_sha256$260000$0ftJSxJfYIa0Qot7qbf9D8$+IIzKHyeDkBhkzcfD+gFqq1XbBDvVAUUO3JrIWddW/o=	\N	f	wieke	wieke@gmail.com		t	f	user	\N	\N	\N
3	2022-01-21 17:19:05.344821+00	2022-01-21 17:19:05.359542+00	pbkdf2_sha256$260000$SnB0TbyiXFDCdMx4WxBRfk$Fkf/pqdMUs7bqnoNmBwlyFPL5jveV/LfCs/6hobyvHk=	2022-01-22 12:21:36.803442+00	t	usef	usef@gmail.com		t	t	user	\N	\N	\N
4	2022-01-23 15:45:17.171296+00	2022-01-23 15:45:17.171323+00	pbkdf2_sha256$260000$mr31mKExiVPpZDnRpglII3$IaF9SvVnsvIt0JDcuM3Q6BZSy3Jd4VYpBnnkHr0zADM=	\N	t	sample-email@gmail.com	sample-email@gmail.com		t	t	user	wieke	\N	\N
5	2022-01-30 21:58:39.992274+00	2022-01-30 21:58:39.992293+00	pbkdf2_sha256$260000$KZSu8tyF3G8xeO6OQP1Ncb$Acq2iJD1wmXEXO66yyLyx9W65SpIQsD85g4vkYzPntA=	\N	f	gaia2@gmail.com	gaia2@gmail.com		t	f	user	gaia2	\N	gaia2
6	2022-01-30 22:02:36.59906+00	2022-01-30 22:02:36.599087+00	pbkdf2_sha256$260000$m7bvj6m4zjNXhWsqk4GqUb$74F/i7mVLLmU/dtQJfUzUwMzoDCdO/KKxSWA5HOJuz0=	\N	f	gaia@gmail.com	gaia@gmail.com		t	f	user	gaia	\N	gaia
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: authtoken_token; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.authtoken_token (key, created, user_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	news	news
2	profile	profile
3	user	user
4	admin	logentry
5	auth	permission
6	auth	group
7	contenttypes	contenttype
8	sessions	session
9	authtoken	token
10	authtoken	tokenproxy
11	shippingaddress	shippingaddress
12	orderitem	orderitem
13	order	order
14	product	product
15	review	review
16	ml	bayesiannetwork
17	ml	commentofmysite
18	ml	spamfilter
19	ml	userinfo
20	ml	bayesiannetworknodecolumn
21	ml	bayesiannetworkedge
22	ml	bayesiannetworknode
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-01-21 11:44:08.872987+00
2	contenttypes	0002_remove_content_type_name	2022-01-21 11:44:08.887065+00
3	auth	0001_initial	2022-01-21 11:44:08.951439+00
4	auth	0002_alter_permission_name_max_length	2022-01-21 11:44:08.959135+00
5	auth	0003_alter_user_email_max_length	2022-01-21 11:44:08.966935+00
6	auth	0004_alter_user_username_opts	2022-01-21 11:44:08.975554+00
7	auth	0005_alter_user_last_login_null	2022-01-21 11:44:08.984313+00
8	auth	0006_require_contenttypes_0002	2022-01-21 11:44:08.988706+00
9	auth	0007_alter_validators_add_error_messages	2022-01-21 11:44:08.997597+00
10	auth	0008_alter_user_username_max_length	2022-01-21 11:44:09.005259+00
11	auth	0009_alter_user_last_name_max_length	2022-01-21 11:44:09.013849+00
12	auth	0010_alter_group_name_max_length	2022-01-21 11:44:09.026132+00
13	auth	0011_update_proxy_permissions	2022-01-21 11:44:09.035336+00
14	auth	0012_alter_user_first_name_max_length	2022-01-21 11:44:09.044707+00
15	user	0001_initial	2022-01-21 11:44:09.113863+00
16	admin	0001_initial	2022-01-21 11:44:09.145491+00
17	admin	0002_logentry_remove_auto_add	2022-01-21 11:44:09.154301+00
18	admin	0003_logentry_add_action_flag_choices	2022-01-21 11:44:09.165356+00
19	authtoken	0001_initial	2022-01-21 11:44:09.188736+00
20	authtoken	0002_auto_20160226_1747	2022-01-21 11:44:09.224833+00
21	authtoken	0003_tokenproxy	2022-01-21 11:44:09.230228+00
22	profile	0001_initial	2022-01-21 11:44:09.265255+00
23	profile	0002_profile_user	2022-01-21 11:44:09.283774+00
24	sessions	0001_initial	2022-01-21 11:44:09.307361+00
25	news	0001_initial	2022-01-21 11:44:23.018122+00
26	user	0002_auto_20220121_1716	2022-01-21 17:16:59.062177+00
27	user	0003_alter_user_phone	2022-01-21 17:18:54.791928+00
28	ml	0001_initial	2022-01-22 18:39:59.79322+00
29	ml	0002_bayesiannetworkedge_bayesiannetworknode_bayesiannetworknodecolumn	2022-01-22 20:01:35.889531+00
30	profile	0003_alter_profile_id	2022-01-22 20:01:35.978525+00
31	product	0001_initial	2022-01-22 20:04:30.69038+00
32	user	0004_auto_20220123_1536	2022-01-23 15:36:37.339557+00
33	order	0001_initial	2022-01-23 15:51:28.84504+00
34	orderitem	0001_initial	2022-01-23 15:51:28.886847+00
35	review	0001_initial	2022-01-23 15:51:28.939702+00
36	shippingaddress	0001_initial	2022-01-23 15:51:28.976496+00
37	user	0005_user_name	2022-01-23 20:07:08.064889+00
38	user	0006_alter_user_table	2022-01-28 21:10:41.421221+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
2hmjmaxijof17zbx8seqe47vzccc70ec	.eJxVjMsOwiAQRf-FtSHDG1y69xsIA4NUDU1KuzL-uzbpQrf3nHNfLKZtbXEbtMSpsDNT7PS7YcoP6jso99RvM89zX5cJ-a7wgw5-nQs9L4f7d9DSaN86o3DgpKVSKhjMTqrqTRIyhEASQGEAaX3WpQpfySrtwIIMBq0S2Wn2_gDT1zbk:1nAxZE:BmfbhIO8A1WTCxe19BvaZYm_QMzK1_4oR0eEXkPndNI	2022-02-04 17:19:16.889543+00
1yjhk5j67vrbl0cohvplg3u34o2m0qvu	.eJxVjMsOwiAQRf-FtSHDG1y69xsIA4NUDU1KuzL-uzbpQrf3nHNfLKZtbXEbtMSpsDNT7PS7YcoP6jso99RvM89zX5cJ-a7wgw5-nQs9L4f7d9DSaN86o3DgpKVSKhjMTqrqTRIyhEASQGEAaX3WpQpfySrtwIIMBq0S2Wn2_gDT1zbk:1nBFOi:-cNt6z7FXuNJOZ18QhhGGtNXKe--Lk2mAqNjKkB4C1w	2022-02-05 12:21:36.811004+00
\.


--
-- Data for Name: ml_bayesiannetwork; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.ml_bayesiannetwork (id, name, sm_type, has_results, metadata, engine_object, engine_object_timestamp, engine_meta_iterations, engine_iterations, results_storage, counter, counter_threshold, threshold_actions, network_type, image) FROM stdin;
\.


--
-- Data for Name: ml_bayesiannetworkedge; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.ml_bayesiannetworkedge (id, description, child_id, network_id, parent_id) FROM stdin;
\.


--
-- Data for Name: ml_bayesiannetworknode; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.ml_bayesiannetworknode (id, name, node_type, is_observable, distribution, distribution_params, deterministic, deterministic_params, engine_object, engine_object_timestamp, engine_inferred_object, engine_inferred_object_timestamp, graph_interval, image, network_id) FROM stdin;
\.


--
-- Data for Name: ml_bayesiannetworknodecolumn; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.ml_bayesiannetworknodecolumn (id, ref_column, "position", node_id, ref_model_id) FROM stdin;
\.


--
-- Data for Name: ml_commentofmysite; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.ml_commentofmysite (id, is_spam, is_misclassified, is_revised, comment, user_id) FROM stdin;
\.


--
-- Data for Name: ml_spamfilter; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.ml_spamfilter (id, name, sm_type, has_results, metadata, engine_object, engine_object_timestamp, engine_meta_iterations, engine_iterations, results_storage, counter, counter_threshold, threshold_actions, is_inferred, sl_type, labels_column, pretraining, cv_is_enabled, cv_folds, engine_object_vectorizer, engine_object_data, classifier, spam_model_is_enabled, spam_model_model, cv_metric, bow_is_enabled, bow_enconding, bow_decode_error, bow_strip_accents, bow_analyzer, bow_ngram_range_min, bow_ngram_range_max, bow_stop_words, bow_max_df, bow_min_df, bow_max_features, bow_vocabulary, bow_binary, bow_use_tf_idf) FROM stdin;
\.


--
-- Data for Name: ml_userinfo; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.ml_userinfo (id, age, sex, avg1, avg_time_pages, visits_pages, avg_time_pages_a, visits_pages_a, avg_time_pages_b, visits_pages_b, avg_time_pages_c, visits_pages_c, avg_time_pages_d, visits_pages_d, avg_time_pages_e, visits_pages_e, avg_time_pages_f, visits_pages_f, avg_time_pages_g, visits_pages_g, avg_time_pages_h, visits_pages_h, avg_time_pages_i, visits_pages_i, avg_time_pages_j, visits_pages_j, cluster_1) FROM stdin;
\.


--
-- Data for Name: newss; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.newss (id, title, link, summary, content, tags, images) FROM stdin;
\.


--
-- Data for Name: orderitems; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.orderitems (name, qty, price, image, _id, order_id, product_id) FROM stdin;
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	23	12	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	24	12	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	25	13	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	26	13	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	27	14	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	28	14	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	29	15	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	30	15	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	31	16	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	32	16	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	33	17	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	34	17	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	35	18	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	36	18	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	37	19	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	38	19	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	39	20	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	40	20	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	41	21	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	42	21	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	43	22	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	44	22	4
Airpods Wireless Bluetooth Headphones	7	89.99	/images/airpods.jpg	45	23	1
Sony Playstation 4 Pro White Version	2	399.99	/images/playstation.jpg	46	23	4
Airpods Wireless Bluetooth Headphones	5	89.99	/images/airpods.jpg	47	24	1
Cannon EOS 80D DSLR Camera	5	929.99	/images/camera_zpMaPRx.jpg	48	25	3
Airpods Wireless Bluetooth Headphones	2	89.99	/images/airpods.jpg	49	26	1
Sony Playstation 4 Pro White Version	1	399.99	/images/playstation.jpg	50	26	4
Airpods Wireless Bluetooth Headphones	3	89.99	/images/airpods.jpg	51	27	1
Sony Playstation 4 Pro White Version	1	399.99	/images/playstation.jpg	52	27	4
iPhone 11 Pro 256GB Memory	2	599.99	/images/phone.jpg	53	28	2
Amazon Echo Dot 3rd Generation	1	29.99	/images/alexa.jpg	54	28	6
Airpods Wireless Bluetooth Headphones	2	89.99	/images/airpods.jpg	55	29	1
iPhone 11 Pro 256GB Memory	3	599.99	/images/phone.jpg	56	29	2
\.


--
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.orders (created_at, updated_at, "paymentMethod", "taxPrice", "shippingPrice", "totalPrice", "isPaid", "paidAt", "isDelivered", "deliveredAt", _id, user_id) FROM stdin;
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	12	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	13	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	14	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	15	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	16	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	17	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	18	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	19	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	20	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	21	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	22	1
2021-01-22 00:14:20.45792+00	\N	PayPal	117.25	0.00	1547.16	f	\N	f	\N	23	1
2021-01-22 00:14:20.45792+00	\N	PayPal	36.90	0.00	486.85	f	\N	f	\N	24	1
2021-01-22 00:14:20.45792+00	\N	PayPal	381.30	0.00	5031.25	f	\N	f	\N	25	1
2021-01-22 00:14:20.45792+00	\N	PayPal	47.56	0.00	627.53	f	\N	f	\N	26	1
2021-01-22 00:14:20.45792+00	\N	PayPal	54.94	0.00	724.90	f	\N	f	\N	27	1
2021-01-22 00:14:20.45792+00	\N	PayPal	100.86	0.00	1330.83	t	2021-01-05 23:58:05+00	t	2021-01-20 17:29:33.639137+00	28	1
2021-01-22 00:14:20.45792+00	\N	PayPal	162.36	0.00	2142.31	t	2021-01-15 14:50:18.094695+00	t	2021-01-20 17:31:34.481452+00	29	1
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.products (created_at, updated_at, _id, brand, category, "countInStock", description, image, name, "numReviews", price, rating, user_id) FROM stdin;
2020-12-24 00:33:52.148105+00	\N	1	Apple	Electronics	5	Bluetooth technology lets you connect it with compatible devices wirelessly High-quality AAC audio offers immersive listening experience Built-in microphone allows you to take calls while working	airpods.jpg	Airpods Wireless Bluetooth Headphones	2	89.99	4.00	1
2020-12-24 04:08:14.324719+00	\N	2	Apple	Electronics	7	Introducing the iPhone 11 Pro. A transformative triple-camera system that adds tons of capability without complexity. An unprecedented leap in battery life	phone.jpg	iPhone 11 Pro 256GB Memory	1	599.99	4.00	1
2020-12-24 19:39:42.787527+00	\N	3	Cannon	Electronics	0	Characterized by versatile imaging specs, the Canon EOS 80D further clarifies itself using a pair of robust focusing systems and an intuitive design	camera_DeAtR52.jpg	Cannon EOS 80D DSLR Camera	12	929.99	3.00	1
2020-12-24 19:40:52.684846+00	\N	4	Sony	Electronics	178	The ultimate home entertainment center starts with PlayStation. Whether you are into gaming, HD movies, television, music	playstation.jpg	Sony Playstation 4 Pro White Version	1	399.99	4.00	1
2020-12-24 19:41:47.595938+00	\N	5	Logitech	Electronics	7	Get a better handle on your games with this Logitech LIGHTSYNC gaming mouse. The six programmable buttons allow customization for a smooth playing experience	mouse.jpg	Logitech G-Series Gaming Mouse	10	49.99	3.50	1
2020-12-24 19:42:31.546425+00	\N	6	Amazon	Electronics	1	Meet Echo Dot - Our most popular smart speaker with a fabric design. It is our most compact smart speaker that fits perfectly into small space	alexa.jpg	Amazon Echo Dot 3rd Generation	12	29.99	4.00	1
\.


--
-- Data for Name: profile_profile; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.profile_profile (id, created_at, updated_at, bio, image, user_id) FROM stdin;
1	2022-01-21 12:19:58.155429+00	2022-01-21 12:19:58.155447+00			1
2	2022-01-21 17:19:05.351911+00	2022-01-21 17:19:05.35193+00			3
3	2022-01-23 15:45:17.183349+00	2022-01-23 15:45:17.183369+00			4
4	2022-01-30 21:58:39.996532+00	2022-01-30 21:58:39.996548+00			5
5	2022-01-30 22:02:36.60178+00	2022-01-30 22:02:36.601825+00			6
\.


--
-- Data for Name: profile_profile_follows; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.profile_profile_follows (id, from_profile_id, to_profile_id) FROM stdin;
\.


--
-- Data for Name: reviews; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.reviews (created_at, updated_at, name, rating, comment, _id, product_id, user_id) FROM stdin;
2021-01-22 01:10:19.602219+00	\N	Dennis Ivanov	3	Good Product	1	1	1
2021-01-22 04:07:51.505526+00	\N	Jack	5	Loved it!\r\n	3	1	3
2022-01-21 13:37:33.453121+00	\N	wieke	4	aku senantiasa menggunakan ini	4	2	4
\.


--
-- Data for Name: shippingaddresss; Type: TABLE DATA; Schema: public; Owner: usef
--

COPY public.shippingaddresss (address, city, "postalCode", country, "shippingPrice", _id, order_id) FROM stdin;
1600 PA Ave	Washington	888888	USA	\N	12	12
1600 PA Ave	Washington	888888	USA	\N	13	13
1600 PA Ave	Washington	888888	USA	\N	14	14
1600 PA Ave	Washington	888888	USA	\N	15	15
1600 PA Ave	Washington	888888	USA	\N	16	16
1600 PA Ave	Washington	888888	USA	\N	17	17
1600 PA Ave	Washington	888888	USA	\N	18	18
1600 PA Ave	Washington	888888	USA	\N	19	19
1600 PA Ave	Washington	888888	USA	\N	20	20
1600 PA Ave	Washington	888888	USA	\N	21	21
1600 PA Ave	Washington	888888	USA	\N	22	22
1600 PA Ave	Washington	888888	USA	\N	23	23
1600 PA Ave	Washington	888888	USA	\N	24	24
1600 PA Ave	Washington	888888	USA	\N	25	25
1600 PA Ave	Washington	888888	USA	\N	26	26
1600 PA Ave	Washington	888888	USA	\N	27	27
1600 PA Ave	Washington	888888	USA	\N	28	28
1600 PA Ave	Washington	888888	USA	\N	29	29
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 88, true);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 22, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 38, true);


--
-- Name: ml_bayesiannetwork_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.ml_bayesiannetwork_id_seq', 1, false);


--
-- Name: ml_bayesiannetworkedge_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.ml_bayesiannetworkedge_id_seq', 1, false);


--
-- Name: ml_bayesiannetworknode_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.ml_bayesiannetworknode_id_seq', 1, false);


--
-- Name: ml_bayesiannetworknodecolumn_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.ml_bayesiannetworknodecolumn_id_seq', 1, false);


--
-- Name: ml_commentofmysite_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.ml_commentofmysite_id_seq', 1, false);


--
-- Name: ml_spamfilter_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.ml_spamfilter_id_seq', 1, false);


--
-- Name: ml_userinfo_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.ml_userinfo_id_seq', 1, false);


--
-- Name: newss_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.newss_id_seq', 1, false);


--
-- Name: orderitems__id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.orderitems__id_seq', 1, false);


--
-- Name: orders__id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.orders__id_seq', 1, false);


--
-- Name: products__id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.products__id_seq', 1, false);


--
-- Name: profile_profile_follows_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.profile_profile_follows_id_seq', 1, false);


--
-- Name: profile_profile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.profile_profile_id_seq', 5, true);


--
-- Name: reviews__id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.reviews__id_seq', 1, false);


--
-- Name: shippingaddresss__id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.shippingaddresss__id_seq', 1, false);


--
-- Name: users_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.users_groups_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.users_id_seq', 6, true);


--
-- Name: users_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: usef
--

SELECT pg_catalog.setval('public.users_user_permissions_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authtoken_token authtoken_token_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);


--
-- Name: authtoken_token authtoken_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: ml_bayesiannetwork ml_bayesiannetwork_name_key; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetwork
    ADD CONSTRAINT ml_bayesiannetwork_name_key UNIQUE (name);


--
-- Name: ml_bayesiannetwork ml_bayesiannetwork_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetwork
    ADD CONSTRAINT ml_bayesiannetwork_pkey PRIMARY KEY (id);


--
-- Name: ml_bayesiannetworkedge ml_bayesiannetworkedge_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworkedge
    ADD CONSTRAINT ml_bayesiannetworkedge_pkey PRIMARY KEY (id);


--
-- Name: ml_bayesiannetworknode ml_bayesiannetworknode_network_id_name_16df1479_uniq; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworknode
    ADD CONSTRAINT ml_bayesiannetworknode_network_id_name_16df1479_uniq UNIQUE (network_id, name);


--
-- Name: ml_bayesiannetworknode ml_bayesiannetworknode_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworknode
    ADD CONSTRAINT ml_bayesiannetworknode_pkey PRIMARY KEY (id);


--
-- Name: ml_bayesiannetworknodecolumn ml_bayesiannetworknodeco_node_id_ref_model_id_ref_fff63154_uniq; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworknodecolumn
    ADD CONSTRAINT ml_bayesiannetworknodeco_node_id_ref_model_id_ref_fff63154_uniq UNIQUE (node_id, ref_model_id, ref_column);


--
-- Name: ml_bayesiannetworknodecolumn ml_bayesiannetworknodecolumn_node_id_position_94f462a1_uniq; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworknodecolumn
    ADD CONSTRAINT ml_bayesiannetworknodecolumn_node_id_position_94f462a1_uniq UNIQUE (node_id, "position");


--
-- Name: ml_bayesiannetworknodecolumn ml_bayesiannetworknodecolumn_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworknodecolumn
    ADD CONSTRAINT ml_bayesiannetworknodecolumn_pkey PRIMARY KEY (id);


--
-- Name: ml_commentofmysite ml_commentofmysite_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_commentofmysite
    ADD CONSTRAINT ml_commentofmysite_pkey PRIMARY KEY (id);


--
-- Name: ml_spamfilter ml_spamfilter_name_key; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_spamfilter
    ADD CONSTRAINT ml_spamfilter_name_key UNIQUE (name);


--
-- Name: ml_spamfilter ml_spamfilter_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_spamfilter
    ADD CONSTRAINT ml_spamfilter_pkey PRIMARY KEY (id);


--
-- Name: ml_userinfo ml_userinfo_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_userinfo
    ADD CONSTRAINT ml_userinfo_pkey PRIMARY KEY (id);


--
-- Name: newss newss_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.newss
    ADD CONSTRAINT newss_pkey PRIMARY KEY (id);


--
-- Name: orderitems orderitems_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.orderitems
    ADD CONSTRAINT orderitems_pkey PRIMARY KEY (_id);


--
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (_id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (_id);


--
-- Name: profile_profile_follows profile_profile_follows_from_profile_id_to_profi_337a72ca_uniq; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.profile_profile_follows
    ADD CONSTRAINT profile_profile_follows_from_profile_id_to_profi_337a72ca_uniq UNIQUE (from_profile_id, to_profile_id);


--
-- Name: profile_profile_follows profile_profile_follows_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.profile_profile_follows
    ADD CONSTRAINT profile_profile_follows_pkey PRIMARY KEY (id);


--
-- Name: profile_profile profile_profile_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.profile_profile
    ADD CONSTRAINT profile_profile_pkey PRIMARY KEY (id);


--
-- Name: profile_profile profile_profile_user_id_key; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.profile_profile
    ADD CONSTRAINT profile_profile_user_id_key UNIQUE (user_id);


--
-- Name: reviews reviews_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_pkey PRIMARY KEY (_id);


--
-- Name: shippingaddresss shippingaddresss_order_id_key; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.shippingaddresss
    ADD CONSTRAINT shippingaddresss_order_id_key UNIQUE (order_id);


--
-- Name: shippingaddresss shippingaddresss_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.shippingaddresss
    ADD CONSTRAINT shippingaddresss_pkey PRIMARY KEY (_id);


--
-- Name: auth_user users_email_key; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: auth_user_groups users_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT users_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups users_groups_user_id_group_id_fc7788e8_uniq; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT users_groups_user_id_group_id_fc7788e8_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user users_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions users_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT users_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions users_user_permissions_user_id_permission_id_3b86cbdf_uniq; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT users_user_permissions_user_id_permission_id_3b86cbdf_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user users_username_key; Type: CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authtoken_token_key_10f0b77e_like; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: ml_bayesiannetwork_name_3dc70f22_like; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX ml_bayesiannetwork_name_3dc70f22_like ON public.ml_bayesiannetwork USING btree (name varchar_pattern_ops);


--
-- Name: ml_bayesiannetworkedge_child_id_5936733d; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX ml_bayesiannetworkedge_child_id_5936733d ON public.ml_bayesiannetworkedge USING btree (child_id);


--
-- Name: ml_bayesiannetworkedge_network_id_94dc1e36; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX ml_bayesiannetworkedge_network_id_94dc1e36 ON public.ml_bayesiannetworkedge USING btree (network_id);


--
-- Name: ml_bayesiannetworkedge_parent_id_f4b85b57; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX ml_bayesiannetworkedge_parent_id_f4b85b57 ON public.ml_bayesiannetworkedge USING btree (parent_id);


--
-- Name: ml_bayesiannetworknode_network_id_9a9d1585; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX ml_bayesiannetworknode_network_id_9a9d1585 ON public.ml_bayesiannetworknode USING btree (network_id);


--
-- Name: ml_bayesiannetworknodecolumn_node_id_44335d28; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX ml_bayesiannetworknodecolumn_node_id_44335d28 ON public.ml_bayesiannetworknodecolumn USING btree (node_id);


--
-- Name: ml_bayesiannetworknodecolumn_ref_model_id_cb5ca8a2; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX ml_bayesiannetworknodecolumn_ref_model_id_cb5ca8a2 ON public.ml_bayesiannetworknodecolumn USING btree (ref_model_id);


--
-- Name: ml_spamfilter_name_0d1ef0ee_like; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX ml_spamfilter_name_0d1ef0ee_like ON public.ml_spamfilter USING btree (name varchar_pattern_ops);


--
-- Name: orderitems_order_id_591c3139; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX orderitems_order_id_591c3139 ON public.orderitems USING btree (order_id);


--
-- Name: orderitems_product_id_0f0de012; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX orderitems_product_id_0f0de012 ON public.orderitems USING btree (product_id);


--
-- Name: orders_user_id_7e2523fb; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX orders_user_id_7e2523fb ON public.orders USING btree (user_id);


--
-- Name: products_user_id_0be7171c; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX products_user_id_0be7171c ON public.products USING btree (user_id);


--
-- Name: profile_profile_follows_from_profile_id_c2d14f74; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX profile_profile_follows_from_profile_id_c2d14f74 ON public.profile_profile_follows USING btree (from_profile_id);


--
-- Name: profile_profile_follows_to_profile_id_0089f180; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX profile_profile_follows_to_profile_id_0089f180 ON public.profile_profile_follows USING btree (to_profile_id);


--
-- Name: reviews_product_id_d4b78cfe; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX reviews_product_id_d4b78cfe ON public.reviews USING btree (product_id);


--
-- Name: reviews_user_id_c23b0903; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX reviews_user_id_c23b0903 ON public.reviews USING btree (user_id);


--
-- Name: users_email_0ea73cca_like; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX users_email_0ea73cca_like ON public.auth_user USING btree (email varchar_pattern_ops);


--
-- Name: users_groups_group_id_2f3517aa; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX users_groups_group_id_2f3517aa ON public.auth_user_groups USING btree (group_id);


--
-- Name: users_groups_user_id_f500bee5; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX users_groups_user_id_f500bee5 ON public.auth_user_groups USING btree (user_id);


--
-- Name: users_phone_2b77170a; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX users_phone_2b77170a ON public.auth_user USING btree (phone);


--
-- Name: users_phone_2b77170a_like; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX users_phone_2b77170a_like ON public.auth_user USING btree (phone varchar_pattern_ops);


--
-- Name: users_user_permissions_permission_id_6d08dcd2; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX users_user_permissions_permission_id_6d08dcd2 ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: users_user_permissions_user_id_92473840; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX users_user_permissions_user_id_92473840 ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: users_username_e8658fc8_like; Type: INDEX; Schema: public; Owner: usef
--

CREATE INDEX users_username_e8658fc8_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authtoken_token authtoken_token_user_id_35299eff_fk; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ml_bayesiannetworkedge ml_bayesiannetworked_child_id_5936733d_fk_ml_bayesi; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworkedge
    ADD CONSTRAINT ml_bayesiannetworked_child_id_5936733d_fk_ml_bayesi FOREIGN KEY (child_id) REFERENCES public.ml_bayesiannetworknode(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ml_bayesiannetworkedge ml_bayesiannetworked_network_id_94dc1e36_fk_ml_bayesi; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworkedge
    ADD CONSTRAINT ml_bayesiannetworked_network_id_94dc1e36_fk_ml_bayesi FOREIGN KEY (network_id) REFERENCES public.ml_bayesiannetwork(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ml_bayesiannetworkedge ml_bayesiannetworked_parent_id_f4b85b57_fk_ml_bayesi; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworkedge
    ADD CONSTRAINT ml_bayesiannetworked_parent_id_f4b85b57_fk_ml_bayesi FOREIGN KEY (parent_id) REFERENCES public.ml_bayesiannetworknode(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ml_bayesiannetworknode ml_bayesiannetworkno_network_id_9a9d1585_fk_ml_bayesi; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworknode
    ADD CONSTRAINT ml_bayesiannetworkno_network_id_9a9d1585_fk_ml_bayesi FOREIGN KEY (network_id) REFERENCES public.ml_bayesiannetwork(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ml_bayesiannetworknodecolumn ml_bayesiannetworkno_node_id_44335d28_fk_ml_bayesi; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworknodecolumn
    ADD CONSTRAINT ml_bayesiannetworkno_node_id_44335d28_fk_ml_bayesi FOREIGN KEY (node_id) REFERENCES public.ml_bayesiannetworknode(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ml_bayesiannetworknodecolumn ml_bayesiannetworkno_ref_model_id_cb5ca8a2_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.ml_bayesiannetworknodecolumn
    ADD CONSTRAINT ml_bayesiannetworkno_ref_model_id_cb5ca8a2_fk_django_co FOREIGN KEY (ref_model_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orderitems orderitems_order_id_591c3139_fk_orders__id; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.orderitems
    ADD CONSTRAINT orderitems_order_id_591c3139_fk_orders__id FOREIGN KEY (order_id) REFERENCES public.orders(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orderitems orderitems_product_id_0f0de012_fk_products__id; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.orderitems
    ADD CONSTRAINT orderitems_product_id_0f0de012_fk_products__id FOREIGN KEY (product_id) REFERENCES public.products(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: orders orders_user_id_7e2523fb_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_user_id_7e2523fb_fk_users_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: products products_user_id_0be7171c_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_user_id_0be7171c_fk_users_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: profile_profile profile_profile_user_id_7b0aedd8_fk; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.profile_profile
    ADD CONSTRAINT profile_profile_user_id_7b0aedd8_fk FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: reviews reviews_product_id_d4b78cfe_fk_products__id; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_product_id_d4b78cfe_fk_products__id FOREIGN KEY (product_id) REFERENCES public.products(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: reviews reviews_user_id_c23b0903_fk_users_id; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.reviews
    ADD CONSTRAINT reviews_user_id_c23b0903_fk_users_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: shippingaddresss shippingaddresss_order_id_0f61f98a_fk_orders__id; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.shippingaddresss
    ADD CONSTRAINT shippingaddresss_order_id_0f61f98a_fk_orders__id FOREIGN KEY (order_id) REFERENCES public.orders(_id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups users_groups_group_id_2f3517aa_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT users_groups_group_id_2f3517aa_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions users_user_permissio_permission_id_6d08dcd2_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: usef
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT users_user_permissio_permission_id_6d08dcd2_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--
--#
