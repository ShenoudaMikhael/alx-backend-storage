-- a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
-- only when the email has been changed.
CREATE TRIGGER invalidate_email
AFTER UPDATE ON users.email FOR EACH ROW
UPDATE users
SET valid_email = 0
WHERE email = NEW.email;
