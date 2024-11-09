WITH user_points AS (
    SELECT  u.id AS user_id,
            u.name AS user_name,
            COALESCE(SUM(a.points),0) AS total_points
    FROM users u
    LEFT JOIN user_achievement ua ON ua.user_id = u.id
    LEFT JOIN achievements a ON a.id = ua.achievement_id
    GROUP BY u.id, u.name
),
points_differences AS(
    SELECT  u1.user_name AS user1_name,
            u1.total_points AS user1_points,
            u2.user_name AS user2_name,
            u2.total_points AS user2_points,
            ABS (u1.total_points - u2.total_points) AS point_difference
FROM user_points u1
JOIN user_points u2 ON u1.user_id <u2.user_id
)
SELECT user1_name, user1_points, user2_name, user2_points, point_difference
FROM points_differences
WHERE point_difference = (SELECT MIN(point_difference) FROM points_differences);