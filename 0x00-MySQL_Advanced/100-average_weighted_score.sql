-- Task 12:
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight INT DEFAULT 0;
    DECLARE weighted_sum FLOAT DEFAULT 0;

    -- Calculate the total weight for all projects related to the user
    SELECT SUM(p.weight) INTO total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Calculate the weighted sum of scores for all projects related to the user
    SELECT SUM(c.score * p.weight) INTO weighted_sum
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Compute the average weighted score
    DECLARE average_weighted_score FLOAT;

    IF total_weight = 0 THEN
        SET average_weighted_score = 0; -- Avoid division by zero
    ELSE
        SET average_weighted_score = weighted_sum / total_weight;
    END IF;

    -- Update the user's average score with the calculated value
    UPDATE users
    SET average_score = average_weighted_score
    WHERE id = user_id;
END;
//

DELIMITER ;
