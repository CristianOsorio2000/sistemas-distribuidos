CREATE TABLE IF NOT EXISTS tabla (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    value INT
);

INSERT INTO tabla (name, value) VALUES
    ('Productos de aseo', 50),
    ('Alimentos', 150),
    ('Bebidas', 150),
    ('Papeleria', 250);