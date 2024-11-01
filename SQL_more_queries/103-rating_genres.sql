-- Select the database to use
-- USE hbtn_0d_tvshows_rate;

-- Query to retrieve each genre's name and the sum of ratings associated with it
SELECT tv_genres.name, SUM(tv_show_ratings.rating) AS rating_sum
FROM tv_genres
-- Join tv_show_genres to link genres with shows, and tv_show_ratings to include ratings
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
-- Group by genre name to calculate the total rating for each genre
GROUP BY tv_genres.name
-- Sort results in descending order by the sum of ratings
ORDER BY rating_sum DESC;
