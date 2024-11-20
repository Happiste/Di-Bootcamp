--select * from language

-- select film.title, film.description, language.name 
-- FROM film inner join language
-- on film.language_id = language.language_id

-- select film.title, film.description, language.name 
-- FROM film right join language
-- on film.language_id = language.language_id

-- create TABLE new_film (
--     id serial primary key,
--     name varchar(255) not null
-- )

-- insert into new_film (name) values
-- ('Venom 3'),
-- ('Thor 5'),
-- ('New Guy')

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


-- delete from new_film where id = 1;


-- update film
-- set language_id = 2 -- use a valid language id from the `language` table
-- where film_id in (1, 2, 3); -- specify film ids to update



