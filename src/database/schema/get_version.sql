-- Returns the currently saved version string from the database

SELECT
    [latest_version]
FROM
    [version]
WHERE
    [id] = 0
