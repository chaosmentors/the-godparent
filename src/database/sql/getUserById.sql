-- Returns a person, identified by their row id
-- Created On: Sun 14 Mar 2021 06:34:14 PM CET
-- Last Modified: Sun 14 Mar 2021 06:34:30 PM CET

SELECT
     [rowid] AS [id]
    ,[created_on]   
    ,[description]
    ,[email]
    ,[last_modified_on]
    ,[nickname]
    ,[password_hash]
    ,[pronoun]
    ,[random_id]
    ,[role]
FROM
    [Person]
WHERE
    [rowid] = {}

