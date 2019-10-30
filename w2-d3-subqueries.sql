# Subquery WHERE
-- SELECT * FROM titles 
-- 	WHERE pub_id IN (
-- 		SELECT pub_id FROM publishers WHERE state='MA'
--     );

# Temporal TABLE (subquery)
-- SELECT * FROM (
-- 	SELECT title_id, count(*) AS totalauthors FROM titleauthor GROUP BY title_id
-- ) AS x WHERE totalauthors=2
