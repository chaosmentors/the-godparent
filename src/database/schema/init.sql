-- INFO: Initializing the database

CREATE TABLE IF NOT EXISTS version (
    id INTEGER PRIMARY KEY,
    last_version TEXT
);

INSERT INTO 
    [version] 
(
     [id]
    ,[last_version]
)
SELECT
     0
    ,'0000-00-00.0'
WHERE NOT EXISTS (
    SELECT 1
    FROM
        [version]
    WHERE
        id = 0
)
