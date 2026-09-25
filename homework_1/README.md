# Module 1 Homework: Docker & SQL

## Question 1 — pip version

pip version: 26.2.1 ✅

## Question 2 — Docker networking

Hostname:port: postgres:5432 ✅

## Question 3 — Short trips count

```sql
SELECT
 COUNT(1)
FROM 
 green_taxi_data
WHERE 
 lpep_pickup_datetime >= '2025-11-01' AND 
 lpep_pickup_datetime < '2025-12-01' AND 
 trip_distance <= 1

```

Answer: 8007 ✅

## Question 4 — Longest trip per day

```sql
SELECT
  CAST(lpep_pickup_datetime AS DATE) AS pickup_day,
  trip_distance
FROM 
 green_taxi_data
WHERE 
 trip_distance < 100
ORDER BY 
 trip_distance DESC
LIMIT 1
```

Answer: 2025-11-14 ✅

## Question 5 — Biggest pickup zone

```sql
SELECT
 z."Zone", 
 SUM(gtx.total_amount) as total_amount_sum
FROM
 green_taxi_data gtx
JOIN 
 zones z ON gtx."PULocationID" = z."LocationID"
WHERE
 CAST(gtx.lpep_pickup_datetime AS DATE) = '2025-11-18'
GROUP BY
 z."Zone"
ORDER BY
 total_amount_sum DESC
LIMIT 1

```

Answer: East Harlem North ✅

## Question 6 — Largest tip

```sql
SELECT
 zd."Zone" AS do_zone,
 gtx."tip_amount"
FROM
 green_taxi_data gtx
JOIN 
 zones zp ON gtx."PULocationID" = zp."LocationID"
JOIN 
 zones zd ON gtx."DOLocationID" = zd."LocationID"
WHERE
 zp."Zone" = 'East Harlem North'
ORDER BY
 gtx."tip_amount" DESC
LIMIT 1;
```

Answer: Yorkville West ✅
