-- a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average 
-- score for a student. Note: An average score can be a decimal
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(user_id)
BEGIN
   	UPDATE users
	SET
	average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
	WHERE id = user_id;
END //
DELIMITER
