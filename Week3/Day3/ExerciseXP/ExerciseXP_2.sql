-- UPDATE film
-- SET language_id = 2 
-- WHERE title IN ('Film A', 'Film B');

-- INSERT INTO customer (store_id, first_name, last_name, email, address_id, activebool, create_date)
-- VALUES (1, 'John', 'Doe', 'johndoe@example.com', 5, true, CURRENT_DATE);

-- DROP TABLE customer_review CASCADE;

-- SELECT COUNT(*)
-- FROM rental
-- WHERE return_date IS NULL;

-- SELECT film.title, film.replacement_cost
-- FROM rental
-- JOIN inventory ON rental.inventory_id = inventory.inventory_id
-- JOIN film ON inventory.film_id = film.film_id
-- WHERE rental.return_date IS NULL
-- ORDER BY film.replacement_cost DESC
-- LIMIT 30;


-- SELECT film.title
-- FROM film
-- JOIN film_actor ON film.film_id = film_actor.film_id
-- JOIN actor ON film_actor.actor_id = actor.actor_id
-- WHERE film.description ILIKE '%sumo%'
--   AND actor.first_name = 'Penelope'
--   AND actor.last_name = 'Monroe';

-- SELECT film.title
-- FROM film
-- WHERE film.length < 60
--   AND film.rating = 'R';


-- SELECT film.title
-- FROM film
-- JOIN inventory ON film.film_id = inventory.film_id
-- JOIN rental ON inventory.inventory_id = rental.inventory_id
-- JOIN customer ON rental.customer_id = customer.customer_id
-- WHERE customer.first_name = 'Matthew'
--   AND customer.last_name = 'Mahan'
--   AND (film.title ILIKE '%boat%' OR film.description ILIKE '%boat%')
--   AND film.replacement_cost = (SELECT MAX(replacement_cost) FROM film);



