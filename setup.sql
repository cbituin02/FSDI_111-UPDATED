
-- Creates a user database table: 

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45) NOT NULL,
    last_name VARCHAR(45) NOT NULL,
    hobbies TEXT,
    active BOOLEAN NOT NULL DEFAULT 1
);

-- INSERT DUMMY DATA

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Caleb",
    "Bituin",
    "Video Games"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "John",
    "Doe",
    "Playing Tennis"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Spongebob",
    "Squarepants",
    "Jellyfish Catching"
);

INSERT INTO user (
    first_name,
    last_name,
    hobbies
) VALUES (
    "Chowder",
    "N/A",
    "Cooking"
);