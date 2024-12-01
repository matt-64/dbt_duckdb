SELECT
    Species,
    AVG(SepalLengthCm) AS avg_sepal_length,
    AVG(SepalWidthCm) AS avg_sepal_width
FROM {{ source('iris_source', 'iris_source') }}
GROUP BY Species
