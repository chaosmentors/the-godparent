-- Sets the version string after an update was performed.

UPDATE
    [version]
SET
    [last_version] = ? 
WHERE
    [id] = 0
