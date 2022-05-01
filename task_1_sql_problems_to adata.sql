-- TABLES CREATIONS BY ORDER: JOBS, LOCATIONS, DEPARTMENTS, EMPLOYEES, JOB_HISTORY
-- CREATE TABLE Jobs(
--    Job_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--    Job_title VARCHAR(100)    NOT NULL,
--    Min_salary NUMERIC(6),
--    Max_salary NUMERIC(6)
-- );

-- CREATE TABLE Locations(
--    	Location_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--    	street_address VARCHAR(100),
-- 	postal_code VARCHAR(12),
-- 	city VARCHAR(40)    NOT NULL,
-- 	state_province VARCHAR(40)
-- );

-- CREATE TABLE Departments(
--    	department_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--    	department_name VARCHAR(32) NOT NULL,
-- 	manager_id INT,
-- 	location_id INT,
-- 	CONSTRAINT Departments_locations FOREIGN KEY (location_id) REFERENCES Locations(Location_id)
-- );

-- CREATE TABLE Employees(
--    	employee_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     first_name  VARCHAR(25)     NOT NULL,
--     last_name   VARCHAR(25)     NOT NULL,
--     email VARCHAR(25),
-- 	phone_number VARCHAR(25),
--     hire_date   DATE            NOT NULL,
--    	job_id INT NOT NULL,
-- 	salary NUMERIC(12, 2),
-- 	manager_id INT,
-- 	department_id INT,
-- 	CONSTRAINT department_employee FOREIGN KEY (department_id) REFERENCES Departments(department_id),
-- 	CONSTRAINT job_employee FOREIGN KEY (job_id) REFERENCES Jobs(Job_id)
-- );

-- CREATE TABLE Job_history(
-- 	employee_id  INT NOT NULL,
-- 	department_id  INT,
--    	job_id INT NOT NULL,
-- 	start_date   DATE NOT NULL,
-- 	end_date   DATE  NOT NULL,
-- 	CONSTRAINT job_history_jobs FOREIGN KEY (job_id) REFERENCES Jobs(Job_id),
-- 	CONSTRAINT job_history_dep FOREIGN KEY (department_id) REFERENCES Departments(department_id),
-- 	CONSTRAINT job_history_emp FOREIGN KEY (employee_id) REFERENCES Employees(employee_id)
-- );


-- POPULATE TABLES JUST FOR TESTING
-- INSERT INTO Jobs(Job_title, Min_salary, Max_salary) VALUES ('Graphic Designer', 360000, 870000);
-- INSERT INTO Jobs(Job_title, Min_salary, Max_salary) VALUES ('Manager', 560000, 986000);
-- INSERT INTO Jobs(Job_title, Min_salary, Max_salary) VALUES ('Python Developer', 350000, 970000);
-- INSERT INTO Jobs(Job_title, Min_salary, Max_salary) VALUES ('Data Engineer', 350000, 880000);
-- INSERT INTO Jobs(Job_title, Min_salary, Max_salary) VALUES ('PHP Developer', 330000, 950000);
-- INSERT INTO Jobs(Job_title, Min_salary, Max_salary) VALUES ('Team Lead', 460000, 980000);

-- INSERT INTO Locations (street_address, postal_code, city, state_province) 
-- 	VALUES ('Hodzhanpv str 56', '0890043', 'Almaty', 'Almaty');
-- INSERT INTO Locations (street_address, postal_code, city, state_province) 
-- 	VALUES ('Abylaikhan ave 136', '0760038', 'Talgar', 'Almaty');
-- INSERT INTO Locations (street_address, postal_code, city, state_province) 
-- 	VALUES ('Furmanov pros 32', '1280042', 'Mamamam', 'Almaty');
-- INSERT INTO Locations (street_address, postal_code, city, state_province) 
-- 	VALUES ('Abai str 233', '0790325', 'Almaty', 'Almaty');
-- INSERT INTO Locations (street_address, postal_code, city, state_province) 
-- 	VALUES ('Elstsyin str 156', '0367045', 'Taraz', 'Almaty');

