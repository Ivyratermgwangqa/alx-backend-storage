# 0x00. MySQL advanced

## Overview
This project focuses on advanced MySQL concepts and tasks, including creating tables with constraints, optimizing queries, implementing stored procedures, triggers, views, and indexing. The tasks aim to provide hands-on experience with complex SQL operations.

## Project Structure
The project contains several SQL scripts to accomplish different tasks. The following is an outline of the tasks:

### Task 0: Unique Users Table
Create a `users` table with unique constraints on the `email` column to ensure no duplicate entries. The table includes `id`, `email`, and `name`.

### Task 1: Users Table with Country Enumeration
Create a `users` table with an enumeration for `country`, ensuring it defaults to `US`. This task introduces enumerations in MySQL.

### Task 2: Rank Country Origins by Number of Fans
Rank the country origins of metal bands based on the number of non-unique fans. This task involves aggregations and grouping in SQL.

### Task 3: List Bands by Longevity
List all bands with `Glam rock` as their main style, ranked by their longevity. This involves computing the lifespan of bands.

### Task 4: Create a Trigger for Inventory Management
Create a trigger that decreases the quantity of an item after adding a new order. Triggers help ensure data consistency when multiple tables are updated.

### Task 5: Create a Trigger for Email Validation
Create a trigger that resets the `valid_email` attribute when the email changes. This helps with email validation and maintaining consistency.

### Task 6: Stored Procedure for Adding Bonus
Create a stored procedure `AddBonus` to add a new correction for a student, creating a new project if necessary.

### Task 7: Stored Procedure to Compute Average Score
Create a stored procedure `ComputeAverageScoreForUser` to compute and store the average score for a specific user.

### Task 8: Create an Index on the First Letter of a Name
Create an index `idx_name_first` on the first letter of a name for faster search operations.

### Task 9: Create an Index on the First Letter and Score
Create an index `idx_name_first_score` on the first letter of a name and the `score`.

### Task 10: Create a Function for Safe Division
Create a function `SafeDiv` that divides one number by another, returning 0 if the divisor is zero. This avoids division-by-zero errors.

### Task 11: Create a View for Students Needing Meetings
Create a view `need_meeting` that lists all students with scores below 80 and either no last meeting or more than a month since the last meeting.

### Task 12: Stored Procedure for Computing Average Weighted Score
Create a stored procedure `ComputeAverageWeightedScoreForUser` to compute and store the average weighted score for a specific student, considering project weights.

### Task 13: Stored Procedure for All Users' Average Weighted Score
Create a stored procedure `ComputeAverageWeightedScoreForUsers` that computes the average weighted score for all students.

## Instructions
To execute these SQL scripts, ensure MySQL is running on your system. You can use the following command to start MySQL:

```bash
sudo service mysql start
```

After starting MySQL, execute the SQL scripts in the correct order to avoid errors. To import an SQL script, use:

```bash
mysql -uroot -p my_database < script_name.sql
```

Enter your MySQL root password when prompted. Replace `my_database` with the name of your database, and `script_name.sql` with the name of the SQL script.

## Troubleshooting
If you encounter errors, check the following:
- Ensure MySQL is running and you have the correct root password.
- Check for syntax errors in the SQL scripts.
- Look at the MySQL error logs for more information:
  ```bash
  cat /var/log/mysql/error.log
  ```

## Further Assistance
If you need further assistance or additional guidance, consult your course instructor, project documentation, or a MySQL expert.

## License
