-- Query to retrieve genres not linked to the show "Dexter"
SELECT tv_genres.name
FROM tv_genres
-- Ensure genre ID is not in the list of genres linked to "Dexter"
WHERE tv_genres.id NOT IN (
    -- Subquery to find all genre IDs linked to the show "Dexter"
    SELECT tv_show_genres.genre_id
    FROM tv_show_genres
    -- Join with tv_shows table to filter only where the title is "Dexter"
    INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
-- Order the results in ascending order by genre name
ORDER BY tv_genres.name ASC;
