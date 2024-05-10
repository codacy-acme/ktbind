-- Error 1: Missing semicolon at the end of the statement
SELECT FirstName
FROM Employees
WHERE LastName = 'Smith'

-- Error 2: Missing alias for a table
SELECT FirstName
FROM Employees E
JOIN Orders O ON E.EmployeeID = O.EmployeeID
WHERE LastName = 'Smith'

-- Error 3: Missing single quotes around the string literal
SELECT *
FROM Products
WHERE ProductName = Apple

-- Error 4: Invalid column name in the ORDER BY clause
SELECT OrderID, CustomerName
FROM Orders
ORDER BY ShipCityy

-- Error 5: Invalid column name in the GROUP BY clause
SELECT CategoryName, COUNT(ProductID)
FROM Products
GROUP BY CategoryID

-- Error 6: Invalid use of an aggregate function in the WHERE clause
SELECT CustomerName
FROM Orders
WHERE SUM(OrderAmount) > 1000

-- Error 7: Using a reserved keyword as a table or column name
SELECT *
FROM SELECT
WHERE SELECT.ID = 1

-- Error 8: Missing parentheses around a subquery
SELECT OrderID
FROM Orders
WHERE OrderID IN (SELECT ProductID
                 FROM Products
                 WHERE Price > 100)

-- Error 9: Mismatched data types in a JOIN condition
SELECT FirstName, LastName
FROM Employees
JOIN Orders ON Employees.EmployeeID = Orders.CustomerID

-- Error 10: Unqualified column name in the SELECT list
SELECT OrderID, CustomerName
FROM Orders
WHERE ShipCity = 'Berlin'
ORDER BY OrderID
