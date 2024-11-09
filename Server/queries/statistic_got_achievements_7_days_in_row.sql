WITH consecutive_achievements AS (
    SELECT  user_id,
            time::date AS achievement_date,
            ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY time::date) - EXTRACT(EPOCH FROM time::date) / (24 * 60 * 60) AS date_group
    FROM user_achievement
    GROUP BY user_id, time::date
),
streaks AS (
    SELECT  user_id,
            COUNT(*) AS days_in_a_row
    FROM consecutive_achievements
    GROUP BY user_id, date_group
    HAVING COUNT(*) >= 7
)
SELECT u.name AS user_name
FROM users u
JOIN streaks s ON u.id = s.user_id;