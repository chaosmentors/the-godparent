-- FILE: schema.sql
-- Author: Famaniel (https://github.com/famaniel)
-- Created On: Wed 10 Feb 2021 10:35:17 PM CET
-- Last Modified: Wed 10 Feb 2021 11:44:57 PM CET
-- Description: Generates the database schema for the godparent application.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS PersonTag;
DROP TABLE IF EXISTS Status;
DROP TABLE IF EXISTS Verification;
DROP TABLE IF EXISTS Tag;
DROP TABLE IF EXISTS Person;

-- Create Tables
CREATE TABLE Person (
     [created_on] TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,[description] TEXT
    ,[email] TEXT UNIQUE
    ,[last_modified_on] TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,[nickname] TEXT
    ,[password_hash] TEXT
    ,[pronoun] TEXT
    ,[random_id] TEXT 
    ,[role] INTEGER NOT NULL
);
CREATE INDEX person_email_index ON [Person] ([email]);
CREATE INDEX person_random_id_index ON [Person] ([random_id]);

CREATE TABLE Tag (
     [created_on] TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,[last_modified_on] TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,[name] TEXT UNIQUE
);

CREATE TABLE Verification (
     [created_on] TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,[last_modified_on] TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,[person_id] INTEGER NOT NULL
    ,[verification_token] TEXT UNIQUE
    ,FOREIGN KEY([person_id]) REFERENCES [Person] ([rowid])
);
CREATE INDEX verification_verification_token_index ON [Verification] ([verification_token]);

CREATE TABLE Status (
     [created_on] TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,[last_modified_on] TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,[person_id] INTEGER NOT NULL
    ,[status] INTEGER NOT NULL
    ,FOREIGN KEY([person_id]) REFERENCES [Person] ([rowid])
);
CREATE INDEX status_status_index ON [Status] ([status]);

CREATE TABLE PersonTag (
     [created_on] TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,[last_modified_on] TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    ,[person_id] INTEGER NOT NULL
    ,[tag_id] INTEGER NOT NULL
    ,FOREIGN KEY([person_id]) REFERENCES [Person] ([rowid])
    ,FOREIGN KEY([tag_id]) REFERENCES [Tag] ([rowid])
);

-- Create an UPDATE trigger, that keeps the [last_modified_on] field 
-- current, when running.
CREATE TRIGGER IF NOT EXISTS 
    update_person 
UPDATE OF
     [created_on]
    ,[description]
    ,[email]
    ,[nickname]
    ,[password_hash]
    ,[pronoun]
    ,[random_id]
    ,[role]
ON 
    [Person]
BEGIN
    UPDATE 
        [Person]
    SET
        [last_modified_on] = CURRENT_TIMESTAMP
    WHERE
        [rowid] = NEW.[rowid];
END;

CREATE TRIGGER IF NOT EXISTS 
    update_tag 
UPDATE OF
     [created_on]
    ,[name]
ON 
    [Tag]
BEGIN
    UPDATE 
        [Tag]
    SET
        [last_modified_on] = CURRENT_TIMESTAMP
    WHERE
        [rowid] = NEW.[rowid];
END;

CREATE TRIGGER IF NOT EXISTS 
    update_verification 
UPDATE OF
     [created_on]
    ,[person_id]
    ,[verification_token]
ON 
    [Tag]
BEGIN
    UPDATE 
        [Verification]
    SET
        [last_modified_on] = CURRENT_TIMESTAMP
    WHERE
        [rowid] = NEW.[rowid];
END;

CREATE TRIGGER IF NOT EXISTS 
    update_status
UPDATE OF
     [created_on]
    ,[person_id]
    ,[status]
ON 
    [Status]
BEGIN
    UPDATE 
        [Status]
    SET
        [last_modified_on] = CURRENT_TIMESTAMP
    WHERE
        [rowid] = NEW.[rowid];
END;

CREATE TRIGGER IF NOT EXISTS 
    update_person_tag
UPDATE OF
     [created_on]
    ,[person_id]
    ,[tag_id]
ON 
    [PersonTag]
BEGIN
    UPDATE 
        [PersonTag]
    SET
        [last_modified_on] = CURRENT_TIMESTAMP
    WHERE
        [rowid] = NEW.[rowid];
END;

-- vim: set nospell: Wed 10 Feb 2021 11:44:52 PM CET
