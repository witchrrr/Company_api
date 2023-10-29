# Company API

This API, built using Django Rest Framework, allows users to manage company details and access employee names in JSON format.

## Features

- **Company Management:** Endpoints to manage company details.
- **Employee Information:** Access all employee names.

## Usage

### Admin Access

- **View/Edit Employees:** Accessible only by admin users. Provides read-only access to view and edit employee information.

### Endpoints

#### Companies

- `GET /api/companies/`: Retrieve all companies.
- `POST /api/companies/`: Create a new company.
- `PUT /api/companies/<company_id>/`: Update a company.
- `DELETE /api/companies/<company_id>/`: Delete a company.

#### Employees

- `GET /api/companies/<company_id>/employees/`: Retrieve all employees of a company.
- `GET /api/employees/<employee_id>/`: Retrieve details of a specific employee.

### Request/Response Formats

All data is returned in JSON format.

## Example

```json
{
  "company_name": "ABC Inc.",
  "location": "New York",
  "employees": [
    {
      "name": "John Doe",
      "email": "john@example.com",
      "position": "Developer"
    },
    {
      "name": "Alice Smith",
      "email": "alice@example.com",
      "position": "Manager"
    }
  ]
}
