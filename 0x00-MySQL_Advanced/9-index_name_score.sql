-- Task 9: Create index on the first letter of name and the score
CREATE INDEX idx_name_first_score
ON names (SUBSTRING(name, 1, 1), score);
