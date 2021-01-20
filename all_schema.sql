-- CREATE DB
DROP DATABASE IF EXISTS kueski_challenge;
CREATE DATABASE kueski_challenge;
USE kueski_challenge;
-- CREATE DEPARTMENTS TABLE
CREATE TABLE IF NOT EXISTS `departments`(
    `department_id` INT(3) UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `department` VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- FILL DEPARTMENTS TABLE
INSERT INTO `departments`(department)
VALUES ('IT'),
('Sales');
-- CREATE EMPLOYEES TABLE
CREATE TABLE IF NOT EXISTS employees (
    `employee_id` INTEGER UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `salary` MEDIUMINT(7) UNSIGNED NOT NULL,
    `department_id` INTEGER UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- FILL EMPLOYEES TABLE
INSERT INTO employees(name,salary,department_id)
VALUES('Joe',70000,1),
('Jim',90000,1),
('Henry',80000,2),
('Sam',60000,2),
('Max',90000,(SELECT department_id FROM departments WHERE department='IT' LIMIT 1));
-- FIND MAX SALARY PER DEPARTMENT, THEN JOIN ANND GROUP
SELECT d.department, e.name, e.salary
FROM employees as e
JOIN (
  SELECT department_id,name,MAX(salary) AS max_salary
  FROM employees
  GROUP BY department_id
) AS t 
 ON e.department_id = t.department_id
 AND e.salary = t.max_salary
JOIN departments as d
  ON e.department_id = d.department_id
ORDER BY d.department,e.salary DESC;
