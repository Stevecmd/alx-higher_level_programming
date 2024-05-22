-- List all shows by their rating from the hbtn_0d_tvshows_rate database

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM hbtn_0d_tvshows.tv_shows
LEFT JOIN hbtn_0d_tvshows.tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.title
ORDER BY rating DESC;
