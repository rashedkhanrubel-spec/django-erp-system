from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ForeignKey("Employee", on_delete=models.SET_NULL,
                                null=True, blank=True, related_name="managed_dept")

    def __str__(self):
        return self.name

class Employee(models.Model):
    EMPLOYMENT_TYPE = [
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("contract", "Contract"),
    ]
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    join_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"

class LeaveRequest(models.Model):
    STATUS = [("pending","Pending"),("approved","Approved"),("rejected","Rejected")]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

