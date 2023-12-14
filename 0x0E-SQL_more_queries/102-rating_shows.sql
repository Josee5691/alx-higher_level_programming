-- Save this script in a file, e.g., rating_shows.sql

-- Select all shows and their rating sum
SELECT tv_shows.title, SUM(tv_show_ratings.rating) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY rating_sum DESC;
