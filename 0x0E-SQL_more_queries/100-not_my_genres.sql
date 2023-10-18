-- Script: 100-not_my_genres.sql
-- Description: Lists all genres not linked to the show Dexter.
-- Allowed editors: vi, vim, emacs
-- Environment: Ubuntu 20.04 LTS, MySQL 8.0.25

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Find the genres linked to the show Dexter
SELECT genre_id
FROM tv_show_genres
WHERE show_id = (
    SELECT id
    FROM tv_shows
    WHERE title = 'Dexter'
);

-- Find the genres that are not linked to the show Dexter
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_show_genres
    WHERE show_id = (
        SELECT id
        FROM tv_shows
        WHERE title = 'Dexter'
    )
)
ORDER BY name;