-- INSERT INTO Departments(department_name, manager_id, location_id) VALUES ('DevOps', 67, 3);
-- INSERT INTO Departments(department_name, manager_id, location_id) VALUES ('HR', 53, 2);
-- INSERT INTO Departments(department_name, manager_id, location_id) VALUES ('Analytics', 87, 3);
-- INSERT INTO Departments(department_name, manager_id, location_id) VALUES ('Sales', 81, 1);
-- INSERT INTO Departments(department_name, manager_id, location_id) VALUES ('Marketing', 50, 4);
-- INSERT INTO Departments(department_name, manager_id, location_id) VALUES ('Inventory', 409, 5);
-- INSERT INTO Departments(department_name, manager_id, location_id) VALUES ('IT Engineers', 708, 5);

-- INSERT INTO Employees(first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
-- 	VALUES ('Amaleyia', 'Koi', 'amykoi@deloitte.ru', '+35678400877', '2019-03-14',2, 980000.00, NULL, 4);
-- INSERT INTO Employees(first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
-- 	VALUES ('David', 'Menzhik', 'davidmenzhik@gmail.com', '+87836900442', '2020-12-10', 3, 560000.00, 409, 1);
-- INSERT INTO Employees(first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
-- 	VALUES ('Lora', 'Kouchuk', 'lora_kou@yandex.ru', '+7567745530', '2020-07-24', 4, 768000.00, NULL, 7);
-- INSERT INTO Employees(first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
-- 	VALUES ('David', 'Mandoloryn', 'mandolorynd@gmail.com', '+45787890442', '2020-08-15', 1, 868900.00, 708, 7);
-- INSERT INTO Employees(first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
-- 	VALUES ('Akmaral', 'Koishy', 'akmaralkoi@mail.ru', '+7669045877', '2018-03-14', 6, 980000.00, NULL, 3);
-- INSERT INTO Employees(first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id)
-- 	VALUES ('David', 'Ishmashel', 'davidismashel@gmail.com', '+87830043200', '2022-01-10', 5, 560000.00, 50, 1);

-- INSERT INTO Job_history (employee_id, department_id, job_id, start_date, end_date)
-- 	VALUES (1, 6, 2, '2019-03-14', '2020-04-15');
-- INSERT INTO Job_history(employee_id, department_id, job_id, start_date, end_date)
-- 	VALUES (2, 7, 3, '2020-12-10', '2022-05-01');
-- INSERT INTO Job_history(employee_id, department_id, job_id, start_date, end_date)
-- 	VALUES (3, 5, 4, '2020-07-24', '2022-04-15');
-- INSERT INTO Job_history(employee_id, department_id, job_id, start_date, end_date)
-- 	VALUES (4, 4, 1, '2020-08-15', '2022-10-25');
-- INSERT INTO Job_history(employee_id, department_id, job_id, start_date, end_date)
-- 	VALUES (5, 3, 6, '2018-03-14', '2020-05-10');
-- INSERT INTO Job_history(employee_id, department_id, job_id, start_date, end_date)
-- 	VALUES (6, 3, 5, '2022-01-10', '2022-05-01');

-- POPULATION WITH TRIGGERS
-- CREATE OR REPLACE FUNCTION locations_insert_trigger_fnc() 
-- RETURNS trigger AS 
-- $$
-- BEGIN
-- 		INSERT INTO Locations(street_address, postal_code, city, state_province)
-- 		VALUES(NEW.street_address, NEW.postal_code, NEW. city, NUll);
-- 	RETURN NEW;
-- END;
-- $$
-- LANGUAGE 'plpgsql';

-- -- DROP TRIGGER job_insert_trigger on Jobs;
-- CREATE OR REPLACE TRIGGER locations_insert_trigger
-- AFTER INSERT ON Locations
-- FOR EACH ROW
-- EXECUTE PROCEDURE locations_insert_trigger_fnc();
  
-- INSERT INTO Jobs(Job_title, Min_salary, Max_salary) 
-- 	VALUES ('UI/UX Designer', 330000, 770000);

-- INSERT INTO Locations (street_address, postal_code, city, state_province) 
-- 	VALUES ('Auezov str 56', '0560043', 'Almaty', 'Almaty');

-- TASK 1
-- get fullname, salary and job with join methods by creating view
CREATE VIEW Employees_information AS
SELECT e.first_name|| ' ' || e.last_name AS fullname, e.salary, j.job_title
FROM Employees e
LEFT JOIN Jobs j
ON e.job_id = j.job_id
RIGHT OUTER JOIN Departments d
on e.department_id = d.department_id
WHERE d.department_name = 'DevOps';
-- find by names employees
SELECT * FROM Employees_information
WHERE fullname LIKE 'David%';

-- TASK 2
-- get avg salary by departments with view
CREATE VIEW Departments_average_salary AS
SELECT d.department_name, AVG(e.salary) as average_salary
FROM Departments d
RIGHT OUTER JOIN Employees e
ON d.department_id = e.department_id
GROUP BY d.department_id;

SELECT * FROM Departments_average_salary;

-- TASK 3
-- create function that finds avg salary by max and min values
CREATE OR REPLACE FUNCTION avg_salary(min_sal Numeric, max_sal Numeric) RETURNS INTEGER
LANGUAGE SQL
IMMUTABLE
RETURNS NULL ON NULL INPUT
RETURN (min_sal + max_sal)/2;
-- create function that compares avg salaries
CREATE OR REPLACE FUNCTION avg_salary_compare(avg_jobs Numeric, avg_emps Numeric) RETURNS Text
LANGUAGE SQL
IMMUTABLE
RETURNS NULL ON NULL INPUT
RETURN CASE WHEN avg_jobs > avg_emps THEN 'Yes'
ELSE 'NO'
END;
-- create materialised view to always have on hand and calling function that finds avg sal
CREATE MATERIALIZED VIEW avg_salary_finder AS
SELECT j.job_title, avg_salary(j.Min_salary, j.Max_salary) AS avg_sal_jobs, AVG(e.salary) as avg_sal_emp
FROM Jobs j
LEFT JOIN Employees e
ON j.job_id = e.job_id
GROUP BY j.job_id;
-- if changes happened on table, refresh view
--REFRESH MATERIALIZED VIEW avg_salary_finder;
-- now select from view all information with function that compares
SELECT asf.job_title, asf.avg_sal_jobs,
avg_salary_compare(asf.avg_sal_jobs, asf.avg_sal_emp) AS is_avg_sal_by_jobs_more_than_avg_sal_emp
FROM avg_salary_finder asf;

-- TASK 4
-- create view where department name, fullname of employee are selected by hire date
CREATE OR REPLACE VIEW departments_employees AS
SELECT d.department_name, e.first_name|| ' ' || e.last_name AS fullname 
FROM Employees e
LEFT JOIN Departments d
ON e.department_id = d.department_id
where e.hire_date  >= '01/01/2021';

-- create a function where the view details are dumped into json
CREATE OR REPLACE FUNCTION dep_emps_json()
RETURNS SETOF json
AS
$$
        SELECT array_to_json(ARRAY_AGG(T)) as events_as_json
		from departments_employees t;
$$
LANGUAGE SQL;

-- now just select job name, department name in array, call the function above, also i sued function i created in third task to find avg sal
-- you need to sort by hire date as well here - to know which record exactly we need and group by jobs of course
SELECT j.job_title, ARRAY_AGG(department_name), dep_emps_json(),
avg_salary(j.Min_salary, j.Max_salary) AS average_salary_by_jobs
FROM Employees e
LEFT JOIN Jobs j
ON e.job_id = j.job_id
RIGHT OUTER JOIN Departments d 
ON e.department_id = d.department_id
where e.hire_date  >= '01/01/2021'
group by j.job_id;  



