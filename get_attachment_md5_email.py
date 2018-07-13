# Shoutout to AB for this one; working to modify and smoothen

# This is a script to retrieve the md5 hash of an email attachment. 
# Think static analysis of malicious emails...

# Function extract_payload that extracts the md5 hash of the email attachment and returns the hash as a string
# Arguments: Payload from email
# Output: Hash

import email
import sys
import hashlib
import base64

def extract_payload(payload_to_extract):

    # Decode the attachment from base64 to binary and compute the md5 hash of the file.
    try:
        attachment_decode = base64.b64decode(payload_to_extract)
        file_hash = hashlib.md5(attachment_decode)
        computed_hash = file_hash.hexdigest()
        print(computed_hash)
        return computed_hash
    except UnicodeDecodeError as e:
        print(e)

if __name__ == "__main__":
    # Check if the Command Line Arguments are proper
    if len(sys.argv) != 2:
        print("Usage: scc> python checkEmlAttachment.py email.eml")
        sys.exit(1)

    # Add more function calls to the TRY and mess around with how I can take my lower base code and pass an exception back
    # Mess around with exception. I want to cascade that a thing happend until soeone knows what to do with it
    # Look at requests guy writing exception!!
    # Look at exit codes (possibly passing to syslog)
    try:
        message_file = open(sys.argv[1], 'r')
    except IOError as e:
        print(e)
        sys.exit(1)

    # Use 1 global for loop and call extract_payloads and send_tovt
    try:
        message = email.message_from_file(message_file)
    except Exception as e:
        print(e)
        print("The file specified is most likely not a .eml file. Exiting...")
        sys.exit(1)
    email_payloads = message.get_payload()

    for payload in email_payloads:
        # Check to see if the payload is an attachment or not. If multipart=true, then it is not an attachment.
        if not payload.is_multipart():
            attachment_payload = payload.get_payload()
            payload_hash = extract_payload(attachment_payload)
