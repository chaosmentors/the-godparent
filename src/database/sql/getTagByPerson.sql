-- Returns a list of tags for a specific person id.
-- Created On: Mon 05 Apr 2021 03:37:57 PM CEST
-- Last Modified: Mon 05 Apr 2021 05:50:41 PM CEST

SELECT 
    T.[name]
FROM
    [Tag] AS T
INNER JOIN
    [PersonTag] AS PT
ON
    T.[rowid] = PT.[tag_id]
WHERE
    PT.[person_id] = {}
    
