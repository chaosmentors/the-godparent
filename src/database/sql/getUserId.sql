-- Returns the id of a person, identified by their e-mail address
-- Created On: Wed 17 Feb 2021 10:06:58 PM CET
-- Last Modified: Wed 17 Feb 2021 10:06:58 PM CET

SELECT
    [rowid] as [id]
FROM 
    [Person]
WHERE
    [email] = {};
