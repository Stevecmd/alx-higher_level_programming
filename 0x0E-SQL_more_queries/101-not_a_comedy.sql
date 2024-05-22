-- lists all shows without the genre Comedy
-- in the database hbtn_0d_tvshows.

-- Retrieve shows without the genre "Comedy"
SELECT tv_shows.title
FROM tv_shows
-- Left join with tv_shows_genres to find linked genres
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
-- Left join with tv_genres to find genres associated with "Comedy"
LEFT JOIN tv_genres ON tv_shows_genres.genre_id = tv_genres.id
-- Filter out shows with the genre "Comedy"
WHERE tv_genres.name = 'Comedy'
AND tv_genres.id IS NULL
-- Order results by show title in ascending order
ORDER BY tv_shows.title;