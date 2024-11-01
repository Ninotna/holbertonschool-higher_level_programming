-- Select the database to use
-- USE hbtn_0d_tvshows_rate;

-- Query to retrieve titles and the sum of ratings for each show
SELECT tv_shows.title, SUM(tv_show_ratings.rating) AS rating_sum
FROM tv_shows
-- Join with tv_show_ratings to get ratings associated with each show
INNER JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
-- Group by show title to calculate the total rating for each show
GROUP BY tv_shows.title
-- Sort results in descending order by the sum of ratings
ORDER BY rating_sum DESC;

