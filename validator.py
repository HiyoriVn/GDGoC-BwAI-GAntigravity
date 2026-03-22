from typing import Dict, Set, Tuple

def validate_row(row: Dict[str, str], seen_emails: Set[str]) -> Tuple[bool, str]:
    """
    Validates a normalized row.
    Returns a tuple of (is_valid, issue).
    If is_valid is True, issue will be an empty string.
    """
    email = row.get("email", "")
    if not email:
        return False, "missing_email"
        
    if email in seen_emails:
        return False, "duplicate_email"
        
    ticket_type = row.get("ticket_type", "")
    if ticket_type not in {"vip", "standard", "student"}:
        return False, "unknown_ticket_type"
        
    seen_emails.add(email)
    return True, ""
