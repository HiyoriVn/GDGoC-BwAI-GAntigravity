from typing import Dict

def trim_whitespace(value: str) -> str:
    """Removes leading and trailing whitespace from a string."""
    if value is None:
        return ""
    return str(value).strip()

VIP_MAPPINGS = {"vip", "vip-pass", "vip pass"}
STANDARD_MAPPINGS = {"standard", "std", "standard pass"}
STUDENT_MAPPINGS = {"student", "student ticket"}

def normalize_ticket_type(ticket: str) -> str:
    """
    Normalizes the ticket type to standard values ('vip', 'standard', 'student').
    For any unsupported type, returns the cleaned, lowercase version.
    """
    cleaned = trim_whitespace(ticket).lower()
    
    if cleaned in VIP_MAPPINGS:
        return "vip"
    elif cleaned in STANDARD_MAPPINGS:
        return "standard"
    elif cleaned in STUDENT_MAPPINGS:
        return "student"
        
    return cleaned

def normalize_row(row: Dict[str, str]) -> Dict[str, str]:
    """
    Normalizes an entire row:
    - Trims whitespace in all fields
    - Converts names to title case
    - Converts emails to lowercase
    - Normalizes ticket types 
    """
    normalized = {}
    
    for key, value in row.items():
        if key is None:
            continue
            
        clean_key = trim_whitespace(key)
        clean_value = trim_whitespace(value)
        
        if clean_key == "name":
            normalized[clean_key] = clean_value.title()
        elif clean_key == "email":
            normalized[clean_key] = clean_value.lower()
        elif clean_key == "ticket_type":
            normalized[clean_key] = normalize_ticket_type(clean_value)
        else:
            normalized[clean_key] = clean_value
            
    return normalized
