-- Use the hbtn_0d_tvshows database to list all
-- genres not linked to the show Dexter

-- Select the genre names from the tv_genres table
SELECT tv_genres.name
FROM tv_genres

-- Left join with tv_show_genres to find linked genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id

-- Left join with tv_shows to find genres associated with the show "Dexter"
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id AND tv_shows.title = 'Dexter'

-- Filter out genres linked to "Dexter"
WHERE tv_shows.id IS NULL

-- Order results by genre name in ascending order
ORDER BY tv_genres.name;
