--EXERCISE XP 1

-- select name from language

-- SELECT film.title AS film_title, 
--        film.description AS film_description, 
--        language.name AS language_name
-- FROM film
-- JOIN language ON film.language_id = language.language_id;

-- SELECT film.title AS film_title, 
--        film.description AS film_description, 
--        language.name AS language_name
-- FROM language
-- LEFT JOIN film ON language.language_id = film.language_id;


-- CREATE TABLE new_film (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );

-- INSERT INTO new_film (name) VALUES 
-- ('Venom 3'),
-- ('Thor 5'),
-- ('New Guy');

-- create table customer_review (
--     review_id serial primary key,
--     film_id int not null,
--     language_id int not null,
--     title varchar(255) not null,
--     score smallint check (score between 1 and 10),
--     review_text text,
--     last_update timestamp default current_timestamp,
--     constraint fk_film foreign key (film_id) references new_film (id) on delete cascade,
--     constraint fk_language foreign key (language_id) references language (language_id)
-- )

-- INSERT INTO customer_review (film_id, language_id, title, score, review_text)
-- VALUES 
-- (1, 1, 'Great Movie', 9, 'This film was fantastic!'),
-- (2, 2, 'Good Effort', 7, 'A decent watch.');


-- DELETE FROM new_film WHERE id = 1;




