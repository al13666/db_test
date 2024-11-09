WITH user_achievement_max_points AS (
    SELECT  u.name AS user_full_name,
            SUM(a.points) AS total_points
    FROM users u
    LEFT JOIN user_achievement ua ON ua.user_id = u.id
    LEFT JOIN achievements a ON a.id = ua.achievement_id
    GROUP BY u.name
)
SELECT user_full_name, total_points
FROM user_achievement_max_points
WHERE total_points = (SELECT MAX(total_points) FROM user_achievement_max_points);