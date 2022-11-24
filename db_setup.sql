CREATE TABLE Author (
    author_id INT AUTO_INCREMENT NOT NULL,
    user_id INT NOT NULL unique,
    rate INT NOT NULL,

    PRIMARY KEY (author_id),
    FOREIGN KEY (user_id) REFERENCES auth_user (id)
);
CREATE TABLE Category (
    category_id INT AUTO_INCREMENT NOT NULL,
    name CHAR(255) NOT NULL UNIQUE,

    PRIMARY KEY (category_id)
);
CREATE TABLE Post (
    post_id INT AUTO_INCREMENT NOT NULL,
    author_id INT NOT NULL unique,
    creation_date DATETIME default current_timestamp NOT NULL,
    title CHAR(255) NOT NULL,
    txt TEXT NOT NULL,
    post_rate INT NOT NULL default 0,

    PRIMARY KEY (post_id),
    FOREIGN KEY (author_id) REFERENCES AUTHOR (author_id)
);
CREATE TABLE PostCategory (
    id INT AUTO_INCREMENT NOT NULL,
    post_id INT NOT NULL,
    category_id INT NOT NULL,

    PRIMARY KEY (id),
    FOREIGN KEY (post_id) REFERENCES Post (post_id),
    FOREIGN KEY (category_id) REFERENCES Category (category_id)
);

CREATE TABLE Comment (
    comm_id INT AUTO_INCREMENT NOT NULL,
    post_id INT NOT NULL,
    user_id INT NOT NULL,
    comm_txt TEXT NOT NULL,
    creation_date DATETIME NOT NULL default current_timestamp,
    comm_rate INT NOT NULL default 0,

    PRIMARY KEY (comm_id),
    FOREIGN KEY (post_id) REFERENCES Post (post_id),
    FOREIGN KEY (user_id) REFERENCES auth_user (id)
);