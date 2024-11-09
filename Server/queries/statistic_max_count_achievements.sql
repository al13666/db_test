WITH user_achievement_count AS (
    SELECT  u.id,
            u.name AS user_full_name,
            COUNT(ua.achievement_id) AS achievement_count
    FROM users u
    LEFT JOIN user_achievement ua ON ua.user_id = u.id
    GROUP BY u.id, u.name
)
SELECT user_full_name, achievement_count
FROM user_achievement_count
WHERE achievement_count = (SELECT MAX(achievement_count) FROM user_achievement_count);