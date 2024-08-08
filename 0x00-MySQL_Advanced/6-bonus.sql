-- a SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student.
DELIMITER // CREATE PROCEDURE AddBonus(user_id, project_name, score) BEGIN
INSERT INTO `project` (project_name)
SELECT `name`
FROM DUAL
WHERE NOT EXISTS (
        SELECT *
        FROM `projects`
        WHERE `name` = project_name
        LIMIT 1
    );
INSERT INTO corrections(user_id, project_id, score)
VALUES (
        user_id,
        SELECT id
        FROM projects
        WHERE `name` = project_name,
            score
    );
END // DELIMITER;
