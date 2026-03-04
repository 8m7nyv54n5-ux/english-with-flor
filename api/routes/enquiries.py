# api/routes/enquiries.py
# Handles the POST /enquiries endpoint.
# Introduces request bodies — the client sends JSON data to us.

from fastapi import APIRouter
from api.schemas import EnquiryIn, EnquiryOut
from datetime import datetime, timezone

router = APIRouter()


# @router.post — this handles HTTP POST requests, not GET.
# POST is used when the client is sending data to create or submit something.
# response_model=EnquiryOut tells FastAPI what shape to validate and document for the response.
# status_code=201 — 201 Created is the correct HTTP status for a successfully created resource.
#   (The default would be 200 OK, which is technically less accurate for a POST.)
@router.post("/enquiries", response_model=EnquiryOut, status_code=201)
def create_enquiry(enquiry: EnquiryIn):
    """Accept a new enquiry from a prospective student."""
    # `enquiry` is already a validated EnquiryIn object — FastAPI parsed and checked it for us.
    # If name/email/message were missing or the wrong type, FastAPI returned a 422 before we got here.

    # Generate a timestamp for when we received this enquiry.
    # datetime.now(timezone.utc) gives the current time in UTC — always use UTC on servers.
    # .isoformat() converts it to a standard string like "2026-03-04T14:32:00+00:00"
    received_at = datetime.now(timezone.utc).isoformat()

    # Build and return the response.
    # We echo back what was sent (name, email, message) plus our server-generated fields.
    return {
        "name":         enquiry.name,
        "email":        enquiry.email,
        "message":      enquiry.message,
        "received_at":  received_at,
        "confirmation": f"Thanks {enquiry.name}, we've received your message and will be in touch shortly.",
    }
