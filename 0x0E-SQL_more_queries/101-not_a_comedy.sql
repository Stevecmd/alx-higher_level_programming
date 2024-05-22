-- lists all shows without the genre Comedy
-- in the database hbtn_0d_tvshows.

-- Retrieve shows without the genre "Comedy"
SELECT tv_shows.title
FROM tv_shows
-- Left join with tv_show_genres to find linked genres
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Left join with tv_genres to find genres associated with "Comedy"
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id AND tv_genres.name = 'Comedy'
-- Filter out shows with the genre "Comedy"
WHERE tv_genres.id IS NULL
-- Order results by show title in ascending order
ORDER BY tv_shows.title;
