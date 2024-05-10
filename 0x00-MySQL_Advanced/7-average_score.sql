-- Task 7: Create stored procedure ComputeAverageScoreForUser
DELIMITER //

-- Create a stored procedure to compute average score for a specific user
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_scores INT;
    DECLARE sum_scores FLOAT;

    -- Calculate the total number of scores and the sum of scores for the user
    SELECT COUNT(*) INTO total_scores, SUM(score) INTO sum_scores
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average score
    DECLARE average_score FLOAT;
    IF total_scores = 0 THEN
        SET average_score = 0; -- Avoid division by zero
    ELSE
        SET average_score = sum_scores / total_scores;
    END IF;

    -- Update the user's average score in the 'users' table
    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;

END //
//
DELIMITER ;
