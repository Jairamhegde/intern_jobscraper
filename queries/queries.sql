SELECT s.name,count(*) as demand
FROM skills s
JOIN job_skills js ON s.j_id=js.skill_id
GROUP BY s.name
ORDER BY demand DESC
LIMIT 10;