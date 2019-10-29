# SELECT * FROM titleauthor WHERE title_id = "MC3021" AND royaltyper > 20;
# SELECT * FROM titleauthor WHERE title_id IN ("PS1372","MC3021");
# SELECT * FROM titleauthor WHERE royaltyper > 80;

# https://dev.mysql.com/doc/refman/8.0/en/group-by-functions.html
# SELECT count(*) FROM titleauthor WHERE royaltyper > 80
# SELECT sum(royaltyper) FROM titleauthor WHERE royaltyper > 80

# JOINS 
# https://stackoverflow.com/questions/6294778/mysql-quick-breakdown-of-the-types-of-joins
# SELECT * FROM titles LEFT JOIN titleauthor ON titles.title_id=titleauthor.title_id

# Nulls appear
# SELECT titles.title_id, titleauthor.title_id FROM titles LEFT JOIN titleauthor ON titles.title_id=titleauthor.title_id

# Alias
#SELECT 
#	t.title_id AS Hola, ta.au_id
#	FROM titles AS t
#   LEFT JOIN titleauthor AS ta ON t.title_id=ta.title_id

# Doble JOIN
-- SELECT 
-- 	t.title, au.au_fname, au.au_lname
-- 	FROM titles AS t
-- 	LEFT JOIN titleauthor AS ta ON t.title_id=ta.title_id
-- 	LEFT JOIN authors AS au ON ta.au_id=au.au_id

# Concat
-- SELECT 
-- 	t.title, concat(au.au_fname,' ', au.au_lname) as fullname
-- 	FROM titles AS t
-- 	LEFT JOIN titleauthor AS ta ON t.title_id=ta.title_id
-- 	LEFT JOIN authors AS au ON ta.au_id=au.au_id
     
# GROUP BY
-- SELECT 
-- 	t.title_id, t.title, count(*) as num_authors, GROUP_CONCAT(concat(au.au_fname,' ', au.au_lname))
-- 	FROM titles AS t
-- 	LEFT JOIN titleauthor AS ta ON t.title_id=ta.title_id
-- 	LEFT JOIN authors AS au ON ta.au_id=au.au_id
--     GROUP BY t.title_id
    
# GROUP BY with filter
-- SELECT 
-- 	t.title_id, t.title, count(*) as num_authors, GROUP_CONCAT(concat(au.au_fname,' ', au.au_lname)), year(t.pubdate)
-- 	FROM titles AS t
-- 	LEFT JOIN titleauthor AS ta ON t.title_id=ta.title_id
-- 	LEFT JOIN authors AS au ON ta.au_id=au.au_id
--         WHERE year(t.pubdate) > 2000
--     GROUP BY t.title_id
    
# ORDER BY
SELECT 
	t.title_id, t.title, year(t.pubdate) as yearpub
	FROM titles AS t
	LEFT JOIN titleauthor AS ta ON t.title_id=ta.title_id
    ORDER BY yearpub DESC
     
    
    
    