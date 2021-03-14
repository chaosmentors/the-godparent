-- Returns the id of a person, identified by their e-mail address
-- Created On: Wed 03 Mar 2021 08:28:49 PM CET
-- Last Modified: Sun 14 Mar 2021 04:13:16 PM CET

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
    [id] = '{}'

