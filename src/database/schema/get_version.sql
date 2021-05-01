-- Returns the currently saved version string from the database

SELECT
    [last_version]
FROM
    [version]
WHERE
    [id] = 0
