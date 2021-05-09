-- INFO: Create user table, to allow logins

CREATE TABLE IF NOT EXISTS [user] (
    [description] TEXT,
    [email] TEXT NOT NULL UNIQUE,
    [is_godmother] INTEGER NOT NULL DEFAULT 0 CHECK([is_godmother] IN (0,1)),
    [nickname] TEXT,
    [password_hash] TEXT,
    [pronoun] TEXT,
    [role] INTEGER NOT NULL DEFAULT 0 CHECK([role] IN (0,1))
);

CREATE TABLE IF NOT EXISTS [tags] (
    [name] TEXT
);

CREATE TABLE IF NOT EXISTS [user_tags] (
    [user_id] INTEGER,
    [tag_id] INTEGER,
    FOREIGN KEY ([user_id]) REFERENCES [user]([rowid]),
    FOREIGN KEY ([tag_id]) REFERENCES [tags]([rowid])
);
