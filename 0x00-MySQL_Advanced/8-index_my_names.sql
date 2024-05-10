-- Task 8: Create index on the first letter of name
CREATE INDEX idx_name_first
ON names (SUBSTRING(name, 1, 1));
