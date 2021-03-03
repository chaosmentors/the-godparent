-- Returns the id of a person, identified by their e-mail address
-- Created On: Wed 03 Mar 2021 08:09:44 PM CET
-- Last Modified: Wed 03 Mar 2021 08:13:25 PM CET

SELECT
     [created_on]   
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
    [email] = {}
