        SELECT u.name AS user_full_name,
            TO_CHAR(ua.time, 'YYYY-MM-DD HH24:MI:SS') AS achievement_time,
            CASE
                WHEN u.language = 'ru' THEN a.name_rus
                ELSE a.name
            END AS achievement_name
        FROM users u
        LEFT JOIN user_achievement ua ON ua.user_id = u.id
        LEFT JOIN achievements a ON a.id = ua.achievement_id
        WHERE u.name = %s;