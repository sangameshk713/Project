class AuditRecord:
    def __init__(self, audit_id, date, auditor_name, location, intersection):
        self.audit_id = audit_id
        self.date = date
        self.auditor_name = auditor_name
        self.location = location
        self.intersection = intersection

    def __repr__(self):
        return (f"AuditRecord(audit_id={self.audit_id}, date={self.date}, "
                f"auditor_name={self.auditor_name}, location={self.location}, "
                f"intersection={self.intersection})")


class SafetyIssue:
    def __init__(self, issue_id, description, severity, date_reported):
        self.issue_id = issue_id
        self.description = description
        self.severity = severity
        self.date_reported = date_reported

    def __repr__(self):
        return (f"SafetyIssue(issue_id={self.issue_id}, description={self.description}, "
                f"severity={self.severity}, date_reported={self.date_reported})")


class SafetyAuditSystem:
    def __init__(self):
        self.audit_records = {}
        self.safety_issues = {}

    # CRUD operations for Audit Records
    def add_audit_record(self, audit_record):
        self.audit_records[audit_record.audit_id] = audit_record
        return True

    def get_audit_record(self, audit_id):
        return self.audit_records.get(audit_id)

    def update_audit_record(self, audit_id, **kwargs):
        audit = self.get_audit_record(audit_id)
        if audit:
            for key, value in kwargs.items():
                setattr(audit, key, value)
            return audit
        return None

    def delete_audit_record(self, audit_id):
        return self.audit_records.pop(audit_id, None)

    # CRUD operations for Safety Issues
    def add_safety_issue(self, safety_issue):
        self.safety_issues[safety_issue.issue_id] = safety_issue
        return True

    def get_safety_issue(self, issue_id):
        return self.safety_issues.get(issue_id)

    def update_safety_issue(self, issue_id, **kwargs):
        issue = self.get_safety_issue(issue_id)
        if issue:
            for key, value in kwargs.items():
                setattr(issue, key, value)
            return issue
        return None

    def delete_safety_issue(self, issue_id):
        return self.safety_issues.pop(issue_id, None)

audit986 = AuditRecord(input(), '2023-03-15', 'madhu', 'Main St', 'Main & First St')
print(audit986.auditor_name)
useFunff = SafetyAuditSystem()
print(useFunff.add_audit_record(audit986))
print(useFunff.get_audit_record(audit986.audit_id))
 
# Unit Testing
import unittest

class TestRoadSafetyAuditSystem(unittest.TestCase):
    def setUp(self):
        self.system = SafetyAuditSystem()
        self.audit = AuditRecord(1, '2023-03-15', 'John Doe', 'Main St', 'Main & First St')
        
        self.issue = SafetyIssue(101, 'Pothole on Main St', 'Medium', '2023-03-15')
        self.system.add_audit_record(self.audit)
        self.system.add_safety_issue(self.issue)

    def test_add_audit_record(self):
        audit = AuditRecord(2, '2023-03-16', 'Jane Smith', 'Second St', 'Second & Third St')
        self.assertTrue(self.system.add_audit_record(audit))

    def test_get_audit_record(self):
        self.assertEqual(self.system.get_audit_record(1), self.audit)

    def test_add_safety_issue(self):
        issue = SafetyIssue(102, 'Faded stop sign', 'High', '2023-03-16')
        self.assertTrue(self.system.add_safety_issue(issue))

    def test_get_safety_issue(self):
        self.assertEqual(self.system.get_safety_issue(101), self.issue)

    def test_update_audit_record(self):
        updated_audit = self.system.update_audit_record(1, location='Updated Main St')
        self.assertEqual(updated_audit.location, 'Updated Main St')

    def test_delete_audit_record(self):
        deleted_audit = self.system.delete_audit_record(1)
        self.assertIsNotNone(deleted_audit)
        self.assertIsNone(self.system.get_audit_record(1))

    def test_update_safety_issue(self):
        updated_issue = self.system.update_safety_issue(101, severity='Low')
        self.assertEqual(updated_issue.severity, 'Low')

    def test_delete_safety_issue(self):
        deleted_issue = self.system.delete_safety_issue(101)
        self.assertIsNotNone(deleted_issue)
        self.assertIsNone(self.system.get_safety_issue(101))

if __name__ == "__main__":
    unittest.main()
