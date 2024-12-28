from difflib import SequenceMatcher
import re

# Normalize text by removing non-alphanumeric characters and making it lowercase
def normalize(text):
    return re.sub(r'[^a-zAZ0-9]', '', text).strip().lower()

# Function to check name match
def name_match(input_name, extracted_name):
    input_parts = input_name.lower().split()
    extracted_parts = extracted_name.lower().split()

    # 1. Exact Letter Match
    if input_name == extracted_name:
        return True
    
    # 2. Abbreviated Names (e.g., "J Smith" vs "John Smith")
    if len(input_parts) == 2 and len(extracted_parts) == 2:
        if input_parts[0] == extracted_parts[0] and extracted_parts[1].startswith(input_parts[1]):
            return True
    
    # 3. Ignoring Middle Names
    if len(input_parts) > len(extracted_parts):
        return False

    # 4. Matching Any Part of the Name
    if any(part in extracted_parts for part in input_parts):
        return True
    
    # 5. Circular Matching (e.g., "Ray Shushi" vs "Shushi Ray")
    if set(input_parts) == set(extracted_parts):
        return True

    return False

# Function to check UID match
def uid_match(input_name, extracted_name, input_uid, extracted_uid):
    # Check if names match first
    if name_match(input_name, extracted_name):
        return True if input_uid == extracted_uid else False
    return False

# Function to check address match
def address_match(input_address, extracted_address):
    normalized_input = normalize(input_address)
    normalized_extracted = normalize(extracted_address)

    # 2. Field-Specific Matching (using similarity ratio)
    similarity = SequenceMatcher(None, normalized_input, normalized_extracted).ratio()
    score = int(similarity * 100)

    # 3. Address mismatch condition: score < 50 is considered mismatched
    if score < 50:
        return f"Address Mismatched (Score: {score})"
    
    return score

# Function to evaluate overall match
def overall_match(name_result, address_result):
    # 1. True cases: Name match and Address match score >= 50
    if name_result and address_result >= 50:
        return True
    return False

# Test cases for 4 persons (including mismatches)
persons = [
    # (name, UID, address, extracted name, extracted UID, extracted address)
    ("John Doe", "123456789012", "123 Baker Street, London", "John D", "123456789012", "123 Baker St., London"),  # True match
    ("Alice Smith", "987654321098", "10 Downing Street, London", "Alice Smith", "987654321097", "10 Downing Street, London"),  # UID mismatch
    ("Michael Johnson", "112233445566", "742 Evergreen Terrace, Springfield", "Michael J", "112233445566", "742 Evergreen Ter, Springfield"),  # Address mismatch
    ("Sarah Lee", "556677889900", "45 High Street, Oxford", "Sarah Lee", "556677889900", "45 High Street, Oxford")  # True match
]

# Run the tests
results = []

for i, person in enumerate(persons):
    input_name, input_uid, input_address, extracted_name, extracted_uid, extracted_address = person

    # Name match
    name_result = name_match(input_name, extracted_name)

    # UID match
    uid_result = uid_match(input_name, extracted_name, input_uid, extracted_uid)

    # Address match
    address_result = address_match(input_address, extracted_address)

    # Overall match
    overall_result = overall_match(name_result, address_result if isinstance(address_result, int) else 0)

    # Add to results
    results.append({
        'person': i+1,
        'name': {
            'input_name': input_name,
            'extracted_name': extracted_name,
            'match': name_result
        },
        'uid': {
            'input_uid': input_uid,
            'extracted_uid': extracted_uid,
            'match': uid_result
        },
        'address': {
            'input_address': input_address,
            'extracted_address': extracted_address,
            'score': address_result
        },
        'overall_match': overall_result
    })

# Display Results
for result in results:
    print(f"Person {result['person']} Results:")
    
    # Name comparison details
    print(f"  Input Name: {result['name']['input_name']}")
    print(f"  Extracted Name: {result['name']['extracted_name']}")
    print(f"  Name Match: {result['name']['match']}")
    
    # UID comparison details
    print(f"  Input UID: {result['uid']['input_uid']}")
    print(f"  Extracted UID: {result['uid']['extracted_uid']}")
    print(f"  UID Match: {result['uid']['match']}")
    
    # Address comparison details
    print(f"  Input Address: {result['address']['input_address']}")
    print(f"  Extracted Address: {result['address']['extracted_address']}")
    print(f"  Address Match Score: {result['address']['score']}")
    
    # Overall match
    print(f"  Overall Match: {result['overall_match']}")
    
    # Remarks
    print("  Remarks:")

    # Check which are not matched
    if not result['name']['match']:
        print("    - Name mismatch")
    if not result['uid']['match']:
        print("    - UID mismatch")
    if isinstance(result['address']['score'], str):  # Address mismatch if score is less than 50
        print(f"    - {result['address']['score']}")
    if not result['overall_match']:
        print("    - Overall match failed")

    print("-" * 50)
