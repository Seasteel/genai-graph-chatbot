CREATE (d:Department {name: 'IT Department'})
CREATE (e:Employee {name: 'Bat', position: 'Developer'})
CREATE (e)-[:WORKS_IN]->(d)
RETURN d, e
