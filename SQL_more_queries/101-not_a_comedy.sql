-- Select the database to use
USE hbtn_0d_tvshows;

-- Query to retrieve titles of shows that do not have the genre "Comedy"
SELECT tv_shows.title
FROM tv_shows
-- Ensure show ID is not in the list of shows linked to the genre "Comedy"
WHERE tv_shows.id NOT IN (
    -- Subquery to find all show IDs linked to the genre "Comedy"
    SELECT tv_show_genres.show_id
    FROM tv_show_genres
    -- Join with tv_genres table to filter only where the genre name is "Comedy"
    INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
-- Order the results in ascending order by show title
ORDER BY tv_shows.title ASC;
