DROP TABLE IF EXISTS jc_db.applications;
DROP TABLE IF EXISTS jc_db.jobs;
DROP TABLE IF EXISTS jc_db.users;

-- CREATE TABLE jc_db.users (
--     id VARCHAR(60) PRIMARY KEY,
--     username VARCHAR(128) NOT NULL,
--     email VARCHAR(128) NOT NULL,
--     first_name VARCHAR(128),
--     last_name VARCHAR(128),
--     password VARCHAR(128) NOT NULL,
--     role ENUM('Job-Seeker', 'Employer') NOT NULL,
--     created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );

-- CREATE TABLE jc_db.jobs (
--     id VARCHAR(60) PRIMARY KEY,
--     user_id VARCHAR(60) NOT NULL,
--     title VARCHAR(128),
--     description VARCHAR(128),
--     location VARCHAR(128) NOT NULL,
--     salary VARCHAR(128) NOT NULL,
--     requirements VARCHAR(128) NOT NULL,
--     deadline DATETIME NOT NULL,
--     FOREIGN KEY (user_id) REFERENCES users (id),
--     created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );

-- CREATE TABLE jc_db.applications (
--     id VARCHAR(60) PRIMARY KEY,
--     user_id VARCHAR(60) NOT NULL,
--     job_id VARCHAR(60) NOT NULL,
--     cover_letter VARCHAR(258),
--     created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--     updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );

-- use jc_db;

-- -- Sample data for the 'users' table
-- INSERT INTO users (id, username, email, first_name, last_name, password, role) VALUES ('user1', 'john_doe', 'john@example.com', 'John', 'Doe', 'password123', 'Job-Seeker');
-- INSERT INTO users (id, username, email, first_name, last_name, password, role) VALUES ('user2', 'jane_smith', 'jane@example.com', 'Jane', 'Smith', 'secret567', 'Employer');
-- INSERT INTO users (id, username, email, first_name, last_name, password, role) VALUES ('user3', 'john_doe', 'john@example.com', 'John', 'Doe', 'password123', 'Job-Seeker');
-- INSERT INTO users (id, username, email, first_name, last_name, password, role) VALUES ('user4', 'jane_smith', 'jane@example.com', 'Jane', 'Smith', 'secret567', 'Employer');
--     -- Add more user data as needed...

-- -- Sample data for the 'jobs' table
-- INSERT INTO jobs (id, user_id, title, description, location, salary, requirements, deadline) VALUES ('job1', 'user2', 'Software Engineer', 'Develop web applications', 'San Francisco', '100000', 'Python, JavaScript', '2023-12-31 23:59:59');
-- INSERT INTO jobs (id, user_id, title, description, location, salary, requirements, deadline) VALUES ('job2', 'user4', 'Marketing Manager', 'Create marketing campaigns', 'New York', '80000', 'Marketing experience', '2023-12-15 23:59:59');
-- INSERT INTO jobs (id, user_id, title, description, location, salary, requirements, deadline) VALUES ('job3', 'user4', 'Software Engineer', 'Develop web applications', 'San Francisco', '100000', 'Python, JavaScript', '2023-12-31 23:59:59');
-- INSERT INTO jobs (id, user_id, title, description, location, salary, requirements, deadline) VALUES ('job4', 'user2', 'Marketing Manager', 'Create marketing campaigns', 'New York', '80000', 'Marketing experience', '2023-12-15 23:59:59');
-- INSERT INTO jobs (id, user_id, title, description, location, salary, requirements, deadline) VALUES ('job5', 'user2', 'Software Engineer', 'Develop web applications', 'San Francisco', '100000', 'Python, JavaScript', '2023-12-31 23:59:59');
-- INSERT INTO jobs (id, user_id, title, description, location, salary, requirements, deadline) VALUES ('job6', 'user4', 'Marketing Manager', 'Create marketing campaigns', 'New York', '80000', 'Marketing experience', '2023-12-15 23:59:59');
-- INSERT INTO jobs (id, user_id, title, description, location, salary, requirements, deadline) VALUES ('job7', 'user4', 'Software Engineer', 'Develop web applications', 'San Francisco', '100000', 'Python, JavaScript', '2023-12-31 23:59:59');
-- INSERT INTO jobs (id, user_id, title, description, location, salary, requirements, deadline) VALUES ('job8', 'user2', 'Marketing Manager', 'Create marketing campaigns', 'New York', '80000', 'Marketing experience', '2023-12-15 23:59:59');
--     -- Add more job data as needed...

-- -- Sample data for the 'applications' table
-- INSERT INTO applications (id, user_id, job_id, cover_letter) VALUES ('app1', 'user1', 'job1', 'I am interested in this position.');
-- INSERT INTO applications (id, user_id, job_id, cover_letter) VALUES ('app2', 'user3', 'job2', 'I have the required skills for this role.');
-- INSERT INTO applications (id, user_id, job_id, cover_letter) VALUES ('app3', 'user3', 'job3', 'Please find my resume attached.');
-- INSERT INTO applications (id, user_id, job_id, cover_letter) VALUES ('app4', 'user1', 'job4', 'I look forward to the opportunity.');
-- INSERT INTO applications (id, user_id, job_id, cover_letter) VALUES ('app5', 'user1', 'job5', 'My experience matches your requirements.')
--     -- Add more user data as needed...