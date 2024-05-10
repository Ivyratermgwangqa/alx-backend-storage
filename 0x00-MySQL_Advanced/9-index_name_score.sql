-- Task 9: Create index on the first letter of name and the score
-- Create an index on the first letter of 'name' and 'score' in the 'names' table
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score);
