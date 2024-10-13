query_1 = "CREATE TABLE Readers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    email VARCHAR(60) UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);"
query_2 = "CREATE TABLE PublishingHouses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    city VARCHAR(20),
    address VARCHAR(120)
);"
query_3 = "CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(60),
    price DECIMAL(5, 2),
    author VARCHAR(60),
    publishing_houses_id INT REFERENCES PublishingHouses(id) ON DELETE SET NULL
);"
query_4 = "CREATE TABLE ReadersBooks (
    reader_id INT REFERENCES Readers(id) ON DELETE CASCADE,
    book_id INT REFERENCES Books(id) ON DELETE CASCADE,
    PRIMARY KEY (reader_id, book_id)
);"
query_5 = "SELECT * FROM Books
WHERE price > 10;"
query_6 = "INSERT INTO PublishingHouses (name, city, address)
VALUES ('Super Books', 'Wilderness', '120 Main Road');"
query_7 = "DELETE FROM Books
WHERE id = 12;"
query_8 = "SELECT DISTINCT R.*
FROM Readers R
JOIN ReadersBooks RB ON R.id = RB.reader_id;"
query_9 = "UPDATE Readers
SET is_active = FALSE
WHERE id = 2;"
query_10 = "ALTER TABLE Readers
ADD COLUMN date_of_birth DATE;"