-- Task 13:
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;

    -- Declare a cursor to fetch all user IDs
    DECLARE user_cursor CURSOR FOR
        SELECT id FROM users;

    -- Declare handlers for cursor control
    DECLARE CONTINUE HANDLER FOR NOT FOUND
        SET user_id = NULL;

    -- Open the cursor
    OPEN user_cursor;

    -- Loop through all user IDs and compute the average weighted score
    user_loop: LOOP
        FETCH user_cursor INTO user_id;

        IF user_id IS NULL THEN
            LEAVE user_loop; -- Exit loop when no more users
        END IF;

        -- Call the procedure for individual user computation
        CALL ComputeAverageWeightedScoreForUser(user_id);

    END LOOP user_loop;

    -- Close the cursor
    CLOSE user_cursor;
END;
//

DELIMITER ;
