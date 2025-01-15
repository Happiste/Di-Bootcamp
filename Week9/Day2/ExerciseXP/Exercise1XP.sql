-- SELECT 
--     g.genre_name,
--     m.title AS movie_title,
--     RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS rank
-- FROM 
--     movies.genre AS g
-- JOIN 
--     movies.movie_genres AS mg ON g.genre_id = mg.genre_id
-- JOIN 
--     movies.movie AS m ON mg.movie_id = m.movie_id
-- WHERE 
--     m.popularity IS NOT NULL
-- ORDER BY 
--     g.genre_name, rank;


-- SELECT 
--     pc.company_name,
--     m.title AS movie_title,
--     m.revenue,
--     NTILE(4) OVER (PARTITION BY pc.company_name ORDER BY m.revenue DESC) AS quartile
-- FROM 
--     movies.production_company AS pc
-- JOIN 
--     movies.movie_company AS mc ON pc.company_id = mc.company_id
-- JOIN 
--     movies.movie AS m ON mc.movie_id = m.movie_id
-- WHERE 
--     m.revenue IS NOT NULL
-- ORDER BY 
--     pc.company_name, quartile, m.revenue DESC;

-- SELECT 
--     g.genre_name,
--     m.title AS movie_title,
--     m.budget,
--     SUM(m.budget) OVER (PARTITION BY g.genre_name ORDER BY m.budget DESC ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total_budget
-- FROM 
--     movies.genre AS g
-- JOIN 
--     movies.movie_genres AS mg ON g.genre_id = mg.genre_id
-- JOIN 
--     movies.movie AS m ON mg.movie_id = m.movie_id
-- WHERE 
--     m.budget IS NOT NULL
-- ORDER BY 
--     g.genre_name, running_total_budget DESC;


-- SELECT 
--     g.genre_name,
--     FIRST_VALUE(m.title) OVER (PARTITION BY g.genre_name ORDER BY m.release_date DESC) AS most_recent_movie,
--     MAX(m.release_date) OVER (PARTITION BY g.genre_name) AS release_date
-- FROM 
--     movies.genre AS g
-- JOIN 
--     movies.movie_genres AS mg ON g.genre_id = mg.genre_id
-- JOIN 
--     movies.movie AS m ON mg.movie_id = m.movie_id
-- WHERE 
--     m.release_date IS NOT NULL
-- ORDER BY 
--     g.genre_name, release_date DESC;





