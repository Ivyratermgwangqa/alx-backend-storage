-- Task 5: Create trigger to reset valid_email when email changes
DELIMITER //
CREATE TRIGGER reset_valid_email_on_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
//
DELIMITER ;
