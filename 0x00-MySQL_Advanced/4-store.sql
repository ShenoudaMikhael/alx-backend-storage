-- SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
-- upon new orders it should work
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
