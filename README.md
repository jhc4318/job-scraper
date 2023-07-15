Scrape Jobs(title, company, info, Optional(salary)) from LinkedIn (own service)
Scrape Jobs(title, company, salaries) from Glassdoor (own service)
Concurrent requests to Glassdoor pages?
Job title mismatch? Allow leeway with software engineer/developer? Maybe just match company
Links to LinkedIn and Glassdoor references
Company

- Jobs[]

Job

- Title
- Info
- InfoLink
- Salary
- SalaryLink

Store both in JSON, use MongoDB?

Update central store with job posting and salary as a callback whenever other services update?
Update frontend
