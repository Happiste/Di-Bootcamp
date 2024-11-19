/*--1.
select * from customer

select concat(first_name, ' ', last_name) as full_name from customer

select distinct create_date from customer duplicate 

select * from customer order by first_name desc

select film_id, title, description, release_year, rental_rate from film order by rental_rate asc 





select address, phone, district from address where district = 'Texas'


select * from film where film_id between 15 and 150


select film_id, title, description, length, rental_rate
from film
where title = 'Rabbi Jacob'



select film_id, title, description, length, rental_rate
from film
where title like 'Ra%'



select * from film order by rental_rate asc limit 10


select * from film order by rental_rate asc limit 20


select customer.first_name,
		customer.last_name,
		payment.amount,
		payment.payment_date
from customer inner join payment
on customer.customer_id = payment.customer_id
order by customer.customer_id asc



select film_id, title, description, length, rental_rate
from film
where film_id not in (select film_id from inventory)


select country.country_id,  country.country,city.city  from city inner join country
on country.country_id = city.country_id order by country_id asc



select  
    c.customer_id,
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_date,
    p.staff_id as staff_member_id
from 
    customer c
join 
    payment p on c.customer_id = p.customer_id
order by 
    p.staff_id;
*/