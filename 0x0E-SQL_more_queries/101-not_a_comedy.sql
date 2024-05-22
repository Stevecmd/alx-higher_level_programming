-- lists all shows without the genre Comedy
-- in the database hbtn_0d_tvshows.

-- Retrieve shows without the genre "Comedy"
SELECT title
FROM tv_shows
WHERE title NOT IN
(
    -- Subquery to find titles of shows linked to "Comedy"
    SELECT tv_shows.title
    FROM tv_shows
    LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
-- Group the results by show title
GROUP BY title
-- Order results by show title in ascending order
ORDER BY title ASC;
